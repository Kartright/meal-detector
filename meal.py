from tkinter import *

root = Tk()

# Title widget for the program
title = Label(root, text="Welcome to the Meal Decider!\nAdd your food to the food list and we'll tell you what you can make!")
title.pack()

root.mainloop()

'''
print('*'*20)
print("Welcome to the Meal Decider!\nAdd your food to the food list and we'll tell you what you can make!")
print('*'*20)
'''

# Readlines for list of food
food = open("Food-List", 'r')
x = food.readlines()
food.close

# Readlines for Recipe list
recipes = open("recipes",'r')
y = recipes.readlines()
recipes.close

# Empty lists for appending food a recipes to
foodLst = []
recipesLst = []

# Strips the newline from each list element
for i in range(len(x)):
    foodLst.append(x[i].strip('\n'))
for i in range(len(y)):
    recipesLst.append(y[i].strip('\n'))

def organizeLst(header,section):
    '''
    Takes the header of each food storage location in the food list file and
    the section that it is in.

    This function separates each food storage location into its own individual list
    and returns the list.
    '''
    lst = []
    for i in range(len(foodLst)):
        if foodLst[i] == header:
            for n in range(foodLst.index(header) + 1,foodLst.index('-'*section)):
                lst.append(foodLst[n])
    return lst

for i in range(len(recipesLst)-1):
    if recipesLst[i] == '-':
        ingredients = []
        x = i + 1
        while recipesLst[x] != '-':
            ingredients.append(recipesLst[x+1])
            x += 1
        if all(elem in foodLst for elem in ingredients):
            print('-'*20)
            print("You have the ingredients to cook " + recipesLst[i+1].strip(":") + "!")
            ingredients.pop()
            print("Ingredients Requred: ", ingredients)
            print('-'*20)


