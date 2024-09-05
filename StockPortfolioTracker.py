import yfinance as yf

portfolio = {}

def add_stock(ticker, shares):
    stock = yf.Ticker(ticker)
    info = stock.info
    portfolio[ticker] = {"shares": shares, "price": info['regularMarketPrice'], "name": info['shortName']}

def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
    else:
        print(f"{ticker} not found in portfolio.")

def display_portfolio():
    print("\nYour Stock Portfolio:")
    for ticker, data in portfolio.items():
        print(f"{data['name']} ({ticker}): {data['shares']} shares @ ${data['price']:.2f} per share")

def update_prices():
    for ticker in portfolio:
        stock = yf.Ticker(ticker)
        portfolio[ticker]['price'] = stock.info['regularMarketPrice']

# Main menu for portfolio management
def portfolio_menu():
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Display Portfolio\n4. Update Prices\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            update_prices()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the portfolio tracker
if __name__ == "__main__":
    portfolio_menu()
