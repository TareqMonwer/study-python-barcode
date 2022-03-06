import barcode
from barcode.writer import ImageWriter
from pathlib import Path


ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
path = Path().cwd() / 'images' / '123456789102.png'
barcode_file = open(path, "wb")
filename = ean.write(barcode_file)
barcode_file.close()
