# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates okay
# set = {} unordered and immutable, but Add/Remove okay. NO duplicates
# tuple = () ordered amd unchangeable. Duplicates okay. Faster 

# fruit = "apple"
# print(fruit)

# fruits = {"apple", "orange", "banana", "coconut", "strawberry"}
# print(fruits)
# # print(dir(fruits))
# # print(help(fruits))
# # print(len(fruits)) # --> how many total values are in list
# # # fruits[0]= "pineapple" --> reassigns values 
# # # fruits.append("pineapple")--> adds a value to the list 
# # # fruits.remove("apple") --> removes a value from your list
# # # fruits.insert(0, "pineapple") --> inserts value at certain place
# # # fruits. sort() --> sorts your lists
# # # fruits.reverse() --> reverses your values
# # # fruits.clear() --> clears your values 

# fruits = ("apple", "orange", "banana", "coconut", "strawberry")
# print(fruits)
# # print(dir(fruits))
# # print(help(fruits))
# # print(len(fruits)) # --> how many total values are in list
# # print("pineapple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)
# for fruits in fruits:
#     print(fruits)
    

#dictionaries
#dictionary= a collection of {key:value} pairs    
                    # ordered and changeable. no duplicates
    
capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}


# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

# if capitals.get("USA"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) #adds value to dictionary
capitals.update({"Thailand":"Bangkok"}) #adds value to dictionary
capitals.update({"USA":"Detroit"}) #changes the value of a key
capitals.pop("China") #takes out the value
capitals.popitem()
capitals.clear() #clears your dictionary
keys= capitals.keys() 
for key in capitals.keys():
    print(key)

values = capitals.values()
for values in capitals.values():
    print(values)
    

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")
print(items)


# print(fruits[0])
# # # for ftuit in fruits:
# # # print(fruit)


# # cars= ["bmw", "maseratri", "audi","mercedes", "ferrari"]
# # print(f"these are lists of {cars}")
# # print(f"the first car is {cars[0]}")

# # cars[0] = "toyota"
# # print(f"the first car is {cars[0]}")

# # print(f"the last car is {cars[-1]}")
# # cars[-1]= "lamborghini"
# # print(f"the last car is {cars[-1]}")

# # #adding a new value to the list
# # cars.append("bugatti")
# # print(cars)
# # cars.remove("maseratri")
# # print(cars)

# # looping through the list
# # otherwise called iterating the list
# # for car in cars:
# #  # print(len(car))
# #  # print(car)
# #     carRequest= input("add a new car please:")
# #     cars.append(carRequest)
# #     print(cars)
# #     print(len(cars))
# #     print(cars)
# #     if len(cars) > 10:
# #         break

# #challenge
# # create a list of friends
#     # make sure the initial list is none
# friends=[]
#     # add a new friend to the list, add at least 5 friends
#     # remove a friends
#     # insert a friend at a specific index
#     # loop through the list and print the friends name
#     # see if a particular friend is in the list (boolean value)
#     # if the list is greater than 10 break the loop




# friends= ["loop", "loopsy", "lizzy", "sarahera", "jeanetty"]
# print(friends)
# addFriends= input("add some new friends please:")
# friends.append(addFriends) 
# print(friends)
# addFriends= input("add some new friends please:")
# friends.append(addFriends) 
# print(friends)
# addFriends= input("add some new friends please:")
# friends.append(addFriends) 
# print(friends)
# addFriends= input("add some new friends please:")
# friends.append(addFriends) 
# print(friends)
# addFriends= input("add some new friends please:")
# friends.append(addFriends) 
# print(friends)

# friends.remove("loopsy")
# print(friends)
# friends.insert(3, "lizziebeth")
# print(friends)

# print("sarah" in friends)
# print(friends)




