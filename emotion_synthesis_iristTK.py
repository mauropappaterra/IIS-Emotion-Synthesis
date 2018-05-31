from random import *

def randomInput():
    """This function generates uniform inputs to emulate the input given by the Machine Learning algorithm"""
    max = 1.0

    #Randomly distribute max probability
    value_1 = round(uniform(0.0, max),8)
    max -= value_1
    value_2 = round(uniform(0.0, max),8)
    max -= value_2
    value_3 = round(uniform(0.0, max),8)
    max -= value_3
    value_4 = round(uniform(0.0, max),8)
    max -= value_4
    value_5 = round(uniform(0.0, max),8)
    max -= value_5
    value_6 = round(max,8)
    probabilities = [value_1,value_2,value_3,value_4,value_5,value_6]
    # FOR TESTING PURPOSES
    #probabilities = [0.17666491, 0.72653016, 0.01022988, 0.01623115, 0.06900918, 0.00133472]

    #Randomly distribute all probabilities among 6 possible emotions
    random_index = randint(0,len(probabilities) - 1)
    ANGER = probabilities.pop(random_index) # ANGER

    random_index = randint(0, len(probabilities) - 1)
    DISGUST = probabilities.pop(random_index) # DISGUST

    random_index = randint(0, len(probabilities) - 1)
    FEAR = probabilities.pop(random_index) # FEAR

    random_index = randint(0, len(probabilities) - 1)
    HAPPY = probabilities.pop(random_index) # HAPPY

    random_index = randint(0, len(probabilities) - 1)
    SADNESS = probabilities.pop(random_index) # SADNESS

    SURPRISE = probabilities[0] # SURPRISE

    input = [ANGER, DISGUST, FEAR, HAPPY, SADNESS, SURPRISE]

    #Print input to screen
    print("RANDOMIZED INPUT\n" + str(input) + "\n" + str(round(sum(input),8)) + "\n")

    return input

def getEmotion (index):
    """Maps the given index on the input array to the corresponding emotion, returns label as string"""
    if (index == 0):
        return "ANGER"
    elif (index == 1):
        return "DISGUST"
    elif (index == 2):
         return "FEAR"
    elif (index == 3):
        return "HAPPY"
    elif (index == 4):
        return "SADNESS"
    elif (index == 5):
        return "SURPRISE"

def getOutput (index):
    """Maps the given index on the input array to the corresponding dialog and emotion to display returned
    as a tuple"""
    if (index == 0): #ANGER

        if (randint(0, 1) == 1):
            return ("That's so scary","fear")
        else:
            return ("I will get you!","anger")

    elif (index == 1): #DISGUST

        if (randint(0, 1) == 1):
            return ("Oh no! That makes me wanna cry!", "sadness")
        else:
            return ("Ewwww! That's gross!", "disgust")

    elif (index == 2): #FEAR
        if (randint(0, 1) == 1):
            return ("That's so scary","fear")
        else:
            return ("Woow, I did not see that coming!", "surprise")

    elif (index == 3 or index == 5): #HAPPINESS OR SURPRISE

        if (randint(0, 1) == 1):
            return ("Yes! I am so glad to hear that!", "happiness")
        else:
            return ("Woow, I did not see that coming!", "surprise")

    elif (index == 4):#SADNESS
        if (randint(0, 1) == 1):
            return ("Oh no! That makes me wanna cry!", "sadness")
        else:
            return ("Woow, I did not see that coming!", "surprise")


def emotionSynthesis (input):
    """This is the main function for the Emotion Synthesis module, given a list containing the probability distribution
    of all the emotions perceived as an input, this function maps out the emotions with the corresponding probabilities
    print out the information on the console and triggers the corresponding reaction from the agent, for the purpose of
    the presentation it will play a video instead. e.g.
    Input: [0.17666491, 0.72653016, 0.01022988, 0.01623115, 0.06900918, 0.00133472]
    Output: Highest Value => 0.72653016 Most Likely Emotion => DISGUST"""

    highest = max(input)  # find highest probability

    for index, probability in enumerate(input):
        print(getEmotion(index) + " => " + str(probability))  # print entire input

        if (probability == highest):
            highest_index = index  # get index

    print("\nHighest Value => " + str(highest))
    print("Most Likely Emotion => " + getEmotion(highest_index))

    output = getOutput(highest_index)
    print("Agent Output =>" + str(output))

    return output

# FOR TESTING PURPOSES
# Uncomment the lines below to generate randomly inputs simulations
"""again = True
while (again):
    random_input = randomInput()
    emotionSynthesis(random_input)

    again = input("\nWant to play the simulation again? y/n\n").lower()
    while (again != 'y' and again != 'n'):
        again = input("Not a valid option. Enter 'y' for yes or 'n' for no!").lower()
    again = (again == 'y')
print("\n-EXIT BY USER-")"""