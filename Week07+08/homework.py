from abc import ABCMeta, abstractclassmethod

#不允许被实例化。定义为抽象基类
class animail(metaclass=ABCMeta): 
    @abstractclassmethod
    def kind(self):
        pass

    @abstractclassmethod
    def size(self):
        pass

    @abstractclassmethod
    def disposition(self):
        pass
    @abstractclassmethod
    def is_feroc(self):
        pass
    
 
class someanimal(animail):
    def __init__(self, kind, size, disposition):
        self._kind = kind
        self._size = size
        self._disposition = disposition
        self._is_feroc = self.is_feroc()

    @property
    def kind(self):
        return self._kind
    
    @property
    def size(self):
        return self._size
    
    @property
    def disposition(self):
        return self._disposition
        
    def is_feroc(self):
        num = someanimal.get_size(self._size)
        if num >=2 and self._kind == "食肉" and self._disposition == "凶猛":
            return True
        else:
            return False

    @staticmethod
    def get_size(p_size):
        if p_size == "小":
            return 1
        elif p_size == "中":
            return 2
        elif p_size == "大":
            return 3
        else:
            return 0

class cat(someanimal):
    sound = "喵喵！"

    def __init__(self, name, kind, size, disposition):
        super().__init__(kind=kind, size=size, disposition=disposition)
        self.name = name
        self.is_pet = not self._is_feroc


class dog(someanimal):
    sound = "汪汪！"

    def __init__(self, name, kind, size, disposition):
        super().__init__(kind=kind, size=size, disposition=disposition)
        self.name = name
        self.is_pet = not self._is_feroc


class zoo(object):
    def __init__(self,name):
        self.name = name

    @classmethod
    def add_animal(self, ani):
        ani_name = type(ani).__name__
        if ani_name not in zoo.__dict__:
            #类添加静态字段
            setattr(zoo,ani_name,ani)


if __name__ == "__main__":
    cat1 = cat('大花猫 1', '食肉', '大', '温顺')
    print(cat1.sound)     
    print(cat1.is_pet)

    z = zoo('时间动物园')
    z.add_animal(cat1)
    cat2 = cat('大花猫 1', '食肉', '大', '温顺')
    z.add_animal(cat2)
    dog1 = dog('小黑狗 1', '食肉', '大', '凶猛')
    z.add_animal(dog1)
    print(zoo.__dict__)
    print(hasattr(z,'cat'))
    print(hasattr(z,'dog'))
    print(hasattr(z,'chicken'))
"""
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

复制代码
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
具体要求：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
"""
