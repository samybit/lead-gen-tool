import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time


def scrape_books(start_url, max_pages=5):
    # max_pages is a safety limit so you don't scrape forever during testing

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
    }

    books_data = []
    current_url = start_url
    pages_scraped = 0

    while current_url and pages_scraped < max_pages:
        print(f"Scraping: {current_url}")  # Debugging print

        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # 1. Extract Data from current page
            articles = soup.find_all("article", class_="product_pod")
            for article in articles:
                title = article.h3.a["title"]
                price = article.find("p", class_="price_color").text
                # Clean currency string
                clean_price = float(price.replace("£", "").replace("Â", ""))

                books_data.append(
                    {"Title": title, "Price": clean_price, "Source URL": current_url}
                )

            # 2. Find the "Next" button
            # On books.toscrape.com, the next button is inside <li class="next"><a href="...">
            next_button = soup.select_one("li.next a")

            if next_button:
                next_page_url = next_button["href"]

                # Handle relative URLs (resolve "catalogue/page-2.html" vs "page-2.html")
                if "catalogue" in next_page_url:
                    current_url = "http://books.toscrape.com/" + next_page_url
                else:
                    # This handles when you are already deep in the catalogue structure
                    base_url = current_url.rsplit("/", 1)[0]
                    current_url = f"{base_url}/{next_page_url}"

                pages_scraped += 1
                time.sleep(1)  # Polite pause (crucial for not getting banned!)
            else:
                current_url = None  # Stop loop

        except Exception as e:
            return None, f"Error on {current_url}: {e}"

    # 3. Export to Excel
    df = pd.DataFrame(books_data)
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    filename = f"books_scraped_{len(books_data)}_items.xlsx"
    filepath = os.path.join("downloads", filename)
    df.to_excel(filepath, index=False)

    return filename, None
