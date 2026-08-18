class Animal:
    def eat(self):
        pass

    def move(self):
        print("двигается")

class Swimming(Animal):
    def sleep(self):
        print("Спит")

    # def move(self):
    #     print("плавает")

class Flying(Animal):
    def feed_baby_bird(self):
        print("кормит птенца")

    # def move(self):
    #     print("летает")

class Duck(Flying, Swimming):
    def move(self):
        print("плавает и летает")
        super().move()

donald_duck = Duck()
print(Duck.__mro__) # method resolution order - порядок поиска методов
donald_duck.move()
donald_duck.eat()
donald_duck.sleep()
donald_duck.feed_baby_bird()