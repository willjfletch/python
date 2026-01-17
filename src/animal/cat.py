from animal.animal import Animal


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name, species="Cat", legs=4)

    def speak(self) -> str:
        return "Meow!"

    def scratch(self, item: str) -> str:
        return f"{self.name} scratched the {item}!"