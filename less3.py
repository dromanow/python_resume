class Animal:
    def sound(self):
        print('Animal')


class Cat(Animal):
    def sound(self):
        print('Cat')
        super().sound()


class Dog(Animal):
    def sound(self):
        print('Dog')
        super().sound()


# class CatDog(Cat, Dog):
#     def sound(self):
#         print('CatDog')
#         super().sound()

def sound(self):
    print('CatDog')
    super(CatDog, self).sound()


class Meta(type):
    def __new__(mcs, name, bases, attrs):
        mod = {}

        for key, val in attrs.items():
            mod[key] = val
            mod[key.upper()] = val
        # print(mod)
        return super().__new__(mcs, name, bases, mod)

    def mro(cls):
       return cls, Dog, Cat, Animal, object


class CatDog(Cat, Dog, metaclass=Meta):
    def sound(self):
        print('CatDog')
        super().sound()


class PigHorse(Cat, Dog, metaclass=Meta):
    def sound(self):
        print('PigHorse')
        super().sound()


# CatDog = type('CatDog', (Cat, Dog), {'sound': sound, 'value': 10})
# cat_dog = CatDog()
#
# cat_dog.sound()
# cat_dog.SOUND()

# pig_horse = PigHorse()
# pig_horse.SOUND()

# print(cat_dog.value)
# print(cat_dog.VALUE)


# class Metaclass(type):
#     def mro(cls):
#         return cls, Dog, Cat, Animal, object
#

# CatDog, Cat, Dog, Animal, object
# MRO
#        object
#        Animal
#   Cat          Dog
#        CatDog

# __set__,
#
#
# class Author(db.Model):
#     name = db.CharField(255)
#
#
# author = Author ...
# author.name = 'text' # str

class NonNegative:
    # def __init__(self, name):
    #     self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

# self.value = value


class Order:
    price = NonNegative()
    count = NonNegative()

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def total(self):
        return self.price * self.count


# order = Order('apple', 1, 10)
# order.price = -5
#
# print(order.total())

t = [i for i in range(10)]


def gen():
    for i in range(10):
        val = yield i
        print(i, val)


# gg = gen()
# next(gg)
# next(gg)  # gg.send(None)
# gg.send(10)
# gg.send(30)
# next(gg)


class A:
    def __init__(self):
        self.val = None
        self.i = 0

    def gen(self):
        temp = self.i
        self.i += 1
        return temp

    def send(self, val):
        self.val = val

# zip
# map
# reduce


a = [1, 2, 3]
b = [4, 6]
c = [8, 9, 10, 11]

gg = zip(a, b, c)
# print(next(gg))

# print(list(zip(a, b, c)))

# map/reduce

gg = map(lambda x: x*x, c)

print(next(gg))


# from functools import reduce as functools_reduce
import functools

def reducer(el_prev, el):
    import functools
    print(el_prev, el)
    return el_prev + el


print(reduce(reducer, map(...)))






