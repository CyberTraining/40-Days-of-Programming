#40 days of coding
#November 13th 2021
#Loops Challenge 15: Grade Point Average App

#title
print("Welcome to the Grade Point Average Calculator App")


#Get Users Name
name=input("What is your name: ").title().strip()
grade_num=int(input("How many grades would you like to enter: "))

#Get the grades
grades=[]
for i in range(grade_num):
  grades.append(int(input("Enter grade: ")))

#Sort the grades and print
grades.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for grade in grades:
  print("\t" + str(grade))

#Calculate the Average
average=sum(grades)/len(grades)
average = round(average, 2)

#print Average Summary
print("\n" + name + "'s Grades Summary:")
print("\tTotal Number of Grades: " + str(grade_num))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage Grade: " + str(average))

#What is the desired average
desired_avg = float(input("What is your desired average: "))
grade_req = desired_avg*(len(grades)+1) - sum(grades)
grade_req = round(grade_req, 2)

#print a summary
print("\nGood Luck " + str(grade_req) + " on your next assignment to earn a " +str(desired_avg))

#Make a copy of the orginal grades and swap out on of the grades
new_grades=grades[:]
print("\nLet's see what you average could have been if you did better or worse on an assignment. ")
grade_change=int(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade=int(input("What grade would you like to change " +str(grade_change)+ " to: "))
new_grades.append(new_grade) 

#Sort new grades and print them to the screen
new_grades.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for grade in new_grades:
  print("\t" + str(grade))

#Calculate the Average
new_average=sum(new_grades)/len(new_grades)
new_average = round(new_average, 2)

#print Average Summary
print("\n" + name + "'s Grades Summary:")
print("\tTotal Number of Grades: " + str(new_grades))
print("\tHighest Grade: " + str(max(new_grades)))
print("\tLowest Grade: " + str(min(new_grades)))
print("\tAverage Grade: " + str(new_average))

# print summary on how the average changed
print("\nYour new average would be a " +str(new_average) + " compared to your real average of " + str(average) + "!")
average_change=new_average - average
average_change=round(average_change,2)

print("\nThat is a change of " + str(average_change)+ "points!")
print("\nTo bad the original grades are still intacked ")
print(grades)
print("\nYou should ask for extra credits")
