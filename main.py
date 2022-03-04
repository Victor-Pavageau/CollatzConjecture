from itertools import chain


def CollatzConjecture(StartNumber):
    global Sucess, AlreadyDoneList
    NumberOfLoop = 0
    ListResult = []
    CurrentNumber = StartNumber
    while((CurrentNumber not in ListResult) and (CurrentNumber not in AlreadyDoneList)):
        NumberOfLoop += 1
        ListResult.append(CurrentNumber)
        if(CurrentNumber%2==0):
            CurrentNumber /= 2
        elif(CurrentNumber%2==1):
            CurrentNumber *= 3
            CurrentNumber += 1
        if(NumberOfLoop > 500):
            for loop in range(len(ListResult)):
                if(ListResult[loop] not in AlreadyDoneList):
                    AlreadyDoneList.append(ListResult[loop])
            print("\nThe number " + str(StartNumber) + " has success to the " + str(NumberOfLoop) + "th step of the Collatz conjecture.\nSequence : " + str(ListResult) + "\n")
            Sucess = True
            break
    if(not Sucess):
            for loop in range(len(ListResult)):
                if(ListResult[loop] not in AlreadyDoneList):
                    AlreadyDoneList.append(ListResult[loop])
            print("\nThe number " + str(StartNumber) + " has failed to the Collatz conjecture in " + str(NumberOfLoop) + " steps.\nSequence : " + str(ListResult) + "\n")

Sucess = False
StartNumber = int(input("Start number ?\n"))
AlreadyDoneList = []

while(not Sucess):
    CollatzConjecture(StartNumber)
    StartNumber += 2