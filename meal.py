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
    food = open("foodList", 'r')
    x = food.readlines()
    food.close

    foodLst = []

    for i in range(len(x)):
        foodLst.append(x[i].strip('\n'))

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

    foodInput = Entry()
    foodInput.pack()

    def addCupboard():
        with open('foodList', 'r+') as food:
            contents = food.readlines()
            if "Cupboards:" in contents[-1]:  # Handle last line to prevent IndexError
                contents.append(foodInput.get() + "\n")
            else:
                for index, line in enumerate(contents):
                    if "Cupboards:" in line and foodInput.get() not in contents[index + 1]:
                        contents.insert(index + 1, foodInput.get() + "\n")
                        break
            food.seek(0)
            food.writelines(contents)
    
    def addFridge():
        with open('foodList', 'r+') as food:
            contents = food.readlines()
            if "Fridge:" in contents[-1]:  # Handle last line to prevent IndexError
                contents.append(foodInput.get() + "\n")
            else:
                for index, line in enumerate(contents):
                    if "Fridge:" in line and foodInput.get() not in contents[index + 1]:
                        contents.insert(index + 1, foodInput.get() + "\n")
                        break
            food.seek(0)
            food.writelines(contents)

    
    addFoodCup = Button(root, text="Add Food to Cupboard", command=addCupboard)
    addFoodFridge = Button(root, text="Add Food to Fridge", command=addFridge)
    addFoodCup.pack()
    addFoodFridge.pack()

    



def displayMeals():
    recipes = open("recipes",'r')
    y = recipes.readlines()
    recipes.close

    recipesLst = []

    for i in range(len(y)):
        recipesLst.append(y[i].strip('\n'))

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
                q = Label(root, text="Ingredients Required:")
                r = Label(root, text=ingredients)
                q.pack()
                r.pack()


root = Tk()

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



