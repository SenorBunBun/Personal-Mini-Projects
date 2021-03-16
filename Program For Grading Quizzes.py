#Defining a function to take the teacher's key for future use\



def key():
    #Setting a global variable that stores the user's # of questions so the variable is accessible and changes are saved throughout the function even if in a loop.
    global usernumquestions
    print("To initialize the program we will need to set the key for all the student quizzes.")

    #Asking the # of questions as it determines how many answers that need to be graded and need to have a key. Converting this to a integer so it can be used to access list elements directly.
    #A while loop is used  to ensure the quiz has more than 5 questions.

    while True:
        usernumquestions = int(input("How many questions are there? (answer with a #) :"))

        #A if statement checking to make sure the # of questions is at least 5 so the quiz is long enough.
        if usernumquestions >= 5:
            break
        else:
            print("Hey a quiz with less than 5 questions, Might as well make that a homework assignment. Make sure you have 5 questions or more. ")
    userkey = []

    #A for loop setting the key for all the quizzes in this session. Using the # of Questions from the lines above we can determine how many times we need to ask the key and the question number for each question.
    #The for loop uses the range() as it easily gives all the numbers from 0 to the desired number.
    #Using the empty list defined before I add the key answer to the list to act as the key for all quizzes and allowing for the key's answers to be accessed quiockly.
    for key in range(usernumquestions):
        userkey.append(input("What is the answer for Question #" + str(key+1) + " [It can be alphanumerical]: "))

    #Returning both the userkey and usernumquestions in a list so the function can be run and both values can be stored
    return [userkey, usernumquestions]


#Defining a function for grading of each indivual test. It takes in the key for determining correct answers, the number of questions for determining how many answers the student needs to give, and the studentnumber for easy organization of which student is getting graded.
def grading(testkey, numquestions, studentnum):

    #This string was being heavily utilized to refer to the student's answers so a variable was set for simplified use
    studentname = "Student " + str(studentnum)

    #Setting an temporary empty list for the student answers as this will change for each student and isn't needed for all features implemented so far.
    print("We will now grade " + studentname + " : ")
    tempstudentanswers = []

    #Setting a for loop to ask what the student's answers was. range() was used as it gives all the numbers from 0 to the number of questions for easy question referencing.
    for answers in range(numquestions):

        #Conditional statement asking the student's answer for the question # and adding a 1 to the student answers list if it equal to the key's answer in the same question.
        #Apeending of the integer 1 basically functions as a "correct" signal for grade point scoring. It appends a 0 as a "incorrect" signal in the list. This allows for the 0's and 1's to be counted for the grade.
        if input("What was " + studentname + "'s answer for Question #" + str(answers+1) + " :") == testkey[answers]:
            tempstudentanswers.append(1)
        else:
            tempstudentanswers.append(0)

    #Returning the student's answers being correct or not at each question.
    return tempstudentanswers

#Defining the statistics for the entire graded set. This takes in all the calculated grades from all students in the session with this key and calculated the wanted statistics.
def statistics(allinputtedgrades):

    #Using len() for the parameter list as the number of grades in the list will be the number of students and list elements in the list.
    print("There was " + str(len(allinputtedgrades)) + " quizzes graded.")

    #Using the sum() function as all the parameter list should be full of only integers and sum adds them up for the average. Then using len() to divide the sum by the number of students getting the class average.
    print("The average was : " + str(sum(allinputtedgrades)/len(allinputtedgrades)))

    #Sorting the grade list so the list goes low to high. This allows retreiving the highest/lowest grade just going to the end or beginning of the list.
    allinputtedgrades.sort()

    #Going to the list element which is first or last as the list is sorted to go from low to high and the list has all the grades.
    #Using len() as it will contain the # of students whose grades are in the list and subtracting 1 as list elements count from 0.
    print("The highest score is :" + str(allinputtedgrades[len(allinputtedgrades)-1]))
    print("The lowest score is: " + str(allinputtedgrades[0]))


#Setting a variable to hold the returns from the key function giving us the key and num questions required for the rest of the program.
currentinitvalues = key()

#Having the Student Number so the teacher can keep track of which student he or she is grading currently.
numstudents = 1

#Setting an empty list to hold all the final grades.
allgrades = []

#A while loop for grading all the student quizzes until the teacher wants to stop with the current key.
while True:
    #Caculates the student grade by using the grading() function with the user key, number of questions, and the current student.
    studentgrade = (grading(currentinitvalues[0], currentinitvalues[1], numstudents).count(1)/currentinitvalues[1]) * 100

    #Apeending this value to the list of all grades for statistics usage in the statistics().
    allgrades.append(studentgrade)

    #Printing out the current score for the student so the teacher is notified of the student she is grading and its score.
    print("The score for Student #" + str(numstudents) + "'s quiz is: " + str(studentgrade))

    #increasing the student number by 1 as the teacher has graded a student
    numstudents += 1

    #Asking if the teacher wants to continue grading quizzes by using an input(). If the teacher responds "Y" another student grading sequence is initated. If the teacher types anything else the loop is broken as all students should be graded.
    if input("Do you want to grade another quiz? [Y/N]") == "Y":
        continue
    else:
        break

#running statistics() to output the class statistics.
statistics(allgrades)



