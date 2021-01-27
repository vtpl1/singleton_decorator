from unittest import TestCase, mock
from typing import Tuple


class Bar(object):
    def __init__(self, weight, width, height):
        self.__weight = weight
        self.__width = width
        self.__height = height

    @property
    def key(self):
        return (self.__weight, self.__width, self.__height)


def get_key(*args, **kwargs) -> Tuple:
    if len(args):
        l = []
        for item in args:
            try:
                l.extend(list(args[0].key))
            except AttributeError as e:
                print("Got Attribute error", e)
                l.append(item)
        return tuple(l)
    if len(kwargs.items()):
        l = []
        for key, value in kwargs.items():
            try:
                l.extend(list(value.key))
            except AttributeError as e:
                print("Got Attribute error", e)
                l.append(value)
        return tuple(l)
    return tuple()


class TestSingletonWrapper(TestCase):
    def setUp(self):
        self.t = t = Bar(1, 2, 3)

    def test_habagoba1(self):

        x1 = get_key(1, 2, 3)
        x2 = get_key(weight=1, width=2, height=3)

        self.assertEqual(x1, x2)
        print(x1, x2)

    def test_habagoba2(self):

        x1 = get_key(1, 2, 3)
        x6 = get_key()
        x2 = get_key(weight=1, width=2, height=3)
        x3 = get_key(self.t)
        x3_1 = get_key(obj=self.t)
        x4 = get_key("000", 0.0, "opn", [1, 2])
        x5 = get_key("000", 0.0, "opn", [1, 2], self.t)

        self.assertEqual(x1, x2)
        self.assertNotEqual(x1, x6)
        self.assertEqual(x1, x3)
        self.assertEqual(x1, x3_1)
        self.assertNotEqual(x1, x4)
        self.assertNotEqual(x1, x5)
        print(x1, x2, x3, x3_1, x4, x5)
