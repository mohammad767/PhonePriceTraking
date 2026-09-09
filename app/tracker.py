from .storage import load_products
from .models import Product
from datetime import datetime


def compare_prices(old_price, new_price) :
    if old_price < new_price:
        return f"{new_price - old_price}  Price Increased"
    elif old_price > new_price :
         return f"{old_price - new_price} Price Decreased"
    else :
        return "Price Didn't Change"
  
  
  
def find_product_by_url(products: list[Product], url: str) -> Product | None:
    for product in products :
        if product.url == url:
            return product
    return None


def track_price(old_product: Product, new_product: Product):
    return compare_prices(
        old_product.price,
        new_product.price
    )
    
    
def get_price_change(old_product, new_product) :
    change = new_product.price - old_product.price
    timestamp = datetime.now().isoformat()
    if change > 0:
        data = {
            "name" : new_product.name,
            "old_price" : old_product.price,
            "new_price" : new_product.price,
            "change" : change,
            "url" : new_product.url,
            "status" : "Increased",
            "timestamp": timestamp
        }
    elif change < 0:
        data = {
            "name" : new_product.name,
            "old_price" : old_product.price,
            "new_price" : new_product.price,
            "change" : change,
            "url" : new_product.url,
            "status" : "Decreased",
            "timestamp": timestamp
        }
    else :
        data = {
            "name" : new_product.name,
            "old_price" : old_product.price,
            "new_price" : new_product.price,
            "change" : change,
            "url" : new_product.url,
            "status" : "Unchanged",
            "timestamp": timestamp
        }
    return data