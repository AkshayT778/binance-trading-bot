# Binance Futures Trading Bot

## Setup

1. Install dependencies
pip install -r requirements.txt

2. Create .env file

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Run MARKET order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Run LIMIT order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000

Logs saved in logs/trading_bot.log