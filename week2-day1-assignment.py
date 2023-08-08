# Exercise #1
# Accept two user ages as inputs and give us the difference between them. 
# (The Answer should always be a positive output)


user1 = int(input("what is your age: "))
user2 = int(input("what is your age: "))

if user1 > user2 :
    result = user1 - user2
else :
    result =user2 - user1

print(result)

# Exercise #2
# Accept 3 user inputs for variables named noun, verb and adjective. 
# Print out a formatted string using the outputs.

noun = input("enter a noun: ")
verb = input ("enter a verb: ")
adjective = input("enter a adjective: ")

print(f" your name is {noun} , and you like to {verb} {adjective}.")


# Exercise #3
# Take in a users input for their age, 
# if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

user1 = int(input("what is your age: "))

if user1 < 18 :
    print("kids")
elif user1 >= 18 and user1 <=65 :
    print("adults")
else:
    print("seniors")


# Exercise #4
# Take in a number from a user input, output the number squared.
user1 = int(input("what is your age: "))

print(user1**2)


# Exercise #5
# Check the below variables' length. 
# If the length of the word is greater than 5 output True, 
# if it is less than 5, output False
def word_legnth(var):
    
    if len(var) > 5:
        return True
    else:
        return False
      
    
print(word_legnth('Devante'))   
    