import time
import logging
from renderer.ticker import TickerRenderer
from util.utils import convert_currency, load_image_url, align_text, Position


class NFTRenderer(TickerRenderer):
    """
    Renderer for Crypto objects

    Attributes:
        cryptos (list):         List of Crypto objects
    """

    def __init__(self, matrix, canvas, draw, config, data):
        super().__init__(matrix, canvas, draw, config, data)
        self.nfts: list = self.data.nfts

        for nft in self.nfts:
            nft.img = load_image_url(nft.img_url, tuple(self.coords['nft']['logo']['size']))

    def render(self):
        logging.debug("self.nfts: " + str(self.nfts))
        for crypto in self.nfts:
            logging.debug('Fetching data for ' + str(crypto))
            previous_close = crypto.prev_close
            if self.currency != 'USD':  # Convert back to USD for chart calculations purposes
                previous_close = convert_currency(self.currency, 'USD', crypto.prev_close)

            self.clear()
            if self.coords['options']['full_names']:
                self.render_name(crypto.name)
            self.render_image(crypto.img)
            #elif self.coords['options']['history_chart']:
            #    self.render_chart(previous_close, crypto.chart_prices, crypto.value_change)
            self.render_price(str(crypto.price) + " ETH", 'crypto')
            self.render_percentage_change(crypto.pct_change, crypto.value_change)
            self.matrix.SetImage(self.canvas)
            time.sleep(self.config.rotation_rate)

    def render_name(self, name: str):
        x, y = align_text(self.font.getsize(name),
                          self.matrix.width,
                          self.matrix.height,
                          Position.CENTER,
                          Position.TOP)
        self.draw.text((x, y), name, self.text_color, self.font)

    def render_price(self, price: str, ticker_type: str):
        x = align_text(self.font.getsize(price),
                       col_width=self.matrix.width,
                       x=Position(self.coords['crypto']['symbol']['x']))[0]
        x += self.coords['crypto']['symbol']['offset']
        y = self.coords['crypto']['symbol']['y']
        self.draw.text((x, y), price, self.text_color, self.font)
