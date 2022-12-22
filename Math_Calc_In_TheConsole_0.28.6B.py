""" Start the application.
The application is coded
in Python.
"""
#Internal module(s)
import os
import sys
try:
    #Modules
    print("Starting the application...")
    os.system("cls")
    print("Importing modules...")
    from colorama import Fore, Back, Style, init
    from time import sleep
    from printy import inputy
    import signal
    import keyboard
    from math import sqrt
    init()

    #Variables
    print("Loading variables...")
    versionOfApp = "0.28.6 Beta"

    #Definitions
    print("Loading and reading definitions...")
    print("Loading and reading definition \42AppHome\50\51\42...")
    def AppHome():
        os.system("cls")
        print()
        print(Fore.LIGHTRED_EX + "This application is a beta version, as it may contain a couple of bugs and/or malware." + Fore.RESET)
        print("Math: Calc In The Console - Version " + versionOfApp + ". Commands")
        print("To add, type \42Add\42")
        print("To subtract, type \42Subtract\42")
        print("To multiply, type \42Multiply\42")
        print("To divide, type \42Divide\42")
        print("To get the square \50NOT SQRT\51, type \42Squaring\42")
        print("To get the square root of a number, type \42SQRT\42")
        print("To get a part of a number, type \42Percent.Part\42")
        print("To reveal the total of a part of a number and percentage, type \42Percent.RevealTotal\42")
        print("To reveal the percentage of a part of a number and total, type \42Percent.RevealPercentage\42")
        print("To round a decimal number, type \42Round\42")
        print("To close the application, type \42Exit\42. To close the application necesarily, type \42ForceAction.Exit\42 in case of an emergency.")
        print("To close the application necesarily, you can also open a task manager or application manager and end this process.")
        print("Note: These commands are case-sensitive. If you write something that's out of these available commands, the application gives you an error.")
    print("Loading and reading definition \42QuickOperations\50\51\42...")
    def QuickOperations():
        actInput = input("Action: ")
        while True:
            if actInput == "Exit":
                print("Please wait... Exiting...")
                sleep(2.5)
                os.system("cls")
                print("Thanks for opening and using this application! See you soon!")
                sleep(3)
                exit()
                break
            if actInput == "ForceAction.Exit":
                exit()
                break
            elif actInput == "Add":
                os.system("cls")
                print("Type the numbers to add:")
                print("First number:")
                sum1 = float(input())
                print("Second number:")
                sum2 = float(input())
                sumres = sum1 + sum2
                sumroundres = round(sumres)
                print("The result of your sum is:")
                print(sumres)
                print("Rounded result:")
                print(sumroundres)
                sleep(10)
                print("Operation: ", sum1, " + ", sum2)
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Subtract":
                os.system("cls")
                print("Type the numbers to subtract:")
                print("First number:")
                sub1 = float(input())
                print("Second number:")
                sub2 = float(input())
                subres = sub1 - sub2
                subroundres = round(subres)
                print("The result of your subtraction is:")
                print(subres)
                print("Rounded result:")
                print(subroundres)
                sleep(10)
                print("Operation: ", sub1, " - ", sub2)
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Multiply":
                os.system("cls")
                print("Type the numbers to multiply:")
                print("First number \50to be multiplied\51:")
                multiply1 = float(input())
                print("Second number \50to multiply by\51:")
                multiply2 = float(input())
                multiplyres = multiply1 * multiply2
                multiplyroundres = round(multiplyres)
                print("The result of your multiplication is:")
                print(multiplyres)
                print("Rounded result:")
                print(multiplyroundres)
                sleep(10)
                print("Operation: ", multiply1, " * ", multiply2)
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Divide":
                os.system("cls")
                print("Type the numbers to divide:")
                print("First number \50to be divided\51:")
                divide1 = float(input())
                print("Second number \50to divide by\51:")
                divide2 = float(input())
                if divide1 == 0:
                    print("The division by cero is impossible to do. Try again later! However, the result returns 0.")
                    sleep(5)
                    AppHome()
                    QuickOperations()
                if divide2 == 0:
                    print("The division by cero is impossible to do. Try again later! However, the result returns 0.")
                    sleep(5)
                    AppHome()
                    QuickOperations()
                divideres = divide1 / divide2
                divideroundres = round(divideres)
                print("The result of your division is:")
                print(divideres)
                print("Rounded result:")
                print(divideroundres)
                sleep(10)
                print("Operation: ", divide1, " / ", divide2)
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Squaring":
                os.system("cls")
                print("Type the number to get its square:")
                print("Number:")
                square1 = float(input())
                squareres = pow(square1,2)
                squareroundres = round(squareres)
                print("The square of that number is:")
                print(squareres)
                print("Rounded result:")
                print(squareroundres)
                sleep(10)
                print("Operation: ", square1, " * ", square1)
                squareSqrtConfirmation = input("Would you like to get its square root? Type Y or Yes to get the square root. If you type any other thing, it means that you don't want to get the square root of its result. This is NOT case-sensitive. ")
                if squareSqrtConfirmation == "Y":
                    sqrtSquared = sqrt(squareres)
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "y":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "Yes":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "yes":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "yES":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YES":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "yeS":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YEs":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YeS":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "yEs":
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YES!":
                    print("Thank you for being happy of that!")
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "Yes!":
                    print("Thank you for being happy of that!")
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YEES!":
                    print("Thank you for being happy of that!")
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YEEES!":
                    print("Thank you for being happy of that!")
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "YEEEES!":
                    print("Thank you for being happy of that!")
                    sqrtSquared = sqrt(squareres)
                    print("The square root of that squared number is:")
                    print(sqrtSquared)
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "Nope":
                    print("OK. I will not do this operation.")
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "Nope.":
                    print("OK. I will not do this operation.")
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "Nope!":
                    print("OK. I will not do this operation.")
                    sleep(15)
                    AppHome()
                    QuickOperations()
                elif squareSqrtConfirmation == "NOPE!":
                    print("OK. I will not do this operation and DO NOT SCREAM ME ANYMORE!")
                    sleep(15)
                    AppHome()
                    QuickOperations()
                else:
                    sleep(15)
                    AppHome()
                    QuickOperations()
            elif actInput == "SQRT":
                os.system("cls")
                print("Type the number to get its square root:")
                print("Number:")
                sqrt1 = float(input())
                sqrtres = sqrt(sqrt1)
                sqrtroundres = round(sqrtres)
                print("The square root of that number is:")
                print(sqrtres)
                print("Rounded result:")
                print(sqrtroundres)
                sleep(10)
                AppHome()
                QuickOperations()
            elif actInput == "Percent.Part":
                os.system("cls")
                print("Type the numbers to get the part of a number by using the rule of three:")
                print("Percent:")
                numPercent = float(input())
                print("Total:")
                numTotal = float(input())
                percentpartres = numPercent * numTotal / 100
                percentpartroundres = round(percentpartres)
                print("The part of that number is:")
                print(percentpartres)
                print("Rounded result:")
                print(percentpartroundres)
                sleep(10)
                print("Operation: ", numPercent, " * ", numTotal, " / 100")
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Percent.RevealTotal":
                os.system("cls")
                print("Type the numbers to reveal the total of a part of a nuumber and percentage by using the rule of three:")
                print("Part:")
                numPart = float(input())
                print("Percent:")
                numPercent = float(input())
                percenttotalres = 100 * numPart / numPercent
                percenttotalroundres = round(percenttotalres)
                print("The total of that part is:")
                print(percenttotalres)
                print("Rounded result:")
                print(percenttotalroundres)
                sleep(10)
                print("Operation: ", "100 * ", numPart, " / ", numPercent)
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Percent.RevealPercentage":
                os.system("cls")
                print("Type the numbers to reveal the percentage of a part and total of a number by using the rule of three:")
                print("Part:")
                numPart = float(input())
                print("Total:")
                numTotal = float(input())
                percentageres = numPart * 100 / numTotal
                percentageroundres = round(percentageres)
                print("The total of that part is:")
                print(percentageres, "%")
                print("Rounded result:")
                print(percentageroundres, "%")
                sleep(10)
                print("Operation: ", numPart, " * 100  / ", numTotal)
                sleep(15)
                AppHome()
                QuickOperations()
            elif actInput == "Round":
                os.system("cls")
                print("Type a decimal number to get its rounded result:")
                print("Number:")
                round1 = float(input())
                roundres = round(round1)
                print("The rounded number is:")
                print(roundres)
                sleep(10)
                AppHome()
                QuickOperations()
            elif actInput == "":
                print("You didn't typed anything. Try again.")
                print()
                actInput = input("Action: ")
            elif actInput == "ForceAction.CloseInmediatelyByNull":
                cls
                print("Returning null...")
                return null
                break
            elif actInput == "DECEMBER25":
                print("Merry Christmas!")
                actInput = input("Action: ")
            elif actInput == "DECEMBER31":
                print("The date \42December 31, 2022\42 is the New Year's Eve.")
                actInput = input("Action: ")
            elif actInput == "JANUARY1":
                print("Happy New Year!")
                actInput = input("Action: ")
            elif actInput == "Y2K38":
                print("\42January 19, 2038\42 is the last date that 32-bit systems support. After that date, 32-bit systems stop working because after the second 2147483647 \50\42January 19, 2038 at 3:14:07 AM\42\51, skips to second -2147483648 that's \42December 13, 1901 at 8:45:52 PM\42, so you have enough time to upgrade to 64-bit systems \50if you want\51.")
                actInput = input("Action: ")
            elif actInput == "ForceAction.GlitchTheApplication.StopWorking.ActionInput":
                while True:
                    AppHome()
                    actInput = input("Action: ")
            elif actInput == "ForceAction.GlitchTheApplication.StopWorkingBy.InfiniteAppHomeLoops":
                while True:
                    AppHome()
            elif actInput == "ForceAction.GlitchTheApplication.StopWorkingBy.InfiniteAppHomeLoops.InfiniteTrueFalse":
                while True:
                    AppHome()
                    while False:
                        AppHome()
            elif actInput == "ForceAction.GlitchTheApplication.StopWorkingBy.InfiniteQuickOperationsLoops":
                while True:
                    QuickOperations()
            elif actInput == "ForceAction.GlitchTheApplication.StopWorkingBy.InfiniteQuickOperationsLoops.InfiniteTrueFalse":
                while True:
                    QuickOperations()
                    while False:
                        QuickOperations()
            elif actInput == "ForceAction.GlitchTheApplication.StopWorkingBy.GeneratingInfiniteLoopsWithBlankSpaces":
                print()
            elif actInput == "ForceAction.QuickRestart":
                print("Restarting quickly...")
                sleep(2.5)
                break
            else:
                print("\42" + actInput + "\42" + " is neither a mathematic operation nor an action. Try again.")
                print()
                actInput = input("Action: ")
    print("Loading and reading definition \42main\50\51\42...")
    def main():
        print("Loading...")
        sleep(2.5)
        AppHome()
    
    #Entire application
    while True:
        main()
        QuickOperations()
except Exception:
    print(Back.RED + Fore.LIGHTWHITE_EX + "Error! Something went wrong during or before running the application and/or doing an operation! Exiting..." + Style.RESET_ALL)
    exit()