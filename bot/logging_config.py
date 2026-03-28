import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

def setup_logging():
    logging.basicConfig(
        filename="logs/trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )