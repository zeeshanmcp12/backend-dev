
# Floor Division
floor_division_num = 10 // 3
print("Floor Division number is:", floor_division_num)
# Output: 3

# Changing in place
player_score = 123456

print("Player score: " + str(player_score)) # No error because of type casting to string
# print("Player score: " + player_score) # can only concatenate str (not "int") to str

# Plus Equal - Reassigning the value
player_score += 1
print("Updated player score: " + str(player_score)) # No error because of type casting to string

# Scientific Notation
scientific_number = 14.1e2
print(str(scientific_number) + " represents as 14.1e2 using 'Scientific Notation'")

max_number_of_players = 1.024e18
print(max_number_of_players)
# Output in decimal notation
# 1,024,000,000,000,000,000

print("---------- Logical Operators in Python ----------")
print("True and True is " + str(True and True) + " Because Logical AND requires both side to be True")
# True
print("True and False is " + str(True and False) + " Because Logical AND requires both side to be True")
# False
print("True or False is " + str(True or False) + " Because Logical OR requires atleast one input to be True")
# True
print("False or False is " + str(False or False) + " Because Logical OR requires atleast one input to be True")
# False
