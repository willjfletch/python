class Animal:
    def __init__(self, name: str, species: str, legs: int):
        self.name = name
        self.species = species
        self.legs = legs

    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")
    
    def __str__(self) -> str:
        return f"{self.name} is a {self.species} with {self.legs} legs."