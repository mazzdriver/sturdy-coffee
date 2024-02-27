
# сканер штрихкода принимает изображение и возвращает код стрингом
# нужен приемщик изображений, отправщик кода, обработчик изображения

# import pytesseract as pt
import os, json
from pyzbar.pyzbar import decode
from PIL import Image

#appdatabase = 1 #get from JSON 
datafile = 'project_db/data/products.json'
with open(datafile) as json_data:
	appdatabase = json.load(json_data)
pic = 'images/barcode.png'

def get_image(file_path:str):
	"""Проверяет файл на пригодность к обработке. Получает файл, возвращает изображение или инструкцию
	"""
	#file proof to image
	#note = 'F* u upload a photo'
	#return image if proof else print(note)
	image = Image.open(file_path)
	return image

def format_image(raw_img):
	"""Форматирует фотографию до пригодной картинки с баркодом. Возвращает пригодную картинку.
	"""
	#find and mask the barcode on image
	#image_with_barcode = crop(mask(raw_img))
	#return image_with_ barcode
	pass

def decode(barcode_image):
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

def scanner():
	"""Включает сканер, обрабатывает изображение. Возвращает стринг с кодом
	"""
	#format_image()
	barcode_num = decode(get_image(pic))
	for obj in barcode_num:
		data = obj.data
	return data

def get_known_product(barcode:str, datasheet:list):
	"""Обращается к базе данных в поисках товара. Возвращает массив информации о конкретном товаре
	"""
	# call database searching for barcode
	# get product by barcode
	product = list(filter(lambda x:x["barcode"]==barcode,datasheet))
	return product

def known_product(barcode, datasheet):
	"""Проверяет наличие товара в базе данных сервиса. Переключается в дальнейшие процессы.
	"""
	if barcode in datasheet:
		product = get_known_product(barcode, datasheet)
	else:
		
		#proceed to script to add product and review
		pass

def input_new_data():
	"""Помогает в создании новой записи в БД в формате массива. Возвращает массив с информацией к записи.
	"""
	#new_data =[]
	#return new_data
	pass

def add_new(data:dict, datafile):
	"""Вносит новую запись в базу данных.
	"""
	#with open(datafile, 'w') as outfile:
			#json.dump(data, outfile)
	success = False
	#return success
	pass

def main():
		print(scanner())


if __name__ == '__main__':
	main()
