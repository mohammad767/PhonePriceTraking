import pytest
from app.models import Product



@pytest.fixture
def old_product() :
    return Product(
        name="iPhone 15",
        price=50000000,
        url="https://example.com/iphone",
        source="technolife"
    )

@pytest.fixture
def new_product_inc() :
    return Product(
            name="iPhone 15",
            price=70000000,
            url="https://example.com/iphone",
            source="technolife"
        )    
    


@pytest.fixture
def new_product_dec() :
    return Product(
            name="iPhone 15",
            price=40000000,
            url="https://example.com/iphone",
            source="technolife"
        )    
    
@pytest.fixture
def new_product_unc() :
    return Product(
            name="iPhone 15",
            price=50000000,
            url="https://example.com/iphone",
            source="technolife"
        )    
    



    


