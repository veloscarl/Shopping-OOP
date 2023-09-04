class Wheel:
    def __init__(self, size) -> None:
        self.size = size

    def rotate(self, clockwise: bool) -> None:
        print(f"Wheel is rotating {'clockwise' if clockwise else 'counter-clockwise'}")

class Shoppingcart:
    def __init__(self, back_wheel: Wheel):
        self.back_wheel = back_wheel

    def rotate(self, clockwise: bool = True) -> None:
        print(f"Shoppingcart is moving {'forward' if clockwise else 'backward'}")
        self.back_wheel.rotate(clockwise)

class Buyer:
    def __init__(self, name, shoppingcart) -> None:
        self.name = name
        self.shoppingcart = shoppingcart

    def push(self) -> None:
        self.shoppingcart.rotate()

if __name__ == '__main__':
    wheel_front = Wheel(5)
    wheel_back = Wheel(5)
    shopping_cart = Shoppingcart(wheel_back)
    carl = Buyer("Carl", shopping_cart)
    carl.push()