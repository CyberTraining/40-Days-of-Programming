#40 days of coding
#November 8th 2021
#List Challenge 6: Grade Sorter App. 


title="Welcome to the Grade Sorter App. "
print(title)

grades=[]

# Get user inputs for four Grades
grade =int(input("What is your first grade: ", ))
grades.append(grade)
grade=int(input("What is your second grade: ", ))
grades.append(grade)
grade=int(input("What is your third grade: ", ))
grades.append(grade)
grade=int(input("What is your fourth grade: ", ))
grades.append(grade)



# list the inputs
print("Your Grades are: " + str(grades))

#sort the list items (reverse=True)
grades.sort(reversed=True)
print("Your Grades from Highest to Lowest " +str(grades))

#Remove the Lowest two grades
print("\nThe lowest two grades will now be dropped. ")
removedGrade = grades.pop()
print("Removed Grade: " + str(removedGrade))
removedGrade = grades.pop()
print("Removed Grade: " + str(removedGrade))

#Recap of remaing objects
print("\n your remaing grades are: " + str(grades))


