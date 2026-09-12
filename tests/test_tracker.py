from app.models import Product
from app.tracker import find_product_by_url,compare_prices,get_price_change



def test_find_product_by_url():
    product = Product(
        name="iPhone 15",
        price=50000000,
        url="https://example.com/iphone",
        source="technolife"
    )

    products = [product]

    result = find_product_by_url(
        products,
        "https://example.com/iphone",
        "technolife"
    )

    assert result == product
    
    
def test_find_product_by_url_not_found():
    products = []

    result = find_product_by_url(
        products,
        "https://example.com/iphone",
        "technolife"
    )

    assert result is None
    
def test_find_product_by_url_different_source():
    product = Product(
        name="iPhone 15",
        price=50000000,
        url="https://example.com/iphone",
        source="technolife"
    )

    result = find_product_by_url(
        [product],
        "https://example.com/iphone",
        "digikala"
    )

    assert result is None
    
def test_compare_prices_increse() :
    old_price = 5000
    new_price = 7000
    
    result = compare_prices(old_price,new_price)
    
    assert result == f"{new_price - old_price}  Price Increased"
    
def test_compare_prices_decrease() :
    old_price = 5000
    new_price = 4000
    
    result = compare_prices(old_price,new_price)
        
    assert result == f"{old_price - new_price} Price Decreased"
    
def test_compare_prices_not_changed() : 
    old_price = 5000
    new_price = 5000
    
    result = compare_prices(old_price,new_price)
    
    assert result == "Price Didn't Change"
    
    
def test_get_price_change_Increased(old_product,new_product_inc) :

    
    result = get_price_change(old_product,new_product_inc)
    
    
    assert result["name"] == new_product_inc.name
    assert result["old_price"] == old_product.price
    assert result["new_price"] == new_product_inc.price
    assert result["change"] == new_product_inc.price - old_product.price
    assert result["url"] ==new_product_inc.url
    assert result["source"] == new_product_inc.source
    assert result["status"] == "Increased"
    assert "timestamp" in result
    
    
    
def test_get_price_change_Decreased(old_product,new_product_dec) :
   
    
    
    result = get_price_change(old_product,new_product_dec)
    
    
    assert result["name"] == new_product_dec.name
    assert result["old_price"] == old_product.price
    assert result["new_price"] == new_product_dec.price
    assert result["change"] == new_product_dec.price - old_product.price
    assert result["url"] == new_product_dec.url
    assert result["source"] == new_product_dec.source
    assert result["status"] == "Decreased"
    assert "timestamp" in result
    
    
def test_get_price_change_Unchanged(old_product,new_product_unc) :
    
    
    
    result = get_price_change(old_product,new_product_unc)
    
    
    assert result["name"] == new_product_unc.name
    assert result["old_price"] == old_product.price
    assert result["new_price"] == new_product_unc.price
    assert result["change"] == new_product_unc.price - old_product.price
    assert result["url"] == new_product_unc.url
    assert result["source"] == new_product_unc.source
    assert result["status"] == "Unchanged"
    assert "timestamp" in result