import logging

class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        logging.info("Market order")
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def place_limit_order(self, symbol, side, quantity, price):
        logging.info("Limit order")
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )