"""
单例模式实现
"""

class Singleton:
    """
    使用 new 关键字实现单例模式
    多线程时会创建多个实例对象，需要加上线程锁
    """
    _instance=None
    def __new__(cls, *args,**kwargs):
        if not cls._instance:
            cls._instance= super().__new__(cls)
        return cls._instance

def SingletonFunction(cls):
    """
    使用函数装饰器实现单例
    """
    _instance = {} # 对象字典
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    
    return inner

@SingletonFunction
class Cls:
    def __init__(self):
        pass


class SingletonClass:
    """
    使用类装饰器实现单例模式
    """
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@SingletonClass
class Cls2(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    # cls1 = Cls()
    # cls2 = Cls()
    # print(id(cls1))
    # print(id(cls2))
    cls1 = Singleton()
    cls2 = Singleton()
    print(id(cls1) == id(cls2))