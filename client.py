from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET")
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def get_client(self):
        return self.client