name=input("Enter the name of the Student :")
Class_name=input("Enter the name of the class :")
#name2=input("Enter the marks")
english=int(input("Enter the marks of english :"))
Maths=int(input("Enter the marks of MAths :"))
Hindi=int(input("Enter the marks of Hindi  :"))
Physics=int(input("Enter the marks of Physics :"))
Chemistry=int(input("Enter the marks of Chemistry :"))
Total_marks=english+Maths+Hindi+Physics+Chemistry
print("print the sum of the number :",Total_marks)
avg=Total_marks/5
print("avg of the marks :",avg)

if avg>=80:
	print("grade A")
elif avg>=70:
	print("Grade B")
elif avg>=60:
	print("Grade C")
else:
    print("Grade F ")
