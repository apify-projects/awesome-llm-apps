# 💻 Web Scraping AI Agent

This **Apify Streamlit app Actor** enables intelligent web scraping using **OpenAI's API** and the `scrapegraphai` library. With this app, you can scrape any website by simply providing the URL and specifying what data you need extracted. You can run it directly on the **Apify platform** for hassle-free scaling and management. 🚀

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

   This creates `.actor/actor.json` with the configuration.
   You also need to provide right `Dockerfile`.

2. **Build the Actor:**

   [Learn more about building an Actor in the Apify Docs](https://docs.apify.com/academy/getting-started/creating-actors#build-an-actor). 🏗️

3. **Run the Actor:**

   [Learn how to run Actors in the Apify console](https://docs.apify.com/academy/getting-started/creating-actors#run-the-actor)📚
   This will start the Streamlit app on the Apify platform, and the logs will display the URL where you can access it.

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

4. **Run the Streamlit App:**

   ```bash
   streamlit run ai_scrapper.py
   ```

---

## 📦 Dockerized for Apify 🐳

This project includes a **Dockerfile** optimized for Apify deployment:

- **Multi-stage build** to keep the Docker image as small as possible.
- Installs **Rust** for building the `minify-html` dependency of `scrapegraphai`.
- **Playwright update** for enhanced web scraping capabilities.
- **Streamlit log suppression** to avoid clutter in logs.
- Runs **Streamlit on port 4321**, which is compatible with Apify.

---

## 🔍 How It Works

1. Upon starting the app, you’ll be prompted to enter your OpenAI API key.
2. Select the **language model** (GPT-3.5-turbo or GPT-4) you wish to use for scraping.
3. Enter the **URL** of the website you want to scrape.
4. Specify **what data** you want the AI agent to extract by providing a custom user prompt.
5. The app will create a `SmartScraperGraph` object to process the scraping request.
6. The extracted data is then displayed in the **Streamlit app**.

---

## 📖 Learn More

- Want to understand why **Apify Actors** are the ideal solution for scalable web scraping? Check out the [Apify Whitepaper](https://whitepaper.actor/) for more insights. 📜

---

This **Web Scraping AI Agent** is perfect for AI-powered data extraction, whether you're conducting research, automating workflows, or gathering business intelligence. With Apify’s platform, you can deploy and scale the app with ease. 🚀
