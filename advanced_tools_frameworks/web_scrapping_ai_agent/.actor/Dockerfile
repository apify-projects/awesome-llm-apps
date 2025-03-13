# First, specify the base Docker image.
# You can see the Docker images from Apify at https://hub.docker.com/r/apify/.
# You can also use any other image from Docker Hub.
FROM apify/actor-python-playwright:3.13 AS builder

# Install necessary build tools (clang, rust, build-essential) and dependencies
RUN echo "Installing build tools and dependencies..." \
    && apt-get update && apt-get install -y \
    build-essential \
    clang \
    curl \
    # Install Rust
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && export PATH="$HOME/.cargo/bin:$PATH"

# Set up environment for Rust
ENV PATH="/root/.cargo/bin:$PATH"

# Second, copy just requirements.txt into the Actor image,
# since it should be the only file that affects the dependency install in the next step,
# in order to speed up the build
COPY requirements.txt ./

# Create and activate a virtual environment for Python dependencies in /opt
RUN python -m venv /opt/.venv
ENV PATH="/opt/.venv/bin:$PATH"

# Install the packages specified in requirements.txt,
# Print the installed Python version, pip version
# and all installed packages with their versions for debugging
RUN echo "Python version:" \
    && python --version \
    && echo "Pip version:" \
    && pip --version \
    && echo "Installing dependencies:" \
    && pip install -r requirements.txt \
    && echo "All installed Python packages:" \
    && pip freeze

# Install Playwright and its dependencies
RUN playwright install-deps && \
    playwright install

# Use compileall to ensure the runnability of the Actor Python code.
RUN python3 -m compileall -q .

# Stage 2: Final lightweight runtime image
FROM python:3.13-slim-bookworm

# Set the PATH to include the virtual environment's bin directory
ENV PATH="/opt/.venv/bin:$PATH"

# Copy virtual environment with installed dependencies
COPY --from=builder /opt/.venv /opt/.venv

# Copy the Playwright dependencies from the builder
COPY --from=builder /root/.cache/ms-playwright/chromium_headless_shell-1155 /root/.cache/ms-playwright/chromium_headless_shell-1155

# Copy the Playwright dependencies (system libraries) from the builder (directory would be /usr/lib/aarch64-linux-gnu on ARM)
COPY --from=builder /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu

# Copy application source code
COPY . ./

# Run the application
CMD ["python3", "-m", "src"]
