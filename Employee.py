Employee_name=input("Enter the employee name :")
Basic_Salary=float(input("Enter the employee basic salary :"))

#calculate the allowance 

Ta = Basic_Salary*0.05
Da= Basic_Salary*0.10
Hra= Basic_Salary*0.25

Net_salary = Basic_Salary + Ta + Da + Hra
print(Net_salary)

# conditon for Employee grade 

if Net_salary>=80000:
        print("grade A")
elif Net_salary>=60000:
        print("Grade B")
elif Net_salary>=40000:
      print("Grade C")                      
else:
    print("grade f")                    
