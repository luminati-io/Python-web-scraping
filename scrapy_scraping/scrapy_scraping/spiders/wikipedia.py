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
