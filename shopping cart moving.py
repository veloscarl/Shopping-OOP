class Wheel:
    def __init__(self, size) -> None:
        self.size = size

    def rotate(self, clockwise: bool) -> None:
        print(f"Wheel is rotating {'clockwise' if clockwise else 'counter-clockwise'}")

class basketcart:
    def __init__(self, back_wheel: Wheel):
        self.back_wheel = back_wheel

    def rotate(self, clockwise: bool = True) -> None:
        print(f"Shoppingcart is moving {'forward' if clockwise else 'backward'}")
        self.back_wheel.rotate(clockwise)

class Buyer:
    def __init__(self, name, basketcart) -> None:
        self.name = name
        self.basketcart = basketcart

    def push(self) -> None:
        self.basketcart.rotate()

if __name__ == '__main__':
    wheel_front = Wheel(5)
    wheel_back = Wheel(5)
    basket_cart = basketcart(wheel_back)
    carl = Buyer("Carl", basket_cart)
    carl.push()
      

class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class basketcart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def compute_total(self):
        total = 0
        for item, quantity in self.items:
            total += item.price * quantity
        return total

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = basketcart()

    def buy_item(self,item, quantity=1):
        self.cart.add_item(item, quantity)
        print(f"{self.name} added {quantity} {item.name}(s) to the cart.")

    def checkout(self):
        total = self.cart.compute_total()
        print(f"{self.name}'s total Price: P{total:.2f}")
        return total

if __name__ == '__main__':
    
    item1 = item("shampoo", 120)
    item2 = item("bear brand", 350)
    item3 = item("rexona", 50)
    item4 = item("toothpaste", 15)

    customer = Customer("carl")

    customer.buy_item(item1, 8)
    customer.buy_item(item2, 5)
    customer.buy_item(item3, 10)
    customer.buy_item(item4, 10)

    total_cost = customer.checkout()
    print(f"{customer.name} paid P{total_cost:.2f} for their purchases.")
