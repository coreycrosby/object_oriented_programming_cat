class Cat:
    """The Cat's Meow"""
    
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return self.name

    def eats_at(self):
        if (self.meal_time >= 0) and (self.meal_time <= 12):
            return f"{self.meal_time} AM"
        else:
            return f"{self.meal_time - 12} PM"
    
    def meow(self):
        return f"My name is {self.name} and I eat {self.preferred_food} at {self.eats_at()}"

garfield = Cat("garfield", "chicken", 7)
zoey = Cat("zoey", "fish", 23)

print(zoey.meow())
