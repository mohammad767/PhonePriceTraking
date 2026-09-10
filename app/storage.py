import json
from .models import Product
import pprint 
pp = pprint.PrettyPrinter(indent=4)



def save_products(products):
    product_list = []

    for product in products:
        product_list.append(product.to_dict())

    with open("data/products.json", "w", encoding="utf-8") as file:
        json.dump(
            product_list,
            file,
            indent=4,
            ensure_ascii=False
        )

    return "Products saved successfully."

            
def load_products() : 
    product_list = []
    try : 
        with open("data/products.json","r", encoding="utf-8") as file : 
            content = file.read()

            if content:
                product_dict_list = json.loads(content)
                for product_dict in product_dict_list :
                    product = Product.from_dict(product_dict)
                    product_list.append(product)
                return product_list
            else : 
                print("File Is Empty!")
                return []
    
    except FileNotFoundError :
        print("File Name Is Not Correct!")
        return []
    
    except json.JSONDecodeError :     
        print("Can Not Read The File!")
        return []
    
    
        
def save_price_history(price_changes):
    history = []

    try:
        with open("data/price_history.json", "r", encoding="utf-8") as file:
            history = json.load(file)

    except FileNotFoundError:
        history = []

    except json.JSONDecodeError:
        history = []

    history.extend(price_changes)

    with open("data/price_history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)

    return "Price history saved."

def load_price_history():
    try:
        with open("data/price_history.json", "r", encoding="utf-8") as file:
            # history = json.load(file)
            # return pp.pprint(history)
        
        
            content = file.read()
        
            if content:
                history = json.loads(content)
                return pp.pprint(history)
            else : 
                print("File Is Empty!")
                return []
    except FileNotFoundError:
        print("Price history file not found.")
        return []
    except json.JSONDecodeError:
        print("Error reading price history file.")
        return []
    
        
# print(load_products())
# products = [
#     Product("iPhone 14", 50000000, "https://example.com/iphone"),
#     Product("Samsung S24", 60000000, "https://example.com/s24")
# ]

# save_products(products)