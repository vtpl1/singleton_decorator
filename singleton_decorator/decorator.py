import threading
import logging

LOGGER = logging.getLogger("root")


class _SingletonWrapper:
    """
    A singleton wrapper class. Its instances would be created
    for each decorated class.
    """    

    def __init__(self, cls):
        self.__wrapped__ = cls
        self.__lock = threading.Lock()
        self._instance = None
        self._instance_dict = None
        self._is_instance_dict = False

        a = dir(cls)
        # print(f"in __init__ {id(self.__lock)}, {self.__wrapped__}")
        if "key" in a:
            self._instance_dict = {}
            self._is_instance_dict = True

    def __call__(self, *args, **kwargs):
        """Returns a single instance of decorated class"""
        with self.__lock:
            # print(f"in __call__ {id(self.__lock), {self.__wrapped__}}")
            if self._is_instance_dict == True:
                temp = self.__wrapped__(*args, **kwargs)
                key = temp.key
                if key in self._instance_dict:
                    temp = self._instance_dict[key]
                else:
                    self._instance_dict[key] = temp
                return temp
            else:
                if self._instance is None:
                    self._instance = self.__wrapped__(*args, **kwargs)
                return self._instance


def singleton(cls):
    """
    A singleton decorator. Returns a wrapper objects. A call on that object
    returns a single instance object of decorated class. Use the __wrapped__
    attribute to access decorated class directly in unit tests
    """
    return _SingletonWrapper(cls)
