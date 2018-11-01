#Dan Coleman
#Assignment 1 R00151926 
#Validation wasn't mentioned on the spec, and I was short on time so I didn't add any
#22/10/2018

import numpy as np 

#Prints out the menu of options
def printMenu():
    print("MENU \n 1. Basic Statistics for Total Rainfall (Millimetres)")
    print(" 2. Basic Statistics for Most Rainfall in a Day (Millimetres) \n 3. Basic Statistics for Number of Rain days (0.2mm or More)")
    print(" 4. Wettest Location \n 5. Percentage of Rain Days \n 6. Exit")

#Deals with the input for the menu
def menuAnswer(cont, ans):
    if ans == 1:
        totalRain()
        return cont
    elif ans == 2:
        mostRain()
        return cont
    elif ans == 3:
        daysRain()
        return cont
    elif ans == 4:
        wettestLocation()
        return cont
    elif ans == 5: 
        percentOfDaysRain()
        return cont
    elif ans == 6:
        print("Goodbye")
        cont = "exit"
        return cont
    else: 
        print("Please input 1-6 \n")
        return cont

#Allows user to pick which location they wish to see the info for
def locationSelect(ans):
    location = ""
    if ans == 1:
        location = "Cork"
        return location
    elif ans == 2:
        location = "Belfast"
        return location
    elif ans == 3:
        location = "Dublin"
        return location
    elif ans == 4:
        location = "Galway"
        return location
    elif ans == 5: 
        location = "Limerick"
        return location
    else:
        print("I am error")

#Calculates and prints out Max and average total rainfall for a given location    
def totalRain():
    #Print out
    print("Basic Statistics for Total Rainfall (Millimetres)\n")
    ans = int(input(" 1. Cork\n 2. Belfast\n 3. Dublin\n 4. Galway\n 5. Limerick \nPlease Select a Location: "))
    
    location = locationSelect(ans) #Gets location
    data = np.genfromtxt(location+"Rainfall.txt", delimiter =' ')#Takes data from relevant file
    
    maxRain = np.amax(data[:,2]) #Finds Max of data
    averageRain = np.average(data[:,2]) #Finds Average of Data
    
    #Below prints the data [3] is total rainfall
    print(location + " Max total rainfall: " + str(maxRain))
    print(location + " Average total rainfall: " + str(averageRain) + "\n")

#Calculates and prints out Max and average most rainfall in a day for a given location    
def mostRain():
    print("Basic Statistics for Most Rainfall in a Day (Millimetres)\n")
    ans = int(input(" 1. Cork\n 2. Belfast\n 3. Dublin\n 4. Galway\n 5. Limerick \nPlease Select a Location: "))
    
    location = locationSelect(ans)#Gets location
    data = np.genfromtxt(location + "Rainfall.txt", dtype=float)#Takes data from relevant file
    
    maxRain = np.amax(data[:,3])#Finds Max of data
    averageRain = np.average(data[:,3])#Finds Average of Data
    
    #Below prints the data [4] is the most rainfall for a day
    print(location + " Max most rainfall in a day : " + str(maxRain))
    print(location + " Average most rainfall in a day: " + str(averageRain) + "\n")

#Calculates and prints out Max and average rainy days for a given location
def daysRain():
    print("Basic Statistics for Number of Rain days (0.2mm or More)\n")

    ans = int(input(" 1. Cork\n 2. Belfast\n 3. Dublin\n 4. Galway\n 5. Limerick \n Please Select a Location: "))
    
    location = locationSelect(ans)#Gets location
    data = np.genfromtxt(location+"Rainfall.txt", dtype = float)#Takes data from relevant file
    
    maxRain = np.amax(data[:,4])#Finds Max of data
    averageRain = np.average(data[:,4])#Finds Average of Data
    
    #Below prints the data 
    print(location + " Max number of rainy days: " + str(maxRain))
    print(location + " Average number of rainy days: " + str(averageRain))

#Calculates and prints total rainfall for each locations and wettest location    
def wettestLocation():
    print("Wettest Location (in mm)\n")
    totalRainfall = list()
    
    #Gets total rainfall for each county
    for each in range(1, 6):
        totalRainfall.append(totalRainfallList(each))
        #Prints locations name and value
        value = totalRainfall[each - 1]
        print(locationSelect(each) + ": " + str(value))

    #Calculates Wettest Place and then Value for wettest Place and Prints wettest location
    wettestPlace = totalRainfall.index(max(totalRainfall))
    maxRain = max(totalRainfall)
    print("The Wettest Location in Ireland is " + locationSelect(wettestPlace + 1) + 
    " with a rainfall figure of " + str(maxRain) + " mm\n")
    

#Takes in a index from the loop above and puts it in as the answer for the locationSelect then returns total Rainfall
def totalRainfallList(ans):
    location = locationSelect(ans)
    data = np.genfromtxt(location + "Rainfall.txt", dtype=float)#Takes data from relevant file
    return np.sum(data[:,2])


#Takes in the number of rainy days you want, Prints the first text, and loops each location through the calculator.   
def percentOfDaysRain():
    #Print out
    print("Percentage of Rain Day\n")
    treshold = int(input("Please enter maximum threshold value for number of rain days: "))
    print("\nThe following are the percentage of rain days less than or equal to ", treshold, "\n")
    
    #Gets the info for each location in order from function below
    for each in range(1, 6):
       PercentofDaysRainCalculate(each, treshold)
    
#Recieves the index for each location in order and then prints their output the percentage of rows in the dataset where
#the Number of Rain Days is less than or equal to treshold
def PercentofDaysRainCalculate(ans, treshold):
    #gets each passed in locations data
    location = locationSelect(ans)
    data = np.genfromtxt(location + "Rainfall.txt", dtype = float)#Takes data from relevant file

    #makes a list of values within the treshold, calculates and prints percent of that location
    result = data[:,4] <= treshold
    percentage = (len(data[result]) * 100.0) / len(data)
    print(str(ans) + ". " + location + "   \t" + str(percentage) + "%\n")
    return    
    
#Loops the code until exit is selected    
def main():
     cont = "y"
     while (cont == "y"):
          printMenu()
          ans = int(input("Please select one of the above options: "))
          print("\n")
          cont = menuAnswer(cont, ans)

#Calling main function          
main()
