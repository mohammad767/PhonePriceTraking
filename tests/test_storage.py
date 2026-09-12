import json
from app.storage import save_products,load_products
from app.models import Product

def test_save_products(tmp_path,old_product) :
    products = [old_product]
    
    file_path = tmp_path / "products.json"
    save_products(products,file_path)
    
    assert file_path.exists()
    
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        
    assert type(data) == list
    assert data[0]["name"] == old_product.name
    assert data[0]["price"] == old_product.price
    

def test_load_products(tmp_path,old_product) :
    products = [old_product]
    file_path =  tmp_path / "products.json"
    
    save_products(products,file_path)
    
    result = load_products(file_path)
    
    assert isinstance(result,list)
    assert len(result) == 1
    assert isinstance(result[0],Product)
    assert result[0].name == old_product.name
    assert result[0].price == old_product.price
    

def test_load_products_file_not_found(tmp_path):
    
    file_path =  tmp_path / "products.json"
    
    result = load_products(file_path)
    
    assert result == []
    
    
    
def test_load_products_invalid_json(tmp_path):

    file_path =  tmp_path / "products.json"
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("{invalid_json}")
            
    result = load_products(file_path)
    assert result == []

def test_load_products_empty_file(tmp_path):
    file_path = tmp_path / "products.json"

    file_path.touch()

    result = load_products(file_path)

    assert result == []