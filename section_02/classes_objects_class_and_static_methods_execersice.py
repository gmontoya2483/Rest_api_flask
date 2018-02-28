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
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        new_store = cls("{} - franchise".format(store.name))
        return new_store 

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return  "{}, total stock price: {}".format(store.name, store.stock_price())

        

store_1 = Store("Amazon")
store_2 = Store.franchise(store_1)
store_2.add_item("blaBla",124.12)
store_2.add_item("Headset",45.23)

print(store_2.name)
print(store_2.items)
print(Store.store_details(store_2))

