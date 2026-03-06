# Binance Futures Testnet Trading Bot

## Overview

This project is a *Python-based trading bot* that interacts with the *Binance Futures Testnet API*.
It allows users to place **MARKET and LIMIT orders** using a simple **Command Line Interface (CLI)**.

The bot demonstrates how Python applications can communicate with the Binance API while following good practices like **secure API key storage, logging, input validation, and error handling**.

This project was created as part of a **Python Developer Internship Application Task**.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Support for **BUY and SELL**
* Command Line input for order parameters
* API request and response logging
* Error handling for invalid inputs and API failures
* Secure API key management using `.env`

---

## Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* logging module

---
---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/adityaupadhayay066-droid/trading-bot.git
cd trading-bot
```

### 2. Install Dependencies

--------------------
pip install -r requirements.txt
---------------------------

### 3. Create `.env` File

Create a `.env` file in the project directory and add your Binance API credentials.
 
 -----------------------------

API_KEY=your api_key
API_SECRET=your api_secret
```

You can generate API keys from the **Binance Futures Testnet**.

---

## How to Run the Bot

Run the Python script:

```
python bot.py
```

You will be asked to enter:

* Symbol (example: BTCUSDT)
* Side (BUY or SELL)
* Order Type (MARKET or LIMIT)
* Quantity
* Price (only required for LIMIT orders)

---

## Example Execution

Example MARKET order:

```
Enter symbol: BTCUSDT
Enter side: BUY
Enter order type: MARKET
Enter quantity: 0.001
```

Example LIMIT order:

```
Enter symbol: BTCUSDT
Enter side: SELL
Enter order type: LIMIT
Enter quantity: 0.001
Enter price: 50000
```

The bot will display:

* Order request summary
* Binance API response
* Order status and executed quantity

---

## Logging

All API requests, responses, and errors are recorded in:

```
trading_bot.log
```

This helps track trading activity and debug issues.

---

## Assumptions

* The user has a **Binance Futures Testnet account**.
* API keys are generated and stored securely in the `.env` file.
* Orders are placed on the **testnet environment**, not real funds.

---

## Future Improvements

* Add additional order types (Stop-Limit / OCO)
* Improve CLI using argparse or Typer
* Add real-time price monitoring
* Build a web interface for the bot

---

## Author

Aditya Upadhayay
