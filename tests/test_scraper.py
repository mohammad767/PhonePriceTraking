import requests
from app.scraper import make_request,parse_products,parse_digikala_products
from app.models import Product

def test_make_request_timeout(monkeypatch):

    def fake_get(*args, **kwargs):
        raise requests.Timeout

    monkeypatch.setattr(requests, "get", fake_get)

    result = make_request("https://example.com")

    assert result is None
    
    
    
def test_make_request_connection_error(monkeypatch) :
    def fake_get(*args,**kwargs) :
        raise requests.ConnectionError
    
    monkeypatch.setattr(requests,"get",fake_get)
    result = make_request("https://example.com")
    
    assert result is None
    
    
def test_make_request_status_code(monkeypatch) :
    class FakeResponse() :
        status_code = 500
        
    def fake_get(*args,**kwargs) :
        return FakeResponse()
    
    monkeypatch.setattr(requests, "get", fake_get)

    result = make_request("https://example.com")

    assert result is None
    
def test_parse_products_success():

    html = """<article><div>
    <h2>iPhone 15</h2>
    <p class="text-[22px]">50,000,000 تومان</p>
    <a href="/product/iphone-15"></a>
</div><div>
    <h2>Samsung Galaxy S24</h2>
    <p class="text-[22px]">60,000,000 تومان</p>
    <a href="/product/galaxy-s24"></a>
</div></article>"""
    class FakeResponse:
        text = html

    result = parse_products(FakeResponse())

    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], Product)

    assert result[0].name == "iPhone 15"
    assert result[0].price == 50000000
    assert result[0].url == "https://www.technolife.com/product/iphone-15"
    
    
def test_parse_products_no_response():

    result = parse_products(None)

    assert result == []
    
def test_parse_products_no_articles():

    html = "<html><body><div>No products</div></body></html>"

    class FakeResponse:
        text = html

    result = parse_products(FakeResponse())

    assert result == []
    
def test_parse_products_missing_name():

    html = """<article><div>
    <p class="text-[22px]">50,000,000 تومان</p>
    <a href="/product/iphone-15"></a>
</div></article>"""

    class FakeResponse:
        text = html

    result = parse_products(FakeResponse())

    assert result == []
    

def test_parse_products_missing_url():

    html = """<article><div>
    <h2>iPhone 15</h2>
    <p class="text-[22px]">50,000,000 تومان</p>
</div></article>"""

    class FakeResponse:
        text = html

    result = parse_products(FakeResponse())

    assert result == []
    
    
def test_parse_products_unavailable_price():

    html = """<article><div>
    <h2>iPhone 15</h2>
    <p class="text-[22px]">ناموجود</p>
    <a href="/product/iphone-15"></a>
</div></article>"""

    class FakeResponse:
        text = html

    result = parse_products(FakeResponse())

    assert len(result) == 1
    assert isinstance(result[0], Product)

    assert result[0].name == "iPhone 15"
    assert result[0].price is None
    assert result[0].url == "https://www.technolife.com/product/iphone-15"
    
    
def test_parse_products_invalid_price():

    html = """<article><div>
    <h2>iPhone 15</h2>
    <p class="text-[22px]">abc تومان</p>
    <a href="/product/iphone-15"></a>
</div></article>"""

    class FakeResponse:
        text = html

    result = parse_products(FakeResponse())

    assert len(result) == 1
    assert result[0].price is None
    


def test_parse_digikala_products_success():

    data = {
        "data": {
            "products": [
                {
                    "title_fa": "iPhone 15",
                    "default_variant": {
                        "price": {
                            "selling_price": 500000000
                        }
                    },
                    "url": {
                        "uri": "/product/123/iphone-15"
                    }
                }
            ]
        }
    }

    result = parse_digikala_products(
        data,
        "https://www.digikala.com"
    )

    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Product)

    assert result[0].name == "iPhone 15"
    assert result[0].price == 500000000
    assert result[0].url == "https://www.digikala.com/product/123/iphone-15"
    assert result[0].source == "digikala"