import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================================
# BOOKSTORE CLASS - OOP
# ==========================================================

class Bookstore:

    def __init__(self):
        self.books = []
        self.sales = []

    # ------------------------------------------------------
    # Add Book
    # ------------------------------------------------------
    def add_book(self, title, author, price, quantity):

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            return

        book = {
            "Title": title,
            "Author": author,
            "Price": price,
            "Quantity": quantity
        }

        self.books.append(book)
        print("Book added successfully!")

    # ------------------------------------------------------
    # Update Inventory
    # ------------------------------------------------------
    def update_inventory(self, title, quantity):

        for book in self.books:
            if book["Title"].lower() == title.lower():

                if quantity <= 0:
                    print("Quantity must be positive.")
                    return

                book["Quantity"] = quantity
                print("Inventory updated successfully!")
                return

        print("Book not found.")

    # ------------------------------------------------------
    # Record Sale
    # ------------------------------------------------------
    def record_sale(self, title, quantity):

        for book in self.books:

            if book["Title"].lower() == title.lower():

                if quantity <= 0:
                    print("Quantity must be positive.")
                    return

                if quantity > book["Quantity"]:
                    print("Not enough stock available.")
                    return

                # Deduct stock
                book["Quantity"] -= quantity

                total = book["Price"] * quantity

                sale = {
                    "Title": book["Title"],
                    "Quantity": quantity,
                    "Price": book["Price"],
                    "Total": total
                }

                self.sales.append(sale)

                print("Sale recorded successfully!")
                print("Total Sale Amount:", total)
                return

        print("Book not found.")

    # ------------------------------------------------------
    # Remove Book
    # ------------------------------------------------------
    def remove_book(self, title):

        for book in self.books:

            if book["Title"].lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!")
                return

        print("Book not found.")

    # ------------------------------------------------------
    # Display Inventory
    # ------------------------------------------------------
    def display_inventory(self):

        if not self.books:
            print("Inventory is empty.")
            return

        df = pd.DataFrame(self.books)

        print("\n========== BOOK INVENTORY ==========")
        print(df.to_string(index=False))

    # ------------------------------------------------------
    # Low Stock Books
    # ------------------------------------------------------
    def low_stock(self):

        print("\n========== LOW STOCK BOOKS ==========")

        found = False

        for book in self.books:

            if book["Quantity"] < 5:
                print(
                    f"Title: {book['Title']} | "
                    f"Quantity: {book['Quantity']}"
                )
                found = True

        if not found:
            print("No low-stock books.")

    # ------------------------------------------------------
    # Inventory Analytics
    # ------------------------------------------------------
    def inventory_analytics(self):

        if not self.books:
            print("No inventory data available.")
            return

        df = pd.DataFrame(self.books)

        total_books = df["Quantity"].sum()
        inventory_value = (df["Price"] * df["Quantity"]).sum()
        average_price = df["Price"].mean()

        print("\n========== INVENTORY ANALYTICS ==========")
        print("Total Books in Stock:", total_books)
        print("Total Inventory Value:", inventory_value)
        print("Average Book Price:", round(average_price, 2))

        # NumPy Array
        quantities = np.array(df["Quantity"])

        print("Maximum Stock:", np.max(quantities))
        print("Minimum Stock:", np.min(quantities))
        print("Average Stock:", round(np.mean(quantities), 2))

    # ------------------------------------------------------
    # Sales Analytics
    # ------------------------------------------------------
    def sales_analytics(self):

        if not self.sales:
            print("No sales data available.")
            return

        df = pd.DataFrame(self.sales)

        total_sales = df["Total"].sum()
        total_books_sold = df["Quantity"].sum()

        best_selling = (
            df.groupby("Title")["Quantity"]
            .sum()
            .idxmax()
        )

        print("\n========== SALES ANALYTICS ==========")
        print("Total Books Sold:", total_books_sold)
        print("Total Sales Revenue:", total_sales)
        print("Best Selling Book:", best_selling)

        print("\nSales Data:")
        print(df.to_string(index=False))

    # ------------------------------------------------------
    # Save Inventory Dataset
    # ------------------------------------------------------
    def save_inventory(self):

        if not self.books:
            print("No inventory data to save.")
            return

        df = pd.DataFrame(self.books)
        df.to_csv("book_inventory.csv", index=False)

        print("Inventory saved to book_inventory.csv")

    # ------------------------------------------------------
    # Save Sales Dataset
    # ------------------------------------------------------
    def save_sales(self):

        if not self.sales:
            print("No sales data to save.")
            return

        df = pd.DataFrame(self.sales)
        df.to_csv("book_sales.csv", index=False)

        print("Sales data saved to book_sales.csv")

    # ------------------------------------------------------
    # Sales Chart - Matplotlib
    # ------------------------------------------------------
    def sales_chart(self):

        if not self.sales:
            print("No sales data available.")
            return

        df = pd.DataFrame(self.sales)

        sales_data = df.groupby("Title")["Quantity"].sum()

        plt.figure(figsize=(9, 5))

        sales_data.plot(kind="bar")

        plt.title("Book-wise Sales")
        plt.xlabel("Book Title")
        plt.ylabel("Quantity Sold")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    # ------------------------------------------------------
    # Inventory Chart - Seaborn
    # ------------------------------------------------------
    def inventory_chart(self):

        if not self.books:
            print("No inventory data available.")
            return

        df = pd.DataFrame(self.books)

        plt.figure(figsize=(9, 5))

        sns.barplot(
            data=df,
            x="Title",
            y="Quantity"
        )

        plt.title("Book Inventory")
        plt.xlabel("Book Title")
        plt.ylabel("Available Quantity")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


