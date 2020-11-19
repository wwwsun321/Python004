.1.类属性与对象属性  


类属性字段在内存中只保存一份
对象属性在每个对象都保存一份。

通过class.__dict__或者实例.__dict__区分属性字段是否为静态字段，在class.__dict__中存在，实例.__dict__中不存在则为静态字段。
class Human(object):              
    staticnum = 1 
    def __init__(self, name):
        self.name = name
上述staticnum为静态字段，内存中存在一份，但name在每个实例中都存在一份。

a = Human("a)
判断对象是否相同：a.__class__()或者id(a) 看内存是否相同

2.类的属性作用域
   a)类添加静态字段：
   方法一：类名.属性=值
   例如:Human.newattr = 1
   
   方法二：
   setattr(cls, 属性，值)，例如：setattr(Human,'newattr',1)
   内置函数不可以
   
   变量下划线区别：
   一个下划线，如：_age 人为不可以修改
   两个下划线，如：__fly  私有属性，python自定定义不可以修改
 
 3.类方法的描述器
   三种方法：
   普通方法：至少一个self参数，表示该方法的对象
   类方法：至少一个cls参数，表示该方法的类
   静态方法：由类调用，无参数
   
   cls.__name__ 获取类的名字
   
  eg:
  class Kls(object):
        bar = 1
        def foo(self):
            print("in foo")
         
        @classmethod
        def class_foo(cls):---这里的cls为调用时类
                print(cls.bar)
                cls().foo()
  调用：Kls.class_foo()----->类名.方法
