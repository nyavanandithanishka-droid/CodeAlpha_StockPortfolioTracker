# Stock Portfolio Tracker

# Dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:

    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Investment added:", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment Value:", total_investment)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value: " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")