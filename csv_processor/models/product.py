class Product:
    def __init__(self, name, brand, price, rating):
        self.name = name
        self.brand = brand
        self.price = float(price)
        self.rating = float(rating)
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            brand=data['brand'],
            price=data['price'],
            rating=data['rating']
        )
    
    def to_dict(self):
        return {
            'name': self.name,
            'brand': self.brand,
            'price': self.price,
            'rating': self.rating
        }