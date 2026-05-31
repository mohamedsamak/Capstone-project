import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv()


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

FORM_LINK = os.getenv("FORM_LINK")

for n in range(len(all_links)):
    driver.get(FORM_LINK)
    time.sleep(2)
    
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    inputs[0].send_keys(all_addresses[n])
    inputs[1].send_keys(all_prices[n])
    inputs[2].send_keys(all_links[n])
    
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    
    time.sleep(2)
    
    driver.find_element(By.LINK_TEXT, "إرسال رد آخر").click()