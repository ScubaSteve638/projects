# Convert Inches to mm
def mm(inches):
    result = inches * 25.4
    start = "The conversion from "
    mid = " Inch(es) to "
    end = "mm is what you need!"
    return start + str(inches) + mid + str(round(result,1)) + end

# Now for the output
import os
os.system('cls')
inch = input("How many Inches do you want to convert?: ")
if inch >= "6": print("Is this male of female size?")

print(mm(float(inch)))