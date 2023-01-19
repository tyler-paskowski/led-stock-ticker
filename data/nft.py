import json
from dataclasses import dataclass
from datetime import datetime, timedelta

from pytz import timezone

from constants import CRYPTO_LOGO_URL
from data.ticker import Ticker
from data.status import Status
from util.utils import convert_currency
import requests


@dataclass
class NFT(Ticker):
    img_url: str = None

    def initialize(self):
        #super(NFT, self).initialize()
        data = self.get_collection(self.symbol)


        self.yf_ticker = None
        self.name = self.symbol
        self.price = data.get("collection").get("stats").get("floor_price")
        self.prev_close = self.get_prev_close()
        self.value_change = data.get("collection").get("stats").get("one_day_change")
        self.pct_change = f'{100 * float(data.get("collection").get("stats").get("one_day_change")):.2f}%'
        self.chart_prices = [] #self.get_chart_prices()
        self.img_url = "https://i.seadn.io/gcs/files/0d5f1b200a067938f507cbe12bbbabc2.jpg?w=500&auto=format"

    def get_prev_close(self) -> float:
        """
        Fetch the crypto's price 24h ago.
        If currency is not set to USD, convert value to user-selected currency.
        :return: prev_close: Previous day's close price
        :exception TypeError: Inappropriate argument type. Occurs when crypto is not valid.
        """
        data = self.get_collection(self.symbol)
        data.get("collection").get("stats").get("floor_price")
        try:
            return 0.0
            # prices = self.yf_ticker.history(interval='1m', period='2d')
            # today = datetime.now(timezone('Europe/London'))  # Timezone used by yfinance library
            # yesterday = today - timedelta(days=1)
            # yesterday = yesterday.replace(second=0)
            # yesterday = datetime.isoformat(yesterday, sep=' ', timespec='seconds').format('%Y-%m-%d %H:%M:%S%z')
            # prev_close = prices.loc[yesterday].Close
            # if self.currency != 'USD':
            #     prev_close = convert_currency('USD', self.currency, prev_close)
            # return prev_close
        except TypeError:
            self.valid = False
            self.status = Status.FAIL

    def get_collection(self, slug) -> dict:
        url = "https://api.opensea.io/api/v1/collection/" + slug
        response = requests.get(url)
        return response.json()
