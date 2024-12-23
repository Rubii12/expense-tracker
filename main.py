import csv
import os
import matplotlib.pyplot as plt
import pandas as pd

file_name="expenses.csv"

def add_expense(date,category,amount,description=""):
    file_exists=os.path.exists(file_name)
    with open(file_name,mode='a',newline='') as file:
        writer=csv.writer(file)
        if not file_exists:
            writer.writerow(["Date","Category","Amount","Description"])
        writer.writerow([date,category,amount,description])
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(file_name):
        print("No expenses recorded yet.")
        return

    df=pd.read_csv(file_name)
    print("\nYour expenses")
    print(df.to_string(index=False))

def visualize_expenses():
    if not os.path.exists(file_name):
        print("No expenses to visualize")
        return

    df=pd.read_csv(file_name)
    category_sum=df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8,6))
    category_sum.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Expense Distribution by Category")
    plt.ylabel("")
    plt.show()

def show_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Visualize Expenses")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice=input("Enter your choice:")
        if choice=="1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Travel): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            add_expense(date, category, amount, description)
        
        elif choice=="2":
            view_expenses()

        elif choice=="3":
            visualize_expenses()

        elif choice=="4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Enter correct option!")

if __name__=="__main__":
    main()