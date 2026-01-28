import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import time


def scrape_books(start_url, max_pages=5):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
    }

    books_data = []
    current_url = start_url
    pages_scraped = 0

    while current_url and pages_scraped < max_pages:
        print(f"Scraping: {current_url}")

        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # 1. Extract Data
            articles = soup.find_all("article", class_="product_pod")
            for article in articles:
                title = article.h3.a["title"]
                price = article.find("p", class_="price_color").text
                clean_price = float(price.replace("£", "").replace("Â", ""))

                books_data.append(
                    {"Title": title, "Price": clean_price, "Source URL": current_url}
                )

            # 2. Pagination Logic
            next_button = soup.select_one("li.next a")
            if next_button:
                next_page_url = next_button["href"]
                if "catalogue" in next_page_url:
                    current_url = "http://books.toscrape.com/" + next_page_url
                else:
                    base_url = current_url.rsplit("/", 1)[0]
                    current_url = f"{base_url}/{next_page_url}"

                pages_scraped += 1
                time.sleep(1)
            else:
                current_url = None

        except Exception as e:
            return None, f"Error on {current_url}: {e}"

    # 3. Export to Memory (Cloud-Ready Refactor)
    df = pd.DataFrame(books_data)

    output = io.BytesIO()
    # Use the 'openpyxl' engine which is compatible with Excel files
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    # Reset cursor to start of file
    output.seek(0)

    # Return the file object directly, not a filename
    return output, None
