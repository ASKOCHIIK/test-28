class Test:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self):
        return self.name, self.age


class Person(Test):
    def __init__(self):
        super().__init__('Доолот', 22)


class Pers(Test):
    def __init__(self):
        super().__init__('Asan', 23)


p = Person()
a = Pers()
print(p.info())
print(a.info())
