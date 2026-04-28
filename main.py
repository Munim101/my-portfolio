AI Web Scraper — Munim Awal
============================
Built with Python, Streamlit, Selenium, BeautifulSoup, and Ollama (LLaMA 3).

SETUP:
1. Install dependencies:    pip install -r requirements.txt
2. Install Ollama:          https://ollama.com
3. Pull the model:          ollama pull llama3
4. Download ChromeDriver matching your Chrome version and place chromedriver.exe in this folder
5. Run the app:             streamlit run main.py

HOW IT WORKS:
- Enter any URL → scrapes the page using Selenium
- Cleans and extracts the body content
- Describe what you want to extract → LLaMA 3 parses and returns structured results
