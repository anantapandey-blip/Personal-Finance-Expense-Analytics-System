import numpy as np
monthly_budget= 190000
print("\n---------Personal Finance & Expense Analytics System----------------")
expenses= np.array([["Months","Food","Transport","Shopping", "Bills","Health","Entertainment"],
                     ["January", 7890 , 340 , 5673 , 56789 , 7890 ,  2345],
                     ["February", 5290 , 1340 , 2340 , 43670, 1234,  6789],
                     ["March", 7890 , 6780 , 5673 , 56789 , 7890 ,  2345],
                     ["April", 7890 , 340 , 5673 , 87789 , 7890 ,  2345],
                     ["May", 7890 ,340 , 5673 , 34789 , 7890 ,  2345],
                     ["June", 7890 , 340 , 3673 , 34789 , 7890 ,  9345],
                     ["July", 7890 , 340 , 3673 , 56789 , 7890 ,  7345],
                     ["August", 7890 , 88340 , 5673 , 32789 , 3890 ,  92985],
                     ["September", 7890 , 340 , 5673 , 56789 , 4590 ,  2345], 
                     ["October", 7890 , 340 , 5673 , 65789 , 7890 ,  2345],
                     ["November", 9030 , 340 , 5673 , 893389 , 7890 ,  2345],
                     ["December", 7890 , 340 , 3473 , 90789 , 7890 ,  2345]])

while True:
     menu= input("\n  1. Show all expenses  \n  2. Monthly expenditure   \n  3. Category Expenditure   \n  4. Highest spending month  \n  5. Lowest spending month   \n  6. Find expenses above budget  \n  7. Check budget  \n  8. Change the monthly budget  \n  9. Show months wise expenditure   \n  10. Exit  \n ")
     if menu=="1":
      print("------------------ Expenses of the year --------------------")
      print(expenses)
      save= input("Want to save this in a separate file?(yes/no) ")
      if save=="yes":
       with open("Expenses.txt","w")as f:
           f.write(str(expenses))  
      else:
       continue            
     elif menu=="2":
      
      monthly_expenses = expenses[1: ,1: ].astype(int)                                       
      total_monthly_expenses= np.sum(monthly_expenses,axis=1)
            
      print(f"Your Monthly expenses are  {total_monthly_expenses} ")
      
     elif menu=="3":
      user_input= input("Enter the category: ")
      if user_input=="food":
       print(f"Total Expenditure on food : {np.sum(expenses[1:11,1:2].astype(int))}")
      
      elif user_input=="Transport":
       print(f"Total Expenditure on Transport : {np.sum(expenses[1:11,2:3].astype(int))}")
      
      elif user_input=="Shopping":
       print(f"Total Expenditure on Shopping : {np.sum(expenses[1:11,3:4].astype(int))}")
      
      elif user_input=="Bills":
       print(f"Total Expenditure on food : {np.sum(expenses[1:11,4:5].astype(int))}")
      
      elif user_input=="Health":
       print(f"Total Expenditure on Health : {np.sum(expenses[1:11,5:6].astype(int))}")
      
      elif user_input=="Entertainment":
       print(f"Total Expenditure on Entertainment : {np.sum(expenses[1:11,6:7].astype(int))}")
      
        
     
     elif menu == "4":
       expenditure= expenses[1: , 1:].astype(int)
       total_of_month= np.sum(expenditure,axis=1)
       highest_index= np.argmax(total_of_month)
       highest_month= expenses[1:,0][highest_index]
       print(f"The month with the highest expenses of the year is {highest_month} with total expenditure of : {np.max(total_of_month)}")
             
      
      
     elif menu=="5":
      
      expenditure = expenses[1: , 1:].astype(int)
      total_of_month = np.sum(expenditure , axis= 1)
      lowest_index = np.argmin(total_of_month)
      lowest_month = expenses[1:, 0][lowest_index]

      print(f"The month with the least expenses of the year is  : {lowest_month} with total expenditure of : {np.min(total_of_month)}")
       
     elif menu=="6":
      expenditures= expenses[1:, 1:].astype(int)
      sum_expenses = np.sum(expenditures , axis=1 )
      over_budget= sum_expenses > monthly_budget

      months = expenses[1:,0]
      print( f" In {months[over_budget]} month expenses exceeded the limit")

      
     elif menu=="7":
       print(f"Your monthly budget is ₹ {monthly_budget} ")

     elif menu=="8":
      user_input= int(input("Enter the Change value : "))
      print(f"Your monthly budget has successfully changed from this :  ₹ {monthly_budget}  to  this :  ₹ {user_input}")
     elif menu=="9":
      user_input=input("Enter the month: ")
      if user_input=="January":
        print(f"Total Expenditure in January: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="February":
       print(f"Total Expenditure in February: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="March":
       print(f"Total Expenditure in March: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="April":
       print(f"Total Expenditure in April: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="May":
       print(f"Total Expenditure in May: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="June":
       print(f"Total Expenditure in June: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="July":
       print(f"Total Expenditure in July: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="August":
       print(f"Total Expenditure in August: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="September":
       print(f"Total Expenditure in September: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="October":
       print(f"Total Expenditure in October : {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="November":
       print(f"Total Expenditure in November: {np.sum(expenses[1:2,1:7].astype(int))}")
      if user_input=="December":
       print(f"Total Expenditure in December: {np.sum(expenses[1:2,1:7].astype(int))}")


     elif menu=="10":
      confirm= input("Do you want to exit?(yes/no)")
      if confirm=="yes":
       print("exiting.......")
       print("Program Ended")
       exit
      else:
       continue

