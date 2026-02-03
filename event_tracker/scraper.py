from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def fetch_events(city):
    driver = webdriver.Chrome()
    driver.get("https://www.district.in/")
    time.sleep(6)

    # STEP 1: collect event URLs
    event_urls = set()
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/events/']")
    for l in links:
        url = l.get_attribute("href")
        if url:
            event_urls.add(url)

    events = []

    # STEP 2: open each event page
    for url in list(event_urls)[:15]:
        try:
            driver.get(url)
            time.sleep(4)

            # Event Name
            try:
                event_name = driver.find_element(By.TAG_NAME, "h1").text.strip()
            except:
                event_name = "N/A"

            # Date
            try:
                date = driver.find_element(By.TAG_NAME, "time").text.strip()
            except:
                date = "N/A"

            # Venue
            try:
                venue = driver.find_element(By.XPATH, "//*[contains(text(),'Venue')]").text
            except:
                venue = "N/A"

            # Category
            try:
                category = driver.find_element(By.CSS_SELECTOR, "a[href*='category']").text
            except:
                category = "general"

            events.append({
                "event_name": event_name,
                "date": date,
                "venue": venue,
                "city": city,
                "category": category,
                "url": url,
                "status": "active"
            })

        except:
            continue

    driver.quit()
    return pd.DataFrame(events)
