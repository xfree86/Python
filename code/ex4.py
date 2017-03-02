# -*- coding: utf-8 -*-

# 变量的用法

# 汽车总数
cars = 100

# 一辆车的空间
space_in_a_car = 4.0

# 司机总数
drivers = 30

# 乘客总数
passengers = 90

# 闲置的汽车数 等于 汽车总数 - 司机总数
cars_not_driven = cars - drivers

# 被开的汽车数 等于 司机总数
cars_driven = drivers

# 拼车能力 等于 被开的汽车数 乘以 一辆车的空间
carpool_capacity = cars_driven * space_in_a_car

# 平均每辆车上的乘客数 等于 乘客总数 除以 被开的汽车
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print u"这里有", cars, u"辆汽车可用。"

print "There are only", drivers, "drivers available."
print u"这里只有", drivers, u"个司机可用。"

print "There will be", cars_not_driven, "empty cars today."
print u"今天将有", cars_not_driven, u"辆汽车闲置。"

print "We can transport", carpool_capacity, "people today."
print u"今天我们可以运输", carpool_capacity, u"个人。"

print "We have", passengers, "to carpool today."
print u"我们今天有", passengers, u"个乘客拼车。"

print "We need to put about", average_passengers_per_car, "in each car."
print u"我们需要安置大约", average_passengers_per_car, u"个乘客在每辆车上。"