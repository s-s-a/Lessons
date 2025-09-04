import random

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def total(self):
        return sum(price * quantity for _, price, quantity in self.items)

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def generate_orders(self, count):
        for i in range(count):
            num_items = random.randint(1, 10)
            items = []
            for _ in range(num_items):
                price = random.uniform(5, 500)
                quantity = random.randint(1, 5)
                items.append(("item", price, quantity))
            self.orders.append(Order(i, items))

    def calculate_totals(self):
        return [order.total() for order in self.orders]

def benchmark(n_orders=1_000_000):
    processor = OrderProcessor()
    processor.generate_orders(n_orders)
    return processor.calculate_totals()

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    totals = benchmark()
    print(f"Processed {len(totals)} orders in {time.perf_counter() - start:.2f} sec")
