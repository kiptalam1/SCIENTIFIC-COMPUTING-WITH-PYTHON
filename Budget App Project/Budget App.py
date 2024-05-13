class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

def create_spend_chart(categories):
    # Calculate total withdrawals for each category
    total_withdrawals = {}
    for category in categories:
        total_withdrawals[category.name] = sum(transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0)
    
    # Calculate percentage spent in each category
    total_spent = sum(total_withdrawals.values())
    percentages = {category: int((spent / total_spent) * 100) for category, spent in total_withdrawals.items()}
    
    # Create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}|"
        for category in categories:
            chart += " o " if percentages[category.name] >= i else "   "
        chart += " \n"
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n     "
    
    # Determine the longest category name
    max_length = max(len(category.name) for category in categories)
    
    # Add category names below the chart
    for i in range(max_length):
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n     "
    
    return chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

# Test create_spend_chart function
categories = [food, clothing]
print(create_spend_chart(categories))
