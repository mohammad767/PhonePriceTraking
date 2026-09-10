import requests
from bs4 import BeautifulSoup
from .models import Product
from .utils import clean_price



BASE_URL = "https://www.technolife.com"
MOBILE_URL = f"{BASE_URL}/category/mobile/mobile-phone"

def make_request(url, params=None, headers=None):
    try:
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=20
        )

    except requests.Timeout:
        print(
            "Error: The request timed out while trying "
            "to retrieve the webpage."
        )
        return None

    except requests.ConnectionError:
        print(
            "Error: Connection error occurred while trying "
            "to retrieve the webpage."
        )
        return None

    except requests.RequestException:
        print("Error: Failed to retrieve the webpage.")
        return None

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        return None

    return response


def scrape_products(url, params=None):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
    }

    return make_request(
        url=url,
        params=params,
        headers=headers
    )
    
    
def parse_products(response):
    if not response:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    if not articles:
        print("Error: No articles found on the webpage.")
        return []

    article = articles[0]
    product_list = []

    for phone in article:

        name_tag = phone.find("h2")

        if not name_tag:
            print("Error: Could not find the name tag for a phone.")
            continue

        name = name_tag.get_text(strip=True)

        price_tag = phone.find(
            "p",
            class_="text-[22px]"
        )

        if not price_tag:
            price = None
        else:
            price = price_tag.get_text(strip=True)
            price = clean_price(price)

        url_tag = phone.find("a")

        if not url_tag or not url_tag.get("href"):
            print("Error: Could not find the link for a phone.")
            continue

        url = BASE_URL + url_tag["href"]

        product = Product(
            name=name,
            price=price,
            url=url
        )

        product_list.append(product)

    return product_list

    
    
        

def technolife_scraper():
    choice = input("Do You Want Have Any Filter On Your Search (Y/N): ")

    if choice.lower() == "y":
        return handle_scrape_by_brand()

    response = scrape_products(MOBILE_URL)

    return parse_products(response)

    


def technolife_scraper_by_brand(brand,params=None,series=None):
    if series:
        url = (f"{BASE_URL}/category/mobile/mobile-phone/brand-{brand}/{series}")
    else:
        url = (
            f"{BASE_URL}/category/mobile/mobile-phone/brand-{brand}")

    response = scrape_products(url,params=params)

    return parse_products(response)



def choose_brand():
    brands = [
        "xiaomi",
        "nokia",
        "samsung",
        "honor",
        "apple"
    ]

    while True:
        print(f"Brands: {brands}")

        brand = input("Choose Your Brand: ").lower()

        if brand in brands:
            return brand

        print("Invalid Brand")


def choose_extra_filters():
    params = {}

    add_filters = input(
        "Do You Want More Filters? (Y/N): "
    ).lower()

    if add_filters != "y":
        return params

    min_price = input(
        "Enter The Min Price (blank to skip): "
    )

    if min_price.strip():
        params["pfrom"] = int(min_price)

    ram_map = {
        "8": "195",
        "6": "194",
        "4": "193"
    }

    add_ram = input(
        "Do You Want To Filter RAM? (Y/N): "
    ).lower()

    if add_ram == "y":
        while True:
            ram = input(
                "Enter RAM Amount (8/6/4): "
            )

            if ram in ram_map:
                params["af"] = ram_map[ram]
                break

            print("Invalid Choice")

    return params


def choose_series(brand):
    series_map = {
        "xiaomi": {
            "economy": "type-economy",
            "flagship": "series-flagship",
            "midrange": "series-midrange",
            "gaming": "type-gaming",
        },
        "samsung": {
            "flagship": "series-flagship",
            "midrange": "series-midrange",
            "series-a": "series-a",
            "series-s": "series-s",
        },
    }

    if brand not in series_map:
        return ""

    add_series = input(
        "Do You Want To Choose A Series? (Y/N): "
    ).lower()

    if add_series != "y":
        return ""

    options = series_map[brand]

    while True:
        print(f"Series = {list(options.keys())}")

        pick = input(
            "Enter Your Choice: "
        ).lower()

        if pick in options:
            return options[pick]

        print("Invalid Serie")


