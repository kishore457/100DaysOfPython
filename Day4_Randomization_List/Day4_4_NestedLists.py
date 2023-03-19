# dirty_dozen = ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries","Pears","Spinach",
#                "Kale", "Tomatoes", "Celery", "Potatoes"]

fruits = ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries","Pears"]
vegetables = ["Spinach","Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

print("dirty_dozen - 0 " + str(dirty_dozen[0]))
print("dirty_dozen - 1 " + str(dirty_dozen[1]))

print("dirty_dozen 0 - 1 " + str(dirty_dozen[0][1]))
print("dirty_dozen 1 - 1 " + str(dirty_dozen[1][1]))

