
import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Get the HTML content of the page
html = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# List where to store the scraped titles
titles = []

# List of header levels (h1, h2, h3, h4, h5)
title_level_list = [1, 2, 3, 4, 5]

# Loop through each header level (h1, h2, h3, h4, h5)
for title_level in title_level_list:
    # Find all elements of the current header level
    title_elements = soup.find_all(f"h{title_level}")

    # Loop through each title element found
    for title_element in title_elements:
        # Data extraction logic
        tag = title_element.name
        text = title_element.text

        # Create a dictionary with the tag and the title text
        title = {
            "tag": tag,
            "title": text,
        }

        # Append the dictionary to the titles list
        titles.append(title)

# Open a CSV file to write the data
with open("titles.csv", mode="w", newline="", encoding="utf-8") as file:
    # Create a CSV writer object and specify the fieldnames (columns)
    writer = csv.DictWriter(file, fieldnames=["tag", "title"])

    # Write the header (column names) to the CSV file
    writer.writeheader()

    # Write each row (dictionary) to the CSV file
    for row in titles:
        writer.writerow(row)
