
# сканер штрихкода принимает изображение и возвращает код стрингом
# нужен приемщик изображений, отправщик кода, обработчик изображения

# import pytesseract as pt
import os, json
from pyzbar.pyzbar import decode
from PIL import Image

#appdatabase = 1 #get from JSON 
with open('project_db/data/products.json') as json_data:
	appdatabase = json.load(json_data)
pic = 'images/barcode.png'

def get_image(file):
	"""Проверяет файл на пригодность к обработке. Получает файл, возвращает изображение или инструкцию
	"""
	#file proof to image
	#note = 'F* u upload a photo'
	#return image if proof else print(note)
	image_path = file
	image = Image.open(image_path)
	return image

def format_image():
	"""Форматирует фотографию до пригодной картинки с баркодом. Возвращает пригодную картинку.
	"""
	#find barcode
	#crop it
	#return image with barcode
	pass

def scan(barcode_image):
	"""Обрабатывает пригодную картинку. Возвращает стринг с кодом
	"""

	#barcode_num = '8887290146203'
	barcode_num = decode(barcode_image)
	return barcode_num

def barcode_corrector(barcode_raw):
	"""Обрабатывает полученный от сканера код до чистого набора цифр. Возвращает стринг с кодом
	"""
	#edit barcode_raw to clear string barcode
	#return barcode_num
	pass

def known_product(barcode_num):
	"""Проверяет наличие товара в базе данных сервиса. Переключается в дальнейшие процессы.
	"""
	if barcode_num in appdatabase:
		pass #proceed to script to show product
	else:
		pass #proceed to script to add product and review

def scanner():
	"""Включает сканер, обрабатывает изображение. Возвращает стринг с кодом
	"""
	#format_image()
	barcode_num = scan(get_image(pic))
	for obj in barcode_num:
		data = obj.data
	return data


def main():
		print(scanner())


if __name__ == '__main__':
	main()