def handle_scrape_by_brand():
    brand = choose_brand()
    params = choose_extra_filters()
    series = choose_series(brand)

    products = technolife_scraper_by_brand(
        brand,
        params,
        series
    )

    print(products)

    return products



def parse_digikala_products(data, base_url):
    products_data = data.get(
        "data",
        {}
    ).get(
        "products",
        []
    )

    if not products_data:
        print("Error: No products found in the response.")
        return []

    product_list = []

    for phone in products_data:

        name = phone.get("title_fa") or phone.get("title_en")

        if not name:
            print(
                "Error: Could not find the name for a phone."
            )
            continue

        variant = phone.get("default_variant") or {}

        price_info = variant.get("price") or {}

        price = price_info.get("selling_price")

        if price is None:
            print(
                "Error: Could not find the price for a phone."
            )
            continue

        url_info = phone.get("url") or {}

        uri = url_info.get("uri")

        if not uri:
            print(
                "Error: Could not find the link for a phone."
            )
            continue

        product_url = base_url + uri

        product = Product(
            name=name,
            price=price,
            url=product_url
        )

        product_list.append(product)

    return product_list




def digikala_scraper(
    category="mobile-phone",
    params=None,
    page=1
):
    base_url = "https://www.digikala.com"

    url = (
        f"https://api.digikala.com/v1/categories/"
        f"{category}/search/"
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        ),
        "Accept": "application/json",
    }

    params = dict(params or {})
    params["page"] = page

    response = make_request(
        url=url,
        params=params,
        headers=headers
    )

    if not response:
        return []

    try:
        data = response.json()

    except ValueError:
        print("Error: Response was not valid JSON.")
        return []

    return parse_digikala_products(data, base_url)
    
def choose_digikala_brand():
    brands = ["apple", "samsung", "xiaomi", "nokia", "honor"]
    while True:
        print(f"Brands: {brands}")
        brand = input("Choose Your Brand: ").lower()
        if brand in brands:
            return brand
        print("Invalid Brand")


def choose_digikala_filters():
   
    params = {}

    add_filters = input("Do You Want More Filters? (Y/N): ").lower()
    if add_filters != "y":
        return params

    min_price = input("Enter The Min Price In Toman (blank to skip): ")
    if min_price.strip():
        params["price[min]"] = int(min_price) * 10 

    max_price = input("Enter The Max Price In Toman (blank to skip): ")
    if max_price.strip():
        params["price[max]"] = int(max_price) * 10

    add_ram = input("Do You Want To Filter RAM? (Y/N): ").lower()
    if add_ram == "y":
        ram_map = {"4": "4", "6": "6", "8": "8", "12": "12"}
        while True:
            ram = input("Enter RAM Amount (4/6/8/12): ")
            if ram in ram_map:
                params["ram[]"] = ram_map[ram]
                break
            print("Invalid Choice")

    add_sort = input("Do You Want To Sort Results? (Y/N): ").lower()
    if add_sort == "y":
        sort_map = {
            "cheapest": "4",
            "expensive": "5",
            "newest": "2",
            "popular": "7",
        }
        while True:
            print(f"Sort Options: {list(sort_map.keys())}")
            sort_choice = input("Enter Your Choice: ").lower()
            if sort_choice in sort_map:
                params["sort"] = sort_map[sort_choice]
                break
            print("Invalid Choice")

    return params


def handle_digikala_scrape():
    brand = choose_digikala_brand()
    params = choose_digikala_filters()

    params["brand[]"] = brand

    all_products = []
    page = 1

    while True:

        products = digikala_scraper(
            category="mobile-phone",
            params=params,
            page=page
        )

        if not products:
            break

        all_products.extend(products)

        more_pages = input(
            f"Got {len(products)} products on page {page}. "
            "Fetch next page? (Y/N): "
        ).lower()

        if more_pages != "y":
            break

        page += 1

    return all_products