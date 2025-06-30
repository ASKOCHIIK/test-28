class Test:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self):
        return self.name, self.age

class My(Test):
    def __init__(self):
        super().__init__('Abubakir',18)
end = My()
print(end.info())


