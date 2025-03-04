# Get the Python version provided as a build argument
ARG PYTHON_VERSION=3.13

# Extend from the latest Debian and its slim version to keep the image as small as possible
FROM python:${PYTHON_VERSION}-slim-bookworm AS builder

# Install necessary packages and Rust
RUN apt-get update && apt-get install -y \
    build-essential \
    clang \
    curl \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && export PATH="$HOME/.cargo/bin:$PATH"

# Set up environment for Rust
ENV PATH="/root/.cargo/bin:$PATH"

# Upgrade pip and install Apify SDK
RUN pip install --upgrade \
    pip \
    setuptools \
    wheel

# Create and activate a virtual environment for Python dependencies in /opt
RUN python -m venv /opt/.venv
ENV PATH="/opt/.venv/bin:$PATH"

# Copy requirements and install dependencies separately for caching benefits
COPY requirements.txt ./
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

# Final stage
FROM python:${PYTHON_VERSION}-slim-bookworm

# Copy the virtual environment from the builder
COPY --from=builder /opt/.venv /opt/.venv
# Copy the Playwright dependencies from the builder
COPY --from=builder /root/.cache/ms-playwright/chromium_headless_shell-1155 /root/.cache/ms-playwright/chromium_headless_shell-1155
# Copy the Playwright dependencies from the builder (directory would be /usr/lib/aarch64-linux-gnu on ARM)
COPY --from=builder /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu

# Set the PATH to include the virtual environment's bin directory
ENV PATH="/opt/.venv/bin:$PATH"

# Copy over application-specific files
COPY . ./

# Set default startup command:
# 1+2. Print the URL where the app is running
# 3. Run the streamlit app on port 4321 and redirect stdout and stderr to /dev/null (to avoid logs in the console)
CMD sh -c 'echo "You can now view your Streamlit app in your browser." && \
    echo "URL: ${ACTOR_WEB_SERVER_URL}" && \
    streamlit run ai_scrapper.py --server.port=4321 >/dev/null 2>&1'