# ==========================================================
# MAIN PROGRAM
# ==========================================================

store = Bookstore()


# Sample Dataset
store.add_book("Python Basics", "John Smith", 450, 10)
store.add_book("Data Science", "Robert Brown", 600, 8)
store.add_book("Machine Learning", "David Lee", 750, 6)
store.add_book("Artificial Intelligence", "James Wilson", 900, 4)
store.add_book("Web Development", "Michael Clark", 500, 12)


# ==========================================================
# MENU
# ==========================================================

while True:

    print("\n")
    print("==============================================")
    print("   BOOKSTORE INVENTORY & ANALYTICS SYSTEM")
    print("==============================================")
    print("1. Add Book")
    print("2. Display Inventory")
    print("3. Update Inventory")
    print("4. Remove Book")
    print("5. Record Sale")
    print("6. Low Stock Books")
    print("7. Inventory Analytics")
    print("8. Sales Analytics")
    print("9. Save Inventory Dataset")
    print("10. Save Sales Dataset")
    print("11. Show Sales Chart")
    print("12. Show Inventory Chart")
    print("13. Exit")
    print("==============================================")


    choice = input("Enter your choice: ")


    # ------------------------------------------------------
    # Add Book
    # ------------------------------------------------------
    if choice == "1":

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            store.add_book(
                title,
                author,
                price,
                quantity
            )

        except ValueError:
            print("Please enter valid numbers.")


    # ------------------------------------------------------
    # Display Inventory
    # ------------------------------------------------------
    elif choice == "2":

        store.display_inventory()


    # ------------------------------------------------------
    # Update Inventory
    # ------------------------------------------------------
    elif choice == "3":

        title = input("Enter book title: ")

        try:
            quantity = int(input("Enter new quantity: "))
            store.update_inventory(title, quantity)

        except ValueError:
            print("Invalid quantity.")


    # ------------------------------------------------------
    # Remove Book
    # ------------------------------------------------------
    elif choice == "4":

        title = input("Enter book title to remove: ")

        store.remove_book(title)


    # ------------------------------------------------------
    # Record Sale
    # ------------------------------------------------------
    elif choice == "5":

        title = input("Enter book title: ")

        try:
            quantity = int(input("Enter quantity sold: "))

            store.record_sale(
                title,
                quantity
            )

        except ValueError:
            print("Invalid quantity.")


    # ------------------------------------------------------
    # Low Stock
    # ------------------------------------------------------
    elif choice == "6":

        store.low_stock()


    # ------------------------------------------------------
    # Inventory Analytics
    # ------------------------------------------------------
    elif choice == "7":

        store.inventory_analytics()


    # ------------------------------------------------------
    # Sales Analytics
    # ------------------------------------------------------
    elif choice == "8":

        store.sales_analytics()


    # ------------------------------------------------------
    # Save Inventory
    # ------------------------------------------------------
    elif choice == "9":

        store.save_inventory()


    # ------------------------------------------------------
    # Save Sales
    # ------------------------------------------------------
    elif choice == "10":

        store.save_sales()


    # ------------------------------------------------------
    # Sales Chart
    # ------------------------------------------------------
    elif choice == "11":

        store.sales_chart()


    # ------------------------------------------------------
    # Inventory Chart
    # ------------------------------------------------------
    elif choice == "12":

        store.inventory_chart()


    # ------------------------------------------------------
    # Exit
    # ------------------------------------------------------
    elif choice == "13":

        print("Thank you for using Bookstore System!")
        break


    else:

        print("Invalid choice. Please try again.")
