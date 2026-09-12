from dataclasses import dataclass



@dataclass
class Product:
    name: str
    price: int | None
    url: str
    source: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            price=data.get("price"),
            url=data.get("url"),
            source=data.get("source")
        )

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "url": self.url,
            "source" : self.source
        }

   
        
               


