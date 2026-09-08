from dataclasses import dataclass
import json


@dataclass
class Product:
    name: str
    price: int
    url: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            price=data.get("price"),
            url=data.get("url")
        )

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "url": self.url
        }

    def save_to_json(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def from_json(cls, filename):
        product_list = []

        with open(filename, "r") as file:
            data = json.load(file)

        for product in data:
            product_obj = cls.from_dict(product)
            product_list.append(product_obj)

        return product_list
        
               


# products_list = [
#     {
#         "name": "iPhone 14",
#         "price": 50000000,
#         "url": "https://example.com/iphone"
#     },
#     {
#         "name": "Samsung S24",
#         "url": "https://example.com/s24"
#     },
#     {
#         "name": "Samsung S22",
#         "price": None,
#         "url": "https://example.com/s24"
#     }
# ]

# product_obj_list = []

# for product in products_list : 
#     product_obj = Product.from_dict(product)
#     product_obj_list.append(product_obj)
    
# product_dict_list = []

# for product in product_obj_list : 
#     product_dict = product.to_dict()
#     product_dict_list.append(product_dict)
    



# phone_list = Product.from_json("product")
# print(phone_list)