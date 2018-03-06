class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })
    
    def stock_price(self):
        #total = 0
        #for item in self.items:
        #    total += item['price']
        #return total
        return sum([item['price'] for item in self.items])



my_store = Store("Mediamark")
my_store.add_item("PC",1452.23)
my_store.add_item("cammera",72.23)

print(my_store.items)
print(my_store.stock_price())


