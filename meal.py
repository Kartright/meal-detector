from tkinter import *
import sys

def openFile(fileName):
    try:
        f = open(fileName, 'r')
        return f
    except FileNotFoundError:
        print("File Not Found")
    except OSError:
        print("OS Error")
        return sys.stdin


def readFile(f):
    file = f.readlines()
    fileLst = []
    for i in range(len(file)):
        fileLst.append(file[i].strip('\n'))
    return fileLst


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
    '''
    Runs when the display food button is pressed.

    Displays food available and then opens an entry box where new food to be
    added can be inserted.
    Two buttons are also displayed, one to put the food entred into the 
    box into the cupboard section adn one for the fridge section.
    '''
    reset()

    food = openFile("foodList")
    foodLst = readFile(food)

    for i in range(len(foodLst)-1):
        if foodLst[i] == '-':
            items = []
            x = i + 1
            while foodLst[x+1] != '-':
                items.append(str(foodLst[x+1]) + ',')
                x += 1
            area = Label(frame, text=foodLst[i+1], font=('arial',15,'bold'))
            foodLabel = Label(frame, text=items)
            area.pack()
            foodLabel.pack()

    foodInput = Entry(frame)
    foodInput.pack()

    def addCupboard():
        '''
        Writes the new food inserted into the entry box into the first line
        after the heading 'Cupboards:' and saves the text file.
        '''
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
        foodInput.delete(0,END)

    def addFridge():
        '''
        Writes the new food inserted into the entry box into the first line
        after the heading 'Fridge:' and saves the text file.
        '''
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
        foodInput.delete(0,END)
    
    addFoodCup = Button(frame, text="Add Food to Cupboard", command=addCupboard)
    addFoodFridge = Button(frame, text="Add Food to Fridge", command=addFridge)
    addFoodCup.pack()
    addFoodFridge.pack()


def displayRecipes():
    '''
    Runs when display recipes button is pressed.

    displays the name of the recipe and the ingredients required to cook it.

    diplays entry box where a new recipe title, and ingredients can be added
    to the recipes list.
    '''
    reset()

    recipes = openFile("recipes")
    recipesLst = readFile(recipes)
    
    for i in range(len(recipesLst)-1):
        if recipesLst[i] == '-':
            items = []
            x = i + 1
            while recipesLst[x+1] != '-':
                items.append(str(recipesLst[x+1]) + ',')
                x += 1
            area = Label(frame, text=recipesLst[i+1], font=('arial',15,'bold'))
            recipesLabel = Label(frame, text=items)
            area.pack()
            recipesLabel.pack()
    
    newRecipe = Entry(frame)
    newRecipe.pack()

    def addRecipe():
        with open('recipes','a') as rp:
            rp.write('\n')
            rp.write(newRecipe.get()+':')
        newRecipe.delete(0,END)

    def addIngredient():
        with open('recipes','a') as rp:
            rp.write('\n')
            rp.write(newRecipe.get())
        newRecipe.delete(0,END)

    def addFinalIngredient():
        with open('recipes','a') as rp:
            rp.write('\n')
            rp.write(newRecipe.get())
            rp.write('\n-')
        newRecipe.delete(0,END)

    addRecipeBut = Button(frame, text='Add New Recipe', command=addRecipe)
    addIngredientBut = Button(frame, text="Add Ingredient", command=addIngredient)
    addFinalIngredientBut = Button(frame, text='Add FINAL Ingredient', command=addFinalIngredient)
    addRecipeBut.pack()
    addIngredientBut.pack()
    addFinalIngredientBut.pack()



def displayMeals():
    '''
    Runs when the display meals button is pressed.

    Compares ingredients required for meals to the ingredients in
    the foodList file. If a they match, it prints a label saying which meal
    can be made, and the two other lables showing which ingredients are requred for the meal.
    '''
    reset()

    recipes = openFile("recipes")
    recipesLst = readFile(recipes)

    food = openFile('foodList')
    foodLst = readFile(food)

    for i in range(len(recipesLst)-1):
        if recipesLst[i] == '-':
            ingredients = []
            x = i + 1
            while recipesLst[x] != '-':
                ingredients.append(recipesLst[x+1])
                x += 1
            if all(elem in foodLst for elem in ingredients):
                mtext = "You have the ingredients to cook " + recipesLst[i+1].strip(":") + "!"
                m = Label(frame, text=mtext, font=('arial',15,'bold'))
                m.pack()
                ingredients.pop()
                q = Label(frame, text="Ingredients Required:")
                r = Label(frame, text=ingredients)
                q.pack()
                r.pack()

def reset():
    global frame

    frame.destroy()
    frame = createFrame(root)
    frame.pack()

def createFrame(root):
    frame = Frame(root)
    # Title widget for the program
    title = Label(frame, text="Welcome to the Meal Detector!")
    desc = Label(frame, text="Start by selecting any of the options below.")
    # Buttons
    foodBut = Button(frame, text="Display Food", command=displayFood)
    recipeBut = Button(frame, text="Display Recipes", command=displayRecipes)
    mealBut = Button(frame, text="Display Meals!", command=displayMeals)

    # Layout commands
    title.pack()
    desc.pack()
    foodBut.pack()
    recipeBut.pack()
    mealBut.pack()

    return frame

root = Tk()

frame = createFrame(root)
frame.pack()

root.mainloop()



