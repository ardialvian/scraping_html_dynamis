from playwright.sync_api import sync_playwright
import pandas as pd
import time

user_data_dir = ""
url = ''

def scraping_shopee():
    with sync_playwright() as pw:
        browser = pw.chromium.launch_persistent_context(
            user_data_dir = user_data_dir,
            headless = False,
            args = [
                "--start-maximized",
                "--disable-blink-features=AutomationControlled"
            ]
        )
        page = browser.new_page()
        page.goto(url)

        input("press enter if login has succesfully...")

        page.goto("")
        page.wait_for_timeout(3000)

        for _ in range(15):
            page.mouse.wheel(0,1000)
            time.sleep(2)

        page.wait_for_selector('')
        products = page.query_selector_all('')
        data = []

        for product in products:
            try:
                product_name = product.query_selector('')
                price = product.query_selector('')
                rating = product.query_selector('')
                location = product.query_selector('')

                data.append({
                    'product_name': product_name.inner_text().strip() if product_name else '',
                    'price': price.inner_text().strip() if price else '',
                    'rating': rating.inner_text().strip() if price else 'not rating',
                    'location': location.inner_text().strip() if location else ''
                })

            except Exception as e:
                print(f"pharsing error: {e}")

        df = pd.DataFrame(data)
        df.index += 1
        print(df)

if __name__=="__main__":
    scraping_shopee()