
# сканер штрихкода принимает изображение и возвращает код стрингом
# нужен приемщик изображений, отправщик кода, обработчик изображения

import pytesseract as pt
import os
from pyzbar.pyzbar import decode

from PIL import Image

def main():
	image_path = 'images/barcode.png'
	image = Image.open(image_path)

	# barcode_num = '1301234567890'
	barcode_num = decode(image)
	print(barcode_num)

if __name__ == '__main__':
	main()
