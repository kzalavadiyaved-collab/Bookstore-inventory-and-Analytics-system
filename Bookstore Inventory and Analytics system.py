import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price, quantity):
        if price > 0 and quantity > 0:
            self.books.append([title, author, price, quantity])
            print("Book added")
        else:
            print("Invalid price or quantity")

    def update_inventory(self, title, quantity):
        for book in self.books:
            if book[0].lower() == title.lower():
                book[3] = quantity
                print("Inventory updated")
                return
        print("Book not found")

    def record_sale(self, title, quantity):
        for book in self.books:
            if book[0].lower() == title.lower() and quantity <= book[3]:
                book[3] -= quantity
                print("Sale recorded")
                return
        print("Book not found or insufficient stock")

    def show(self):
        df = pd.DataFrame(
            self.books,
            columns=["Title", "Author", "Price", "Quantity"]
        )
        print(df)

        stock = np.array(df["Quantity"])
        print("Total Stock:", np.sum(stock))
        print("Average Stock:", np.mean(stock))


store = Bookstore()

store.add_book("Python", "John", 500, 10)
store.add_book("AI", "David", 700, 8)
store.add_book("Data Science", "Alex", 600, 5)

store.record_sale("Python", 2)
store.update_inventory("AI", 10)

store.show()

# Analytics Chart
df = pd.DataFrame(
    store.books,
    columns=["Title", "Author", "Price", "Quantity"]
)

sns.barplot(data=df, x="Title", y="Quantity")
plt.title("Bookstore Inventory")
plt.show()
