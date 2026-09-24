import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bookstore System", layout="wide")


class Bookstore:

    def __init__(self):
        if "books" not in st.session_state:
            st.session_state.books = [
                {
                    "Title": "Python Basics",
                    "Author": "John Smith",
                    "Price": 450.0,
                    "Quantity": 10,
                },
                {
                    "Title": "Data Science",
                    "Author": "Robert Brown",
                    "Price": 600.0,
                    "Quantity": 8,
                },
                {
                    "Title": "Machine Learning",
                    "Author": "David Lee",
                    "Price": 750.0,
                    "Quantity": 6,
                },
                {
                    "Title": "Artificial Intelligence",
                    "Author": "James Wilson",
                    "Price": 900.0,
                    "Quantity": 4,
                },
                {
                    "Title": "Web Development",
                    "Author": "Michael Clark",
                    "Price": 500.0,
                    "Quantity": 12,
                },
            ]

        if "sales" not in st.session_state:
            st.session_state.sales = []

        self.books = st.session_state.books
        self.sales = st.session_state.sales

    def add_book(self):
        st.header("Add New Book")
        with st.form("add_form"):
            title = st.text_input("Book Title")
            author = st.text_input("Author Name")
            price = st.number_input("Price", min_value=1.0, value=100.0)
            quantity = st.number_input("Quantity", min_value=1, value=1)
            submit = st.form_submit_button("Add Book")

            if submit:
                if title and author:
                    self.books.append(
                        {
                            "Title": title,
                            "Author": author,
                            "Price": price,
                            "Quantity": quantity,
                        }
                    )
                    st.success(f"Book '{title}' added successfully!")
                else:
                    st.error("Please enter Title and Author.")

    def update_inventory(self):
        st.header("Update Book Quantity")
        if not self.books:
            st.warning("Inventory is empty.")
            return

        titles = [b["Title"] for b in self.books]
        selected = st.selectbox("Select Book", titles)
        new_qty = st.number_input("New Quantity", min_value=1, value=1)

        if st.button("Update"):
            for book in self.books:
                if book["Title"] == selected:
                    book["Quantity"] = new_qty
                    st.success(f"Quantity updated for '{selected}'!")
                    break

    def record_sale(self):
        st.header("Record Sale")
        if not self.books:
            st.warning("Inventory is empty.")
            return

        titles = [b["Title"] for b in self.books]
        selected = st.selectbox("Select Book", titles)
        qty = st.number_input("Quantity Sold", min_value=1, value=1)

        if st.button("Record Sale"):
            for book in self.books:
                if book["Title"] == selected:
                    if qty > book["Quantity"]:
                        st.error("Not enough stock!")
                    else:
                        book["Quantity"] -= qty
                        total = book["Price"] * qty
                        self.sales.append(
                            {
                                "Title": book["Title"],
                                "Quantity": qty,
                                "Price": book["Price"],
                                "Total": total,
                            }
                        )
                        st.success(f"Sale recorded! Total Amount: ₹{total}")
                    break

    def remove_book(self):
        st.header("Remove Book")
        if not self.books:
            st.warning("Inventory is empty.")
            return

        titles = [b["Title"] for b in self.books]
        selected = st.selectbox("Select Book", titles)

        if st.button("Remove"):
            st.session_state.books = [
                b for b in self.books if b["Title"] != selected
            ]
            st.success(f"Book '{selected}' removed!")

    def display_inventory(self):
        st.header("Book Inventory")
        if not self.books:
            st.warning("Inventory is empty.")
        else:
            st.dataframe(pd.DataFrame(self.books), use_container_width=True)

    def low_stock(self):
        st.header("Low Stock Books (< 5)")
        low_stock_list = [b for b in self.books if b["Quantity"] < 5]
        if low_stock_list:
            st.dataframe(
                pd.DataFrame(low_stock_list), use_container_width=True
            )
        else:
            st.info("No low stock books.")

    def inventory_analytics(self):
        st.header("Inventory Analytics")
        if not self.books:
            st.warning("No data available.")
            return

        df = pd.DataFrame(self.books)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Books", int(df["Quantity"].sum()))
        col2.metric(
            "Total Value", f"₹{(df['Price'] * df['Quantity']).sum():,.2f}"
        )
        col3.metric("Average Price", f"₹{df['Price'].mean():.2f}")

        quantities = np.array(df["Quantity"])
        m1, m2, m3 = st.columns(3)
        m1.metric("Max Stock", int(np.max(quantities)))
        m2.metric("Min Stock", int(np.min(quantities)))
        m3.metric("Avg Stock", f"{np.mean(quantities):.2f}")

    def sales_analytics(self):
        st.header("Sales Analytics")
        if not self.sales:
            st.info("No sales data available.")
            return

        df = pd.DataFrame(self.sales)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Books Sold", int(df["Quantity"].sum()))
        col2.metric("Total Revenue", f"₹{df['Total'].sum():,.2f}")
        col3.metric(
            "Best Seller", df.groupby("Title")["Quantity"].sum().idxmax()
        )

        st.dataframe(df, use_container_width=True)

    def save_inventory(self):
        st.header("Save Inventory")
        if not self.books:
            st.warning("No data to save.")
            return

        csv = pd.DataFrame(self.books).to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Inventory CSV",
            csv,
            "book_inventory.csv",
            mime="text/csv",
        )

    def save_sales(self):
        st.header("Save Sales")
        if not self.sales:
            st.warning("No data to save.")
            return

        csv = pd.DataFrame(self.sales).to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Sales CSV", csv, "book_sales.csv", mime="text/csv"
        )

    def sales_chart(self):
        st.header("Sales Chart")
        if not self.sales:
            st.info("No sales data available.")
            return

        df = pd.DataFrame(self.sales)
        sales_data = df.groupby("Title")["Quantity"].sum()

        fig, ax = plt.subplots(figsize=(8, 4))
        sales_data.plot(kind="bar", ax=ax, color="skyblue")
        ax.set_title("Book-wise Sales")
        ax.set_xlabel("Title")
        ax.set_ylabel("Quantity Sold")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

    def inventory_chart(self):
        st.header("Inventory Chart")
        if not self.books:
            st.warning("No inventory data available.")
            return

        df = pd.DataFrame(self.books)
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(data=df, x="Title", y="Quantity", ax=ax, palette="Blues_d")
        ax.set_title("Book Inventory Levels")
        ax.set_xlabel("Title")
        ax.set_ylabel("Quantity")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

    def run(self):
        st.title("📚 Bookstore Inventory & Analytics System")

        options = {
            "1. Display Inventory": self.display_inventory,
            "2. Add Book": self.add_book,
            "3. Update Inventory": self.update_inventory,
            "4. Remove Book": self.remove_book,
            "5. Record Sale": self.record_sale,
            "6. Low Stock Books": self.low_stock,
            "7. Inventory Analytics": self.inventory_analytics,
            "8. Sales Analytics": self.sales_analytics,
            "9. Save Inventory Dataset": self.save_inventory,
            "10. Save Sales Dataset": self.save_sales,
            "11. Show Sales Chart": self.sales_chart,
            "12. Show Inventory Chart": self.inventory_chart,
        }

        choice = st.sidebar.selectbox("Menu", list(options.keys()))
        options[choice]()


if __name__ == "__main__":
    app = Bookstore()
    app.run()
