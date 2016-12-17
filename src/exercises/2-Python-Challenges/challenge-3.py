class Person:
    def __init__(self, name, age,study):
        self.name=name
        self.age=age
        self.study=study

    def new_age(self):
        self.age=self.age+1

tobi = Person("Tobi",23,'Computer Science')
brandon = Person("Brendan",25,'Power Engineering')
Person.new_age(tobi)
print(tobi.age)