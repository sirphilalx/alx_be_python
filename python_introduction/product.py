class Product:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
    def totalQuantity(self):
        return(f'Total quantity of {self.name} is {self.quantity}')

basket = Product('basket', 'basket description', 100)
# basket.totalQuantity()
print(basket.totalQuantity())
