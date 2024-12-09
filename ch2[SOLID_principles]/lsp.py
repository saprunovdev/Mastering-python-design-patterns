class Bird:
    def move(self):
        print("I'm moving")

class FlyingBird(Bird):
    def move(self):
        print("I'm flying")

class FlyghtlessBird(Bird):
    def move(self):
        print("I'm walking")

def make_bird_fly(bird):
    bird.move()


if __name__ == "__main__":
    generic_bird = Bird()
    eagle = FlyingBird()
    penguin = FlyghtlessBird()

    make_bird_fly(generic_bird)
    make_bird_fly(eagle)
    make_bird_fly(penguin)