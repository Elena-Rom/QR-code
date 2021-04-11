import png
import pyqrcode
from pyqrcode import QRCode

url = "<url>"

code = pyqrcode.create(url)
code.png('name.png', scale=6)