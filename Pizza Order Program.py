#Arsh Suri
#To use this program just run it and answer the prompts

#declares a function with takes an order for a single pizza
def askOrder(numPizza):
    #checks if a pizza has been ordered to avoid saying the intro line again
    if numPizza < 1:
        print("Hello welcome to Taco Palace, where we only serve the finest tacos, I'll be taking your order today.")

    #A loop for the entire ordering process
    while True:
        #asking size of pizza, doesn't require a loop because it is at the top of the function
        sizePizza = input("What size pizza were you wanting? We have large, medium, and small pizzas. ")
        #cleaning the input to ensure the user is saying it is large, medium, or small
        if sizePizza == "large" or sizePizza == "medium" or sizePizza == "small":
            pass
        else:
            print("We only have large, medium, or small pizzas.")
            continue

        #A loop for handling the user ordering toppings
        while True:
            #tries to set a topping variable and tries to int() that input to ensure it is an actual integer
            try:
                numTopping = int(input("How many toppings did you want on that " + sizePizza + " pizza? "))
                #cleaning the input to ensure that a user can't have negative or decimal toppings
                if type(numTopping) != float:
                    if numTopping >= 0:
                        break
                else:
                    print("Make sure to tupe the proper number of toppings")
            except:
                print("Make sure to type the number of toppings.")
                continue

        #A looping for asking the user if the pizza is correct
        while True:
            pizzaCorrect = input("So a " + sizePizza + " pizza with " + str(numTopping) + " toppings, correct? [Answer with Yes or No] ")
            #Cleaning the input to ensure the user typed yes or no
            if pizzaCorrect == "Yes" or pizzaCorrect == "No":
                break
            else:
                print("[Make sure to type Yes or No.]")
        if pizzaCorrect == "Yes":
            break
        elif pizzaCorrect == "No":
            continue

    #returning the values from the order
    return [sizePizza, numTopping]


def calcPrice(size, topping, pizzaSum, endSum, numPizza):

    #A section of code handling the "end" of the order meaning tax and delivery, allows for the function to be multipurpose in doing regular price calculations and the end calculations
    if endSum == True:

        #calculate the tax
        tax = pizzaSum*0.06
        #setting the total sum with the incorporated tax
        totalSum = tax + pizzaSum

        #A loop for handling the tip for the order
        while True:
            #tries to see if tip is a integer and ensures it can't be negative, using float() in case of non whole tips
            try:
                tip = float(input("How much did you want to tip? "))
                if tip >= 0:
                    totalSum += tip
                    break
                else:
                    print("Make sure to type the amount of tip ")
                    continue
            except:
                print("Make sure to type the amount of tip ")
                continue

        #A loop for handling the delivery and its price
        while True:
            #cleans the input for to ensure the user only inputs yes or no when being prompted with the delivery
            delivery = input("Did you want to deliver? [Answer with Yes or No] ")
            if delivery == "Yes":
                totalSum += 5
                break
            elif delivery == "No":
                break
            else:
                continue

        #A section of the code devoted to ensuring that the final message with the total amount of pizzas using correct nouns. Ex: "You have ordered 1 pizzas" is now converted into "You have ordered 1 pizza"
        if numPizza > 1:
            plural = "s"
        else:
            plural = ""

        #Prints the summary of the order after a new line
        print("\n")
        print("You have ordered " + str(numPizza) + " pizza" + plural)
        print("Pizza Cost: $" + str(pizzaSum) )
        print("Amount of Tax: $" + str(tax))

        #Checking the delivery variable again so the print statement goes with the rest of the order summary
        if delivery == "Yes":
            print("Delivery Charge: $5")

        print("Tip Charge: $" + str(tip))
        print("Total Amount Due: $" + str(totalSum))
        print("Thank you. Have a nice day.")

    #A section of the code devoted to regular pizza price calculations, is calculated per pizza
    #Section with checks the price depending on the size of the pizza, doesn't need to check for bad inputs because input is already cleaned
    if size == "large":
        pizzaSum += 10
    elif size == "medium":
        pizzaSum += 8
    elif size == "small":
        pizzaSum += 6

    #Section determines added price depending on toppings
    if topping == 0:
        pass
    elif 1 <= topping <= 3:
        pizzaSum += topping*1.5
    elif topping >= 4:
        pizzaSum += topping*1

    #A debugging statement to ensure that the indivual pizza price is correct and the total pizza sum is correct
    #print(pizzaSum)
    #retuns the sum of all the pizzas so far
    return pizzaSum


#sets the currentsum to 0 to keep the calcPrice() additive
currentSum = 0

#Sets the number of ordered pizzas to 0
orderedPizza = 0

#A loop for handling the rest of actual calculations for the order
while True:
    #sets a list as the output for the askOrder()
    order = askOrder(orderedPizza)
    #Sets the currentSum to the output of the calcPrice() function so the function knows the last price value
    currentSum = calcPrice(order[0], order[1],currentSum, False, orderedPizza)

    #Increases the number of pizzas ordered by 1
    orderedPizza += 1

    #Aks the user if they want to order another pizza
    while True:
        #cleans the input when asking if the user wants to order another pizza
        anotherPizza = input("Did you want to order another pizza? [Answer with Yes or No] ")
        if anotherPizza == "Yes" or anotherPizza == "No":
            break
        else:
            continue

    if anotherPizza == "Yes":
        continue
    else:
        break
#running calcPrice() for the final price calcualtions
currentSum += calcPrice(order[0], order[1], currentSum, True, orderedPizza)







