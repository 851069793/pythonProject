class Animal:
    def __init__(self, name, age, sex, legNum, weight):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__legNum = legNum
        self.__weight = weight

    def eating(self, food):
        print("The animal 's food is"+food)

    def __str__(self) -> str:
        return "名字：{}\t年龄：{}\t性别：{}\t腿的数目：{}\t重量：{}".format(self.__name,self.__age,self.__sex,self.__legNum,
                                                            self.__weight)


class Pig(Animal):
    def __init__(self, name, age, sex, legNum, weight, length, height, color):
        super().__init__(name, age, sex, legNum, weight)
        self.__length = length
        self.__height = height
        self.__color = color

    def eating(self, food):
        print("Pig is eating", food)

    def walking(self):
        print("Pig can walk")

    def __str__(self) -> str:
        return super(Pig, self).__str__() + "\t身长：{}\t身高：{\t颜色：{}".format(self.__length,self.__height,self.__color)


class Chicken(Animal):
    def __init__(self, name, age, sex, legNum, weight, combColor):
        super().__init__(name, age, sex, legNum, weight)
        self.combColor = combColor

    def eating(self, food):
        print("The chicken is eating", food, "use the mouth")

    def flying(self):
        print("Chicken can fly")

    def __str__(self) -> str:
        return super(Chicken, self).__str__() + "\t鸡冠颜色：{}".format(self.combColor)