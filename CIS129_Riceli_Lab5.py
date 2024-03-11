#Riceli Foster
#March 10, 2024
#Lab 5 The Bottle Return Program
#This program returns a grocery store's bottle return count and payout and allows the user to enter another week.

totalBottles = 0
#This variable will store the accumulated bottle values

counter = 1
#This variable will control the loop

todayBottles = 0
#This variable will store the number of bottles returned on a day

totalPayout = 0
#This variable will store the calculated value of totalBottles times 10

keepGoing = 'y'
#This variable will run the program again

while keepGoing == 'y': #This is the while loop that will determine if the program keeps going or quits.
    counter = 1 #Set variable equal to one since after the program resets, you want the counter to always be at one.
    for bottles in range (7): #This gives you seven  days' worth of data.
        print('Enter number of bottles for day #',counter,':') #Input
        todayBottles = int(input())
        counter += 1 #The += adds the total to the variable (same as line directly underneath)
        totalBottles += todayBottles
    todayBottles = int()
    totalPayout = (.10 * totalBottles)
    totalPayout = format(totalPayout, ".2f")
    print('The total number of bottles collected is',totalBottles) #Display 
    print('The total paid out is $:',totalPayout)
    keepGoing = input('Do you want to enter another week? "y" for yes.\n')
    



