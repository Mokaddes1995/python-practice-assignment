# Student Grade Calculator Program

# Takes a student's name

name = input("\nTakes a student's name: ")


# Takes marks for three subjects

marks_1  = int(input("\nEnter Math marks: "))

marks_2 = int(input("Enter English marks: "))
    
marks_3 = int(input("Enter Python marks: "))


# Validation for marks for below 0 & above 100

if marks_1 < 0 or marks_1 > 100:
    
    print("\nInvalid marks! All marks must be between 0 and 100.")
    
elif marks_2 < 0 or marks_2 > 100:
    
    print("\nInvalid marks! All marks must be between 0 and 100.")
    
elif marks_3 < 0 or marks_3 > 100:
    
    print("\nInvalid marks! All marks must be between 0 and 100.")

else:
    
    # Calculate Average

    average_marks = (marks_1 + marks_2 + marks_3) / 3


    # Calculate Grade

    if average_marks >= 80:
        
        grade = "A+"

    elif average_marks >= 70:
        
        grade = "A"

    elif average_marks >= 60:
        
        grade = "A-"
        
    elif average_marks >= 50:
        
        grade = "B"

    elif average_marks >= 40:
        
        grade = "C"

    else:
        
        grade = "F"
        
    
    # Display Information

    print(f"\nStudent Name: {name}")

    print(f"Average Marks: {average_marks:.2f}")

    print(f"Final Grade: {grade}")
