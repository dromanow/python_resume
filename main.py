
# a = [1, 2, 3]
# a1 = 1
#
#
# m = {
#     1: lambda a: a*2,
#     2: lambda a: a/3
# }
#
# print(m[1](1))
#
# if a1 == 1:
#     print(1)
# elif len(a) == 3:
#     print(4)
# else:
#     print(2)


# from typing import Final
#
# a: Final = [1, 2, 3, 4]
#
#
# class A:
#     a = 1
#
#     def __init__(self):
#         self.a = 1
#
#
# def f():
#     a = 10
#
#     def f1():
#         # nonlocal a
#         a = 1
#     print(a)
#     f1()
#     print(a)
#
#
# f()

# print('test' + str(10) + str(112) + 'qwerty')
#
# print(f'{10} {a} {a1}')

class A:
    def __init__(self, a):
        self._a = a
        self.b = False

    a = property()

    @a.setter
    def a(self, val):
        self._a = val
        self.b = True

    @a.getter
    def a(self):
        return self._a + 1

    @staticmethod
    def fabric(a):
        return A(a)

    @classmethod
    def test(cls):
        print(type(cls))


a = A(1)
a.a = 20
print(a.a)


a.raw_test = lambda a: a*2

print(a.raw_test(1))
# a.b = True



# class B:
#     def __init__(self, a):
#         self.a = a
#
#
# def test_1():
#     print('test1')
#
#
# # A.test = test_1
#
# a = A(1)
# b = B(1)
# # a.a = 20
#
# # A.test(b)
# # getattr(A, 'test')(a)
#
# temp = a
#
# # if hasattr(temp, 'test'):
# #     temp.test()
#
# a.a = 20
# setattr(a, 'a', 20)
#
# a1 = A.fabric(10)
#
# # print(type(a1))
#
# a1.test()


class Animal:
    def sound(self):
        print('Animal')


class Cat(Animal):
    def sound(self):
        print('Cat')
        super().sound()
    # pass


class Dog(Animal):
    def sound(self):
        print('Dog')
        super().sound()


class Meta(type):
    def mro(cls):
        return (cls, Dog, Cat, Animal)

    def __new__(cls, *args, **kwargs):
        return CatDog()


class CatDog(Cat, Dog):
    def sound(self):
        print('CatDog')
        super().sound()

# CatDog, Cat, Dog, Animal

# MRO

def f(a):
    a.sound()



# animal = Animal()
f(Cat())
print('<<<<<<')
# cd = CatDog()
# cd.__mro__ = (CatDog, Dog, Cat, Animal)
f(CatDog())
# f(Dog())
# del animal
# f(Dog())
