import argparse
import logging

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        client = BinanceClient().get_client()
        manager = OrderManager(client)

        if order_type == "MARKET":
            response = manager.place_market_order(symbol, side, quantity)
        else:
            price = validate_price(args.price)
            response = manager.place_limit_order(symbol, side, quantity, price)

        print("Order Placed:", response)

    except Exception as e:
        logging.error(str(e))
        print("Error:", str(e))

if __name__ == "__main__":
    main()