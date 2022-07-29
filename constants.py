"""Constants class"""

# Directories & Files
CONFIG_FILE = 'config/config.json'
LAYOUT_FILE = 'config/layout/w{}h{}.json'
LOG_FILE = 'led-stock-ticker.log'
LOADING_IMAGE = 'assets/img/logo.png'
ERROR_IMAGE = 'assets/img/error.png'

# Software Defaults
DEFAULT_STOCKS = ['TSLA', 'AMZN', 'MSFT']
DEFAULT_CRYPTOS = ['BTC', 'ETH', 'LTC']
DEFAULT_DATE_FORMAT = '%a, %b %d'  # eg. Sun, Jan 5
DEFAULT_FONT_PATH = 'rpi-rgb-led-matrix/fonts/4x6.bdf'
DEFAULT_UPDATE_RATE = 10 * 60  # 10 minutes
DEFAULT_ROTATION_RATE = 10  # 10 seconds
TEXT_SCROLL_DELAY = 0.5  # 0.5 seconds
TEXT_SCROLL_SPEED = 0.1  # 0.1 seconds

# Date/Time Formatting
DATE_FORMATS = [
    '%a, %b %d',  # Sun, Jan 5
    '%B %d',  # January 5
    '%m/%d/%Y',  # MM/DD/YYYY
    '%a, %d %b',  # Sun, 5 Jan
    '%d/%m/%Y',  # DD/MM/YYYY
]
CLOCK_FORMATS = ['12h', '24h']
TWELVE_HOURS_FORMAT = '%I:%M %p'  # eg. 11:38 PM
TWENTY_FOUR_HOURS_FORMAT = '%H:%M'  # eg. 23:38
