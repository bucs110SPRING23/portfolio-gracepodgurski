import random #Part B
example = random.randint(1,10)

my_list = [8, 12.0, "txt","brb","gtg"]
updated_list = random.choice(my_list)
print(my_list)
print(updated_list)

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition/classes)/weeks)
print("Cost per week:",cost_per_week)

classes_per_week = 3
cost_per_class = cost_per_week/classes_per_week

print(weeks,type(weeks))
print(classes,type(classes))
print(tuition,type(tuition))
print(cost_per_week,type(cost_per_week))
print(classes_per_week,type(classes_per_week))
print(cost_per_class,type(cost_per_class))


