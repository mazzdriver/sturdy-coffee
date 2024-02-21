
# сканер штрихкода принимает изображение и возвращает код стрингом
# нужен приемщик изображений, отправщик кода, обработчик изображения

# import pytesseract as pt
# import os
# from pyzbar.pyzbar import decode
# from PIL import Image

appdatabase = 1 #get from JSON 

def main():
	image_path = 'images/barcode.png'
	image = Image.open(image_path)

	barcode_num = '8887290146203'
	# barcode_num = decode(image)
	print(barcode_num)

def get_image(file):
	"""Проверяет файл на пригодность к обработке. Получает файл, возвращает изображение или инструкцию
	"""
	#file proof to image
	#note = 'F* u upload a photo'
	#return image if proof else print(note)
	pass

def format_image():
	"""Форматирует фотографию до пригодной картинки с баркодом. Возвращает пригодную картинку.
	"""
	#find barcode
	#crop it
	#return image with barcode
	pass

def scan():
	"""Обрабатывает пригодную картинку. Возвращает стринг с кодом
	"""
	#scan image with barcode
	#return string barcode
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
	#get_image()
	#format_image()
	#scan()
	#return barcode_num
	pass


if __name__ == '__main__':
	main()
