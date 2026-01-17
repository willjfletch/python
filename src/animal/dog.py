from animal.animal import Animal


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, species="Dog", legs=4)

    def speak(self) -> str:
        return "Woof!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetched the {item}!"