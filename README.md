
# Python Web Scraping Guide

In this Python Web Scraping repository, you will find everything you need to get started with web scraping. We will explore how web scraping works, dive into various approaches in Python, and review complete examples at the end.

Python is widely considered one of the [best languages for web scraping](https://brightdata.com/blog/web-data/best-languages-web-scraping) thanks to its simple syntax and a vast selection of open-source libraries. Time to learn more about it!

## Table of Contents
- [Web Scraping Logic in Python](#web-scraping-logic-in-python)
- [Python Web Scraping Libraries](#python-web-scraping-libraries)
   * [HTTP Clients](#http-clients)
   * [HTML Parsers](#html-parsers)
   * [Browser Automation](#browser-automation)
   * [All-in-One Scraping](#all-in-one-scraping)
- [Common Stacks for Scraping in Python](#common-stacks-for-scraping-in-python)
- [Prerequisites](#prerequisites)
- [Web Scraping with Requests and Beautiful Soup](#web-scraping-with-requests-and-beautiful-soup)
   * [Features](#features)
      + [Requests](#requests)
      + [Beautiful Soup](#beautiful-soup)
   * [Setup](#setup)
   * [Methods](#methods)
      + [Connect to a Web Page](#connect-to-a-web-page)
      + [Parse an HTML String](#parse-an-html-string)
      + [Basic Node Selection and Data Extraction Methods](#basic-node-selection-and-data-extraction-methods)
      + [Find Nodes](#find-nodes)
      + [Select Nodes](#select-nodes)
- [Export the Scraped Data](#export-the-scraped-data)
   * [CSV Export](#csv-export)
   * [JSON Export](#json-export)
- [Web Scraping Examples in Python](#web-scraping-examples-in-python)
   * [1. Requests + Beautiful Soup](#1-requests-beautiful-soup)
   * [2. Selenium](#2-selenium)
   * [Scrapy](#scrapy)
- [Challenges of Python Web Scraping](#challenges-of-python-web-scraping)
- [Simplified Web Scraping With Web Scraper API](#simplified-web-scraping-with-web-scraper-api)

## Web Scraping Logic in Python
The main building blocks for any [Python web scraping](https://brightdata.com/blog/how-tos/web-scraping-with-python) script are:
1. Retrieve the HTML of the target page.
2. Parse the HTML into a Python object.
3. Extract data from the parsed HTML.
4. Export the extracted data to a human-readable format, such as CSV or JSON.

The approach for the first two steps depends on whether the target page is static or dynamic:
- **Static Sites**: Use an HTTP client like [Requests](https://requests.readthedocs.io/en/latest/) to request the HTML directly from the server. After receiving the response, parse the HTML using an HTML parser like [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
- **Dynamic Sites**: Use a browser automation tool (e.g., [Selenium](https://selenium-python.readthedocs.io/)) to load the page in a headless browser. This approach enables you to render dynamic content before parsing it with the browser engine.

For step 3, the high-level logic for extracting data depends on the DOM structure of the page. However, the implementation will vary based on the tools you choose and the methods they provide for HTML node selection and data extraction.

Finally, keep in mind that there are also all-in-one web scraping tools like [Scrapy](https://scrapy.org/). These libraries simplify the process by integrating all four steps into a single platform, streamlining the scraping workflow.

## Python Web Scraping Libraries
Discover some of the most useful libraries for web scraping with Python. For a comprehensive list, refer to our [Awesome Web Scraping repository](https://github.com/luminati-io/Awesome-Web-Scraping/blob/main/python.md).

### HTTP Clients
- [`requests`](https://github.com/kennethreitz/requests): A simple, yet elegant HTTP library.
- [`httpx`](https://github.com/encode/httpx): A next generation HTTP client for Python.
- [`aiohttp`](https://github.com/aio-libs/aiohttp): An asynchronous HTTP client/server framework for `asyncio` and Python.

### HTML Parsers
- [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/): A program designed for screen-scraping HTML.
- [`lxml`](https://github.com/lxml/lxml/): A feature-rich and easy-to-use library for processing XML and HTML in the Python language
- [`html5lib`](https://github.com/html5lib/html5lib-python): A Standards-compliant library for parsing and serializing HTML documents and fragments in Python

### Browser Automation
- [`selenium`](https://github.com/SeleniumHQ/selenium): A browser automation framework and ecosystem.
- [`playwright`](https://github.com/microsoft/playwright-python): A Python version of the Playwright testing and automation library.
- [`pyppeteer`](https://github.com/pyppeteer/pyppeteer): A headless Chrome/Chromium automation library (unofficial port of Puppeteer).

### All-in-One Scraping
- [`scrapy`](https://github.com/scrapy/scrapy): A fast high-level web crawling & scraping framework for Python.
- [`autoscraper`](https://github.com/alirezamika/autoscraper): A smart, automatic, fast and lightweight web scraper for Python.
- [`requests-html`](https://github.com/psf/requests-html): A library that intends to make parsing HTML (e.g. scraping the web) as simple and intuitive as possible.

## Common Stacks for Scraping in Python
Compare the three most common Python web scraping stacks in the following table:
|                               | **Requests + Beautiful Soup**                                                                            | **Selenium**                                                                                  | **Scrapy**                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Description**               | Uses Requests to fetch the HTML content of a webpage, and Beautiful Soup for parsing and extracting data | Automates web browsers to interact with dynamic sites, fetch data, and simulate user behavior | A powerful framework for large-scale web scraping tasks                                                                           |
| **Requirements**              | - `requests`<br>- `beautifulsoup4`                                                                       | -  `selenium`<br>- A web browser like Chrome, Firefox, or Edge                                | - `scrapy`                                                                                                                        |
| **Support for Static Pages**  | Yes                                                                                                      | Yes                                                                                           | Yes                                                                                                                               |
| **Support for Dynamic Pages** | No                                                                                                       | Yes                                                                                           | Not available out of the box, but can be accessed via the [Scrapy Splash plugin](https://github.com/scrapy-plugins/scrapy-splash) |
| **Best For**                  | Simple scraping tasks                                                                                    | Scraping dynamic websites that require user interaction                                       | Large-scale scraping projects, involving web crawling                                                                             |

You are ready to see how to perform web scraping using Requests + Beautiful Soup, which is the most common approach to data scraping in Python.

## Prerequisites
To perform web scraping in Python, you will need:
- Python 3+ installed on your machine.
- A Python project set up with a [virtual environment](https://docs.python.org/3/library/venv.html) where you can install the required scraping libraries.

Also, using a Python IDE like [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python) or [PyCharm](https://www.jetbrains.com/pycharm/) will make writing and managing your code much easier.

## Web Scraping with Requests and Beautiful Soup
Let’s now jump into web scraping with Beautiful Soup, using Requests as the HTTP client.

**Note**: You can easily extend the following examples to Selenium-based web scraping or Scrapy-based web scraping.

For a dedicated tutorial, refer to our guide on [web scraping with Beautiful Soup](https://brightdata.com/blog/how-tos/beautiful-soup-web-scraping).

### Features
Explore the main capabilities provided by Requests and Beautiful Soup.

#### Requests
- Support for HTTP requests in any method (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`).
- Handles HTTP headers, cookies, and query parameters with ease.
- Supports SSL/TLS verification for secure connections.
- Automatic decoding of response content based on the server-provided encoding.
- Built-in session handling for maintaining cookies and authentication.
- Streamlined error handling for HTTP errors ([`4xx` and `5xx` response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)).

#### Beautiful Soup
- Parses HTML and XML documents into a Python-readable format.
- Provides methods to search for elements using tags, attributes, and text.
- Supports multiple parsers, including the fast built-in HTML parser [`html.parser`](https://docs.python.org/3/library/html.parser.html) and external parsers like `lxml`.
- Handles poorly formatted or broken HTML gracefully.
- Facilitates easy navigation (and modification) of parsed HTML content.
- Integrates seamlessly with Requests and any other [Python HTTP client](https://brightdata.com/blog/web-data/best-python-http-clients) for complete web scraping workflows.

### Setup
To install Requests and Beautiful Soup in your project, execute the following command in your activated virtual environment:
```bash
pip install requests beautifulsoup4
```
You can then import the two libraries with:
```python
import requests
from bs4 import BeautifulSoup
```
### Methods
Explore the most common operations for Python web scraping, made possible by the methods provided by Requests and Beautiful Soup.

#### Connect to a Web Page
Retrieve the HTML of a web page with the [`get()`](https://requests.readthedocs.io/en/latest/api/#requests.get) method exposed by Requests:
```python
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
```
Replace `url` with the URL of your target page.

Behind the scenes, Requests performs an HTTP `GET` request to the specified URL. The website's server responds with a response object containing the page's HTML. Verify that by printing `response`:
```python
print(response)
```
The output should look like this:
```
<Response [200]>
```
The HTTP response status code of [`200`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) means that the request was successful.

To extract the HTML content from the response object, access the `text` attribute:
```python
print(response.text)
```
This will print the HTML content of the page:
```html
<!DOCTYPE html>
<html
  class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-pinned-clientpref-1 vector-feature-night-mode-enabled skin-theme-clientpref-day vector-toc-available"
  lang="en"
  dir="ltr"
>
  <head>
    <meta charset="UTF-8">
    <title>Web scraping - Wikipedia</title>
    <!-- omitted for brevity... -->
  </head>
</html>
```
The output is a string containing the raw HTML of the page.

#### Parse an HTML String
You can parse an HTML string by passing it to the Beautiful Soup constructor:
```python
soup = BeautifulSoup(html, "html.parser")
```
The first argument is a variable containing the raw HTML as a string. Instead, the second argument specifies the parser to use for processing the HTML. Here, `html.parser` is the default HTML parser provided by Python's standard library.

The resulting `soup` variable contains methods and attributes that allow you to select HTML nodes, modify the DOM, and access and manipulate data within selected nodes.

#### Basic Node Selection and Data Extraction Methods
You can retrieve the `<title>` element of the page as follows:
```python
print(soup.title)

# OUTPUT:
# <title>Web scraping - Wikipedia</title>
```
To extract the text inside the `<title>` element, use the `text` attribute:
```python
print(soup.title.text)

# OUTPUT:
# Web scraping - Wikipedia
```
Similarly, you can access the `<h1>` element like this:
```python
print(soup.h1)

# OUTPUT:
# <h1 class="firstHeading mw-first-heading" id="firstHeading">
#   <span class="mw-page-title-main">Web scraping</span>
# </h1>
```python
To retrieve the value of an HTML attribute (e.g., `id`), access it using the attribute name as a dictionary key:
```python
print(soup.h1["id"])

# OUTPUT:
# firstHeading
```
#### Find Nodes
Two of the most commonly used methods in Beautiful Soup for finding HTML elements are [`find()` and `find_all()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all). These methods enable you to locate specific elements or groups of elements within an HTML document.

Here is a quick overview:
- `find()`: Locates the first matching element.
- `find_all()`: Returns a list of all matching elements.

The signature for `find()` looks like this:
```python
find(name=None, attrs={}, recursive=True, text=None, **kwargs)
```
This shows that `find()` can search by tag name, attributes, or text content. To find an element by class or ID, the `**kwargs` parameter allows you to filter easily.

For example, to get the `<h1>` element with `id="firstHeading"`, you can write:
```python
h1 = soup.find("h1", id="firstHeading")
print(h1)

# OUTPUT:
# <h1 class="firstHeading mw-first-heading" id="firstHeading">
#   <span class="mw-page-title-main">Web scraping</span>
# </h1>
```
Although `id` is not an explicit parameter of `find()`, the logic above works seamlessly thanks to the flexibility of `**kwargs`.

If you need all elements of a particular type, such as headings or links, `find_all()` is the better choice. For instance, to get all `<a>` tags:
```python
links = soup.find_all("a")
print(links)

# OUTPUT:
# [
#     <a class="mw-jump-link" href="#bodyContent">Jump to content</a>,
#     <a accesskey="z" href="/wiki/Main_Page" title="Visit the main page [z]">
#         <span>Main page</span>
#     </a>,
#     <a href="/wiki/Wikipedia:Contents" title="Guides to browsing Wikipedia">
#         <span>Contents</span>
#     </a>,
#     omitted for brevity...
# ]
```
This method returns a list of matching elements, enabling you to easily loop through them and perform operations, such as extracting their text. For example, you can extract the text content of all matching elements using the following code:
```python
links = soup.find_all("a")
for link in links:
  print(link.text)

# OUTPUT:
# Jump to content
# Main page
# Contents
# omitted for brevity...
```
You can also combine tag names with attribute filters to narrow down your search. For example, to find all `<span>` tags with `class="mw-editsection"`, write:
```python
specific_spans = soup.find_all("span", {"class": "mw-editsection"})
```
Or, equivalently:
```python
specific_spans = soup.find_all("span", class_="mw-editsection")
```
Since `class` is a reserved keyword in Python, you cannot use it directly as a parameter. Instead, you should `class_`.

Both approaches will return a list of all `<span>` elements that match the specified criteria:
```
[
    <span class="mw-editsection">
        <span class="mw-editsection-bracket">[</span>
        <a href="/w/index.php?title=Web_scraping&amp;action=edit&amp;section=1" title="Edit section: History">
            <span>edit</span>
        </a>
        <span class="mw-editsection-bracket">]</span>
    </span>,
    <span class="mw-editsection">
        <span class="mw-editsection-bracket">[</span>
        <a href="/w/index.php?title=Web_scraping&amp;action=edit&amp;section=2" title="Edit section: Techniques">
            <span>edit</span>
        </a>
        <span class="mw-editsection-bracket">]</span>
    </span>,
    <!-- omitted for brevity... -->
]
```
Note that the objects returned by `find()` and `find_all()` expose these two methods as well. When called on result nodes, the scope of `find()` and `find_all()` will be limited to their child nodes.
For example, select the HTML element containing the page references by class:
```python
references_element = soup.find(class_="references")
```
Then, get all `<li>` tags inside this element and print their content with:
```python
list_items = references_element.find_all("li")
for item in list_items:
    print(item.text)

# OUTPUT:
# ^ Thapelo, Tsaone Swaabow; Namoshe, Molaletsa; Matsebe, Oduetse; Motshegwa, Tshiamo; Bopape, Mary-Jane Morongwa (2021-07-28). "SASSCAL WebSAPI: A Web Scraping Application Programming Interface to Support Access to SASSCAL's Weather Data". Data Science Journal. 20: 24. doi:10.5334/dsj-2021-024. ISSN 1683-1470. S2CID 237719804.
# ^ "Search Engine History.com". Search Engine History. Retrieved November 26, 2019.
# ^ Song, Ruihua; Microsoft Research (Sep 14, 2007). "Joint optimization of wrapper generation and template detection" (PDF). Proceedings of the 13th ACM SIGKDD international conference on Knowledge discovery and data mining. p. 894. doi:10.1145/1281192.1281287. ISBN 9781595936097. S2CID 833565. Archived from the original (PDF) on October 11, 2016.
# omitted for brevity...
```

#### Select Nodes
Another useful method in Beautiful Soup for locating elements is [`select()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property). This function allows you to find elements using [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors), which offer a powerful and flexible way to target elements based on their tags, classes, ids, and other attributes.

For example, you can get all `<li>` elements inside the `.references` nodes with:
```python
li_elements = soup.select(".references > li")
print(len(li_elements))

# OUTPUT:
# 31
```

## Export the Scraped Data
Once you have scraped data from the target page, you will likely find yourself with a dictionary containing the extracted data. For instance, suppose your `titles` dictionary list with scraped data contains:
```
[
    {'tag': 'h1', 'title': 'Web scraping'},
    {'tag': 'h2', 'title': 'Contents'},
    {'tag': 'h2', 'title': 'History'},
    {'tag': 'h2', 'title': 'Techniques'},
    {'tag': 'h2', 'title': 'Legal issues'},
    {'tag': 'h2', 'title': 'Methods to prevent web scraping'},
    # ...
    {'tag': 'h3', 'title': 'India'}
]
```
Usually, you want to export this data into a human-readable format like CSV or JSON, so that other members of your team can easily access and use it. Let's see how to export it in both formats!

**Note**: The data export logic below applies to scraping scripts that do not use an all-in-one scraping solution like Scrapy. The reason is that solutions typically include built-in [features for exporting data directly in the desired format through specific configurations](https://docs.scrapy.org/en/latest/topics/feed-exports.html).

### CSV Export
To export the data to CSV, you can use the use Python's built-in [`csv`](https://docs.python.org/3/library/csv.html) module. This module enables you to write data to a `.csv` file, where each key in the dictionary corresponds to a column header, and the values become the corresponding rows.

First, open a CSV file called `titles.csv` where to write data using the [`open()`](https://docs.python.org/3/library/functions.html#open) function:
```python
with open("titles.csv", mode="w", newline="", encoding="utf-8") as file:
```
In this case, `"w"` is used for writing to the file, and `newline=""` guarantees that rows are written correctly without extra blank lines between them. Note the use of the [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#with), which ensures that the file is properly closed after the operation is complete.

Next, write the header—which will correspond to the dictionary keys—using a [`DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter) class:
```python
writer = csv.DictWriter(file, fieldnames=["tag", "title"])
writer.writeheader()
```
After the header, you can write the data itself with the `writer.writerow()` method by iterating over the dictionary list:
```python
for row in titles:
    writer.writerow(row)
```
The above logic will write the entire rows, where the keys correspond to the columns, and the values are the actual data from the dictionary.

Finally, the `with` statement will automatically take care of closing the file after writing.

The output will be something like this:
```csv
tag,title
h1,Web scraping
h2,Contents
h2,History
h2,Techniques
h2,Legal issues
h2,Methods to prevent web scraping
h2,See also
h2,References
h3,Human copy-and-paste
h3,Text pattern matching
h3,HTTP programming
h3,HTML parsing
h3,DOM parsing
h3,Vertical aggregation
h3,Semantic annotation recognizing
h3,Computer vision web-page analysis
h3,AI-powered document understanding
h3,United States
h3,European Union
h3,Australia
h3,India
```
You can find the same result in `titles.csv` file in the repository.

### JSON Export
To export the scraped data to JSON, you can utilize the Python built-in [`json`](https://docs.python.org/3/library/json.html) module. This module allows you to convert Python dictionaries to a JSON-formatted string and write it to a `.json` file.

First, open a JSON file called `titles.json` for writing using the `open()` function:
```python
with open("titles.json", mode="w", encoding="utf-8") as file:
```
Again, the `with` statement ensures that the file will be automatically closed after the operation is complete.

Next, use the `json.dump()` function to convert your dictionary into JSON format and write it to the file:
```python
json.dump(titles, file, indent=4)
```
The `indent=4` argument ensures that the JSON data is pretty-printed with an indentation level of 4 spaces, making it human-readable.

The output will look something like this:
```json
[
    {
        "tag": "h1",
        "title": "Web scraping"
    },
    {
        "tag": "h2",
        "title": "Contents"
    },
    {
        "tag": "h2",
        "title": "History"
    },
    {
        "tag": "h2",
        "title": "Techniques"
    },
    {
        "tag": "h2",
        "title": "Legal issues"
    },
    {
        "tag": "h2",
        "title": "Methods to prevent web scraping"
    },
    {
        "tag": "h2",
        "title": "See also"
    },
    {
        "tag": "h2",
        "title": "References"
    },
    {
        "tag": "h3",
        "title": "Human copy-and-paste"
    },
    {
        "tag": "h3",
        "title": "Text pattern matching"
    },
    {
        "tag": "h3",
        "title": "HTTP programming"
    },
    {
        "tag": "h3",
        "title": "HTML parsing"
    },
    {
        "tag": "h3",
        "title": "DOM parsing"
    },
    {
        "tag": "h3",
        "title": "Vertical aggregation"
    },
    {
        "tag": "h3",
        "title": "Semantic annotation recognizing"
    },
    {
        "tag": "h3",
        "title": "Computer vision web-page analysis"
    },
    {
        "tag": "h3",
        "title": "AI-powered document understanding"
    },
    {
        "tag": "h3",
        "title": "United States"
    },
    {
        "tag": "h3",
        "title": "European Union"
    },
    {
        "tag": "h3",
        "title": "Australia"
    },
    {
        "tag": "h3",
        "title": "India"
    }
]
```
You can find the same result in the `titles.json` file in the repository.

## Web Scraping Examples in Python
Assume you want to scrape all `<hX>` (where `X` is `1`, `2`, `3`, `4`, or `5`) title elements from the ["Web Scraping" Wikipedia page](https://en.wikipedia.org/wiki/Web_scraping) and export them to CSV. See how to achieve that with:
1. Requests + Beautiful Soup
2. Selenium
3. Scrapy

Let's perform Python web scraping!

### 1. Requests + Beautiful Soup
```python
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
```
You can find the same logic in the `requests-beautifulsoup-scraper.py` file.

### 2. Selenium
```python
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
```
You can find the same logic in the `selenium-scraper.py` file.

### Scrapy
First, initialize a Scrapy project:
```bash
scrapy startproject scrapy_scraping
```
Then, enter the `scrapy_scraping` folder and creat a new Spider called “wikipedia” that targets the desired page:
```bash
cd scrapy_scraping
scrapy genspider wikipedia https://en.wikipedia.org/wiki/Web_scraping
```
A `wikipedia.py` file will appear in the `scrapy_scraping/scrapy_scraping/spiders` folder:
```python
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]

    def parse(self, response):
        pass
```
Implement the scraping logic:
```python
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]

    def parse(self, response):
        # List to store the titles
        titles = []

        # List of header levels (h1, h2, h3, h4, h5)
        title_level_list = [1, 2, 3, 4, 5]

        # Loop through each header level (h1, h2, h3, h4, h5)
        for title_level in title_level_list:
            # Find all elements of the current header level
            title_elements = response.css(f"h{title_level}")

            # Loop through each title element found
            for title_element in title_elements:
                # Extract tag and text
                tag = title_element.root.tag
                text = title_element.css("::text").get().strip()

                # Yield the data directly to the feed
                yield {
                    "tag": tag,
                    "title": text,
                }
```
You can now run the spider to scrape data and export it to a `titles.csv` file with:
```bash
scrapy crawl wikipedia -o titles.csv
```
You can find this Scrapy project in the `scrapy_scraping` folder in the repo.

## Challenges of Python Web Scraping
Web scraping is not always as simple as demonstrated in this repository. Most websites know the value of their data, even if it is publicly accessible on their pages. Thus, they implement several [anti-scraping measures](https://brightdata.com/blog/web-data/anti-scraping-techniques) to prevent scrapers from accessing their pages and extracting data.

Some of the most effective methods include CAPTCHAs, browser fingerprinting, TLS fingerprinting, rate limiting, IP blocking. While it may be possible to bypass these methods with workarounds, it is a cat-and-mouse game where most tricks are temporary and not always reliable.

The solution? Keep reading!

## Simplified Web Scraping With Web Scraper API
[Bright Data's Web Scraper API](https://brightdata.com/products/web-scraper) provides an efficient and scalable solution for extracting structured data from over 100 popular domains, including known e-commerce and social media platforms. The list of supported domains contains of some of the most visited sites worldwide.

With dedicated endpoints, the API offers seamless access to high-quality, compliant data. The key features of this tool include:
- Bulk request handling (up to 5,000 URLs per request).
- Data export to JSON, CSV, and other formats.
- Integration with any programming language and HTTP client tool.
- Unlimited concurrent scraping tasks for faster data collection.
- 99.9% uptime.
- Automatic IP rotation, CAPTCHA solving, and JavaScript rendering to avoid any block.
- Built-in integration with a residential proxy network with over 72 million IPs in 195 countries.

Web Scraper API reduces web scraping in Python (or any other programming language) to a simple API call. Check out the integration guides in the [official documentation](https://docs.brightdata.com/scraping-automation/web-data-apis/web-scraper-api/overview).
