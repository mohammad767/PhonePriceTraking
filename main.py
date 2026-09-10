from app.scraper import (
    technolife_scraper,
    handle_scrape_by_brand,
    handle_digikala_scrape
)

from app.storage import (
    load_products,
    save_products,
    save_price_history,
    load_price_history
)

from app.tracker import (
    find_product_by_url,
    get_price_change
)


def update_prices():
    old_products = load_products()
    new_products = technolife_scraper()

    price_changes = []

    for new_product in new_products:
        old_product = find_product_by_url(
            old_products,
            new_product.url
        )

        if old_product is None:
            print(f"New Product: {new_product.name}")
            continue

        price_change = get_price_change(
            old_product,
            new_product
        )

        price_changes.append(price_change)

    save_price_history(price_changes)
    save_products(new_products)

    print("Prices updated successfully.")


def show_price_history():
    history = load_price_history()
    print(history)


def main():
    while True:
        print("\n===== Price Tracker =====")
        print("1 - Scrape Technolife products")
        print("2 - Update Technolife prices")
        print("3 - Show price history")
        print("4 - Scrape Technolife by filter")
        print("5 - Scrape Digikala products")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            products = technolife_scraper()
            save_products(products)

        elif choice == "2":
            update_prices()

        elif choice == "3":
            show_price_history()

        elif choice == "4":
            products = handle_scrape_by_brand()
            save_products(products)

        elif choice == "5":
            products = handle_digikala_scrape()
            save_products(products)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            

if __name__ == "__main__":
    main()