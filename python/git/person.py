class Person:
    name = None
    gender = '男'
    age = 0
    # 私有属性 只能通过方法访问
    __money = 10000

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        pass

    # 动态方法
    def eat(self):
        print("eating")

    def sleep(self):
        print("sellp")

    def running(self):
        print("running")

    def hava_money(self):
        return self.__money

    def get_money(self):
        return self.__money + 100


class Funny(Person):
    skill: str

    # 继承 Person
    # 新增方法fun（）搞笑方法
    def __init__(self, name, gender, age, skill):
        super().__init__(name, gender, age)
        self.skill = skill

    def fun(self):
        print(f"{self.name}""is funy")


class Singer(Person):

    def get_money(self):
        return "1000"


fun1 = Funny("沈腾", "男", "30", "戏剧")
print(fun1.name)
print(fun1.skill)
# fun1.fun()

# singer1 = Singer("周","男","30")
# print(singer1.get_money())
# 实例化一个人，类的
# p1 = Person(name='张三',gender='男',age="20")
# print(p1.name)
# p1.eat()
# print(p1.get_money())
