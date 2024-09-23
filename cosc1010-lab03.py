# Ethan Hall
# UWYO COSC 1010
# 09.23.2024
# Lab 03 
# Lab Section: 14
# n/a 
# i
# have
# none



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
names = ["Wyoming", "Colorado", "Montana"]


#print the entire list
print(names)

#now print the first element in the list
print(names[0])


#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(names[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{names[1].upper()} is south of {names[0].upper()}")



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
names.append("Washington")
names.append("Oregon")
names.append("California")
print(names)


#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
names.insert(-2,"Maine")
print(names)
#Insert the state Texas to be the third element in the list, again printing your list
names.insert(2,"Texas") 
print(names)
#Using the `del` statement remove the fourth item from the list, print your list 
del names[3]
print(names)
#Remove Texas using its value, print the list
names.pop(2)
print(names)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(names))
print(names)

#Permanently sort your list in reverse order, printing it out
names.sort(reverse=True)
print(names)

#Using the reverse method reverse the list and print it
names.reverse()
print(names)
