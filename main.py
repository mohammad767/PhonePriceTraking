from app.scraper import technolife_scraper,technolife_scraper_by_brand,handle_scrape_by_brand
from app.storage import load_products,save_products,save_price_history,load_price_history
from app.tracker import find_product_by_url, track_price,get_price_change

if __name__ == "__main__":
    while True :
        print("1 - Scrape and save products")
        print("2 - Update price")
        print("3 - Track changes")
        print("4 - Scrap and save product by filter")
        print("6 - Exit")
        choice = input("Enter your choice : ")
        
        if choice == "1":
            phone_data = technolife_scraper()
            save_products(phone_data)
        
        elif choice == "2":
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

                result = get_price_change(old_product, new_product)
                price_changes.append(result)
            save_price_history(price_changes)
            save_products(new_products)
        elif choice == "3" :    
            print(load_price_history())
        
        elif choice == "4" :
            handle_scrape_by_brand()
        
        
        elif choice == "6" :
            print("GoodBye")
            break
            
            
        else :
            print("Invalid Choice")
        

            
