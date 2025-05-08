import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        driver.get(website)
        time.sleep(5)
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    return str(body) if body else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    cleaned = soup.get_text(separator="\n")
    cleaned = "\n".join([line.strip() for line in cleaned.splitlines() if line.strip()])
    return cleaned

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
