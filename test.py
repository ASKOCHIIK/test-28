class Test:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self):
        return self.name, self.age

class  TestPy(Test):
    def __init__(self):
        super().__init__('uluk', 19)

class Person(Test):
       def __init__(self):
           super().__init__("askar", 24)
           
           
class Dog(Test):
    def __init__(self):
        super().__init__("artosh", 3)

class Person(Test):
    def __init__(self):
        super().__init__('Доолот', 22)


class Pers(Test):
    def __init__(self):
        super().__init__('Asan', 23)


class My(Test):
    def __init__(self):
        super().__init__('Abubakir',18)



