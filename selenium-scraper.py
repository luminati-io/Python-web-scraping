from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

# Set up the WebDriver that operates in headless mode
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(), options=options)

# URL of the page to scrape
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Open the URL in the browser
driver.get(url)

# List to store the scraped titles
titles = []

# List of header levels (h1, h2, h3, h4, h5)
title_level_list = [1, 2, 3, 4, 5]

# Loop through each header level (h1, h2, h3, h4, h5)
for title_level in title_level_list:
    # Find all elements of the current header level using a CSS Selector
    title_elements = driver.find_elements(By.CSS_SELECTOR, f"h{title_level}")

    # Loop through each title element found
    for title_element in title_elements:
        # Data extraction logic
        tag = title_element.tag_name
        text = title_element.text

        # Create a dictionary with the tag and the title text
        title = {
            "tag": tag,
            "title": text,
        }

        # Append the dictionary to the titles list
        titles.append(title)

# Close the browser
driver.quit()

# Open a CSV file to write the data
with open("titles.csv", mode="w", newline="", encoding="utf-8") as file:
    # Create a CSV writer object and specify the fieldnames (columns)
    writer = csv.DictWriter(file, fieldnames=["tag", "title"])

    # Write the header (column names) to the CSV file
    writer.writeheader()

    # Write each row (dictionary) to the CSV file
    for row in titles:
        writer.writerow(row)
