from tkinter import *

# Readlines for list of food
food = open("foodList", 'r')
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



def displayFood():
    for i in range(len(foodLst)-1):
        if foodLst[i] == '-':
            items = []
            x = i + 1
            while foodLst[x+1] != '-':
                items.append(str(foodLst[x+1]) + ',')
                x += 1
            area = Label(root, text=foodLst[i+1])
            foodLabel = Label(root, text=items)
            area.pack()
            foodLabel.pack()

def displayMeals():
    for i in range(len(recipesLst)-1):
        if recipesLst[i] == '-':
            ingredients = []
            x = i + 1
            while recipesLst[x] != '-':
                ingredients.append(recipesLst[x+1])
                x += 1
            if all(elem in foodLst for elem in ingredients):
                mtext = "You have the ingredients to cook " + recipesLst[i+1].strip(":") + "!"
                m = Label(root, text=mtext)
                m.pack()
                ingredients.pop()
                rtext = "Ingredients Requred: ", ingredients
                r = Label(root, text=rtext)
                r.pack()


root = Tk()
root.geometry("600x450")
# Title widget for the program
title = Label(root, text="Welcome to the Meal Detector!")
desc = Label(root, text="Start by selecting any of the options below.")
# Buttons
foodBut = Button(root, text="Display Food", command=displayFood)
recipeBut = Button(root, text="Display Recipes",)
mealBut = Button(root, text="Display Meals!", command=displayMeals)

# Layout commands
title.pack()
desc.pack()
foodBut.pack()
recipeBut.pack()
mealBut.pack()

root.mainloop()



