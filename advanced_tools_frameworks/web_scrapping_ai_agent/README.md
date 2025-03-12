Sure! Here's the updated README with added emojis for a more engaging and visually appealing presentation:

---

# 💻 Web Scraping AI Agent

This **Apify Streamlit app Actor** enables intelligent web scraping using **OpenAI's API** and the `scrapegraphai` library. With this app, you can scrape any website by simply providing the URL and specifying the data you need extracted. You can run it directly on the **Apify platform** for hassle-free scaling and management. 🚀

## 💡 Why Apify Actors Are Powerful

Apify Actors provide an easy and efficient way to run your web scraping tasks at scale. They are fully-managed, cloud-based containers designed for tasks like web scraping, automation, and data extraction. [Learn more about Apify Actors in the whitepaper here](https://whitepaper.actor/). 📖

---

## 🌟 Features

- **Scrape any website** by providing the URL. 🌍
- **Leverage OpenAI's LLMs** (GPT-3.5-turbo or GPT-4) for intelligent data extraction. 🤖💬
- **Run as an Apify Actor** on the Apify platform for seamless deployment and scaling. ⚡
- **Customize your scraping task** by providing specific user prompts. ✍️

---

## 🔧 How to Get Started?

### 🅰️ Run as an Apify Actor

See full guide in [Apify Academy](https://docs.apify.com/academy/getting-started/actors)📚

This project is already set up as an **Apify Actor**, allowing you to easily deploy it on the Apify platform.

1. **Initialize the Apify Actor** (already done in the repository):

   ```bash
   apify init
   ```

   This creates `.actor/actor.json` with the configuration and the necessary Dockerfile. 🛠️

2. **Refactor the Code**:

   The code has been refactored to separate the logic into a function that handles input and output independently, improving maintainability and scalability. This function now takes the inputs (URL, prompt, model choice) and returns the extracted output, allowing for better handling in the Apify environment. 🔄

3. **Build the Actor**:

   [Learn more about building an Actor in the Apify Docs](https://docs.apify.com/academy/getting-started/creating-actors#build-an-actor). 🏗️

4. **Run the Actor**:

   [Learn how to run Actors in the Apify console](https://docs.apify.com/academy/getting-started/creating-actors#run-the-actor)📚  
   This will trigger the process on the Apify platform, and you’ll receive logs detailing the results.

---

### 🅱️ Run Locally

1. **Clone the GitHub Repository:**

   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/advanced_tools_frameworks/web_scrapping_ai_agent
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Get Your OpenAI API Key:**
   - Sign up for an [OpenAI account](https://platform.openai.com/) (or another LLM provider) and obtain your API key. 🔑

4. **Run the App:**

   The app has been refactored to remove Streamlit, and it now focuses on the core logic for scraping. You can run the function directly as a Python script:

   ```bash
   python run_ai_scraper.py
   ```

---

## 📦 Dockerized for Apify 🐳

This project includes a **Dockerfile** optimized for Apify deployment, inspired by the official Apify templates:

- **Multi-stage build** to keep the Docker image as small as possible.
- Installs **Rust** for building the `minify-html` dependency of `scrapegraphai`.
- **Playwright update** for enhanced web scraping capabilities.
- **Streamlit removal** to optimize the actor's performance and reduce unnecessary dependencies.
- **Concurrency Handling**: Apify Actor's entrypoint function is optimized to handle concurrency and process multiple requests in parallel while managing inputs and outputs efficiently.

---

## 🔍 How It Works

1. Upon starting the actor, you will pass the necessary inputs to the **entrypoint function**. 🚪
2. The **entrypoint function** maps Apify input parameters to the scraping logic function, ensuring concurrency is handled efficiently. 🔄
3. The **scraping logic function** uses the inputs (URL, OpenAI model, user prompt) and returns the processed data. 🧠
4. The result is returned by the actor, which can be saved to Apify datasets or returned as an output for further processing. 📈

---

## 📖 Learn More

- Want to understand why **Apify Actors** are the ideal solution for scalable web scraping? Check out the [Apify Whitepaper](https://whitepaper.actor/) for more insights. 📜

---

This **Web Scraping AI Agent** is perfect for AI-powered data extraction, whether you're conducting research, automating workflows, or gathering business intelligence. With Apify’s platform, you can deploy and scale the app with ease. 🚀

---

### Additional Notes for Apify Actor Development

- **Code Refactor**: The code has been refactored to separate the logic into a function that accepts inputs and returns outputs, facilitating better scalability and reusability in the Apify Actor environment. 🛠️
- **Concurrency**: The entrypoint function handles multiple requests concurrently, allowing the actor to scale efficiently. 🔄
- **No Streamlit**: Streamlit has been removed from the app as the primary focus is on backend scraping logic, which is now suitable for Apify actor deployment. ❌
