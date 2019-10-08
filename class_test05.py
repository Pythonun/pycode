class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA()
obj_b = TestA()#实例属性被重新赋值，不会影响类属性的引用

obj_a.attr = 42#类属性被重新赋值，会影响到类属性的引用
print(obj_b.attr)
print(obj_a.attr)
print(TestA.__dict__)
print(obj_a.__dict__)
