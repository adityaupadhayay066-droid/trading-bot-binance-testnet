import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load API keys
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        print(f"Placing order for {symbol}...")
        
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order placed successfully: {order}")

        print("\nOrder Request Summary")
        print("----------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        print("\nOrder Response")
        print("----------------------")
        print("Full API Response:", order)

        if "orderId" in order:
            print("Order ID:", order["orderId"])
            print("Status:", order["status"])
            print("Executed Quantity:", order["executedQty"])
        else:
            print("Error: Order was not placed successfully.")
            print("Full Response:", order) 

    except BinanceAPIException as e:
        logging.error(f"Binance API error: {e}")
        print(f"Binance API error: {e}")
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        print(f"Error placing order: {e}")

# Function creation
def get_valid_float(prompt):
    while True:
        try:
            value = input(prompt)
            value = float(value)
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()

    quantity = get_valid_float("Enter quantity: ")

    price = None
    if order_type == "LIMIT":
        price = get_valid_float("Enter price: ")

    place_order(symbol, side, order_type, quantity, price)