# 📚 Bookstore Inventory and Analytics System

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical-013243.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Data-3776AB.svg)](https://seaborn.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"Quality is our Motto."** — *Shaping "skills" for "scaling" higher...!!!*

An end-to-end Python-based management and data analytics platform designed for bookstore owners. This system integrates Object-Oriented Programming (OOP), numerical computing, data manipulation, and high-level visual data insights to streamline inventory tracking and analyze store business performance.

---

## 📋 Table of Contents
- [Project Objective](#-project-objective)
- [Problem Statement](#-problem-statement)
- [Features & System Capabilities](#-features--system-capabilities)
- [System Architecture & OOP Design](#-system-architecture--oop-design)
- [Dataset Specifications](#-dataset-specifications)
- [Visual Analytics & Insights](#-visual-analytics--insights)
- [Installation & Requirements](#-installation--requirements)
- [Usage & Example Workflow](#-usage--example-workflow)
- [Submission Checklist](#-submission-checklist)

---

## 🎯 Project Objective

The goal of this project is to build a robust Python application that handles basic inventory operations, conducts statistical sales analysis, and renders clear data visual charts. 

The project incorporates:
1. **Control Structures & Input Validation** (Loops, Conditionals, Error Handling)
2. **Object-Oriented Programming (OOP)** (Modular design using classes & methods)
3. **NumPy** (Numerical calculations, growth rates, mean metrics)
4. **Pandas** (CSV data processing, grouping, aggregation)
5. **Matplotlib & Seaborn** (Data visual reports)

---

## ❓ Problem Statement

Bookstore owners frequently struggle with manual stock tracking, inefficient sales logs, and a lack of data-driven insights into customer buying behavior. 

The **Bookstore Inventory and Analytics System** solves this by offering an automated solution to:
* Manage real-time inventory levels cleanly.
* Calculate revenue metrics automatically.
* Visualize sales trends by genre, author, and time period to optimize stock replenishment.

---

## ✨ Features & System Capabilities

### 1. Inventory Control (Low Weightage)
* Add, update, and remove stock items gracefully.
* Input validation ensures prices and quantities cannot be negative or invalid numbers.

### 2. OOP Architecture (Medium Weightage)
* Encapsulates all management logic within a reusable `Bookstore` class.
* Includes specialized methods for inventory modification, transaction logging, and summary generation.

### 3. Numerical & Statistical Analysis (Medium Weightage)
* **NumPy Calculations:** Rapid computations of total revenue, mean unit price, and sales growth rates.
* **Pandas Data Processing:** Automated cleaning, missing value handling, grouping, and filtering across data files.

### 4. Visual Data Analytics (High Weightage)
* Multi-chart plotting engine providing visual reports to help management make data-driven decisions.

---
## video
[![Play Video](https://img.shields.io/badge/▶%20Play-Video-success?style=for-the-badge)](https://drive.google.com/file/d/1DLl20xGPpQ72SVOb-ehCRyiAsJEVnF0y/view?usp=sharing)

---

## 🏗️ System Architecture & OOP Design

The system relies on a central `Bookstore` class structured as follows:

```python
class Bookstore:
    def __init__(self, inventory_file, sales_file):
        """Initializes the bookstore with inventory and sales data paths."""
        pass

    def add_book(self, title, author, genre, price, quantity):
        """Adds a new book record after validating inputs (Price > 0, Quantity > 0)."""
        pass

    def update_inventory(self, title, quantity):
        """Updates the available stock quantity for an existing book title."""
        pass

    def record_sale(self, title, quantity):
        """Deducts sold units from inventory and records sale metrics into sales history."""
        pass

    def generate_report(self):
        """Summarizes key metrics across stock status and historical sales revenue."""
        pass
