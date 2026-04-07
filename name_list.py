"""
Angelo Scala
000354536

Member name list
"""

nameList = []

while True:
    add = input("Add member?(Yes, No) ").lower() # takes response in lower case
    if add in ["yes", "y"]: # checks if response is yes
        adding = True

        while True:   # adding is true
            name = input("Enter your name: ").title() # capitalizes first letter

            if not name.isalpha(): # checks if name not alpha
                print("Please enter valid name.")
                continue   # if name not alpha restarts loop

            else:    
                nameList.append(name) # appends to nameList
                break   # breaks from while loop
        continue    # restarts from input option
        
            
    elif add in ["no", "n"]:
        print("Session finished.") # checks if response is no
        break
        
    else:
        print("Please enter valid response.")
        continue # restarts prompt if response invalid

print("Members added: ", nameList)

