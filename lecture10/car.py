"""一个可用于表示汽车的类"""


class Car(object):
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_read = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print("This car has " + str(self.odometer_read) + " miles on it.")

    def update_odometer(self, mileage):
        """
            将里程表读数增加增加指定的值
            拒绝将里程表往回拨
        """
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读书增加指定的量"""
        self.odometer_read += miles


class Battery(object):
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.batteyr_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.batteyr_size) + " _kwh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的信息"""
        if self.batteyr_size == 70:
            range = 240
        elif self.batteyr_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
            初始化父类的属性，在初始化电动车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
