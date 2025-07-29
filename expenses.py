from datetime import datetime
import pytz , os

# Türkiye saat dilimi
istanbul = pytz.timezone("Europe/Istanbul")

def clear():
    os.system("cls")
    
global type_of_expense
global amount
global expenses
expenses = open("D:\Masaüstü\CODİNG\python\my_kivy\expenses.txt","a+")

def input_expense(expenses=expenses):
    tarih_tr = datetime.now(istanbul)
    type_of_expense = input("Card or Cash : ")
    if type_of_expense.lower() == "cash":
        amount = float(input("Please input the amount as float (Ex: 17.0 or 18.25) : "))
        explanation = input("Please input the explanation for this expense : ")

        expenses.write(f"{tarih_tr.date()} - {amount} - {explanation} - {type_of_expense}\n")
        print(f"Expense recorded: {tarih_tr.date()} - {amount} - {explanation} - {type_of_expense}\n")

    elif type_of_expense.lower() == "card":
        amount = float(input("Please input the amount as float (Ex: 17.0 or 18.25) : "))
        explanation = input("Please input the explanation for this expense : ")
        card_name=input("Please input the card name : ")
        expenses.write(f"{tarih_tr.date()} - {amount} - {explanation} - {type_of_expense.lower()}: {card_name}\n")
        print(f"Expense recorded: {tarih_tr.date()}  - {amount} - {explanation} - {type_of_expense.lower()}: {card_name}")
   
    else:
        print("Please input either 'Card' or 'Cash' as type of expense.")
        return

def show_all_expenses(expenses=expenses):
    expenses.seek(0)  # Dosyanın başına dön
    print("Recorded Expenses:")
    for line in expenses:
        print(line.strip())

def close_expenses_file(expenses=expenses):
    expenses.close()
    print("Expenses file closed.")

def show_expenses_by_type(expense_type):
    expenses.seek(0)  # Dosyanın başına dön
    print(f"Expenses of type '{expense_type}':")
    x1=0
    for line in expenses:
        if expense_type.lower() in line.lower():
            x1+=1
            print(line.strip())
    
    if expense_type == "card":
        choice = input("If you want to see expenses for a specific card name, enter 'yes' or enter anything else to continue: ")
        if choice.lower() == 'yes':
            card_name = input("Please enter the card name to filter expenses by spesific card name: ").lower()
            expenses.seek(0)
            x2 = 0
            for line in expenses:
                if card_name.lower() in line.lower():
                    x2+=1
                    print(line.strip())
            if x2 == 0:
                print(f"No expenses found for the card name '{card_name}'.")
    else:
        if expense_type.lower() == "cash" and x1==0 :
            print("No cash expenses recorded.")
    
def show_total_expenses_by_type(expense_type):
    expenses.seek(0)
    total = 0.0
    expense_type = expense_type.lower()

    for line in expenses:
        parts = line.strip().split(' - ')
        if len(parts) < 4:
            continue  # format uymayan satırı atla

        date_str, amount_str, explanation, payment_type = parts

        # payment_type örn: "card: garanti" veya "cash"
        # expense_type filtrelemesi için:
        if expense_type in payment_type.lower():
            try:
                total += float(amount_str)
            except ValueError:
                print(f"Could not convert amount '{amount_str}' to float.")
    print(f"Total expenses of type '{expense_type}': {total}")
    
    if expense_type.lower() == 'card' :
        choice=input("If you want to see expenses for a spesific card name,enter 'yes' or enter anything else to continue : ")
        if choice.lower() == 'yes' :
            card_name = input("Please enter the card name  : ").lower()
            total = 0.0
            expenses.seek(0)
            for line in expenses:
                parts = line.strip().split(' - ')
                if len(parts) < 4:
                    continue  # format uymayan satırı atla

                date_str, amount_str, explanation, payment_type = parts
                if card_name.lower() in line.lower():
                    try:
                       total += float(amount_str)
                    except ValueError:
                     print(f"Could not convert amount '{amount_str}' to float.")
            print(f"Total expenses of  '{card_name}' card : {total}")

while True:
    clear()
    print("Welcome to the Expense Tracker! \
      \n1) Input Expense  \
      \n2) See All Expenses \
      \n3) Show Expenses By Type \
      \n4) Show Total  Expenses By Type \
      \n5) Exit The Tracker ")
    
    choice=int(input("Choice an option from above : "))
    # print("Note :  ")
    if choice not in [1,2,3,4,5] or type(choice) != int:
        print("Please choice one of options which mentioned above")
        continue
    else:
        if choice == 5:
            print("Exiting Espense Tracker...")
            expenses.flush()  
            expenses.close()
            
            break
        elif choice == 1:
            input_expense(expenses)
            expenses.flush() 
            a=input("Press Enter to continue...")
           
            continue

        elif choice == 2:
            show_all_expenses(expenses)
            a=input("Press Enter to continue...")
            
            continue

        elif choice == 3:
            e_type = input("Please input the type of expense (Card or Cash) to see expenses by type : ")     
            show_expenses_by_type(e_type)
            a=input("Press Enter to continue...")
            
            continue
        
        elif choice == 4:
            e_type = input("Please input the type of expense (Card or Cash) to see total expenses by type : ")  
            show_total_expenses_by_type(e_type)
            a=input("Press Enter to continue...")
           
            continue
    