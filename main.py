# imports first
import os, json
from pyzbar.pyzbar import decode
from PIL import Image

# then variables
datafile = 'project_db/data/products.json'
pic = 'images/barcode.png'

with open(datafile) as json_data:
	appdatabase = json.load(json_data)
image = Image.open(pic)

# then functions
def format_image(raw_img):
	"""Форматирует фотографию до пригодной картинки с баркодом. Возвращает пригодную картинку.
	"""
	#find and mask the barcode on image
	#image_with_barcode = crop(mask(raw_img))
	#return image_with_barcode
	pass

def barcode_decoder(barcode_raw):
	"""Обрабатывает картинку до чистого набора цифр. Возвращает стринг с кодом
	"""
	#edit barcode_raw to clear string barcode
	barcode_num = str(decode(barcode_raw))
	return barcode_num

def get_known_product(barcode:str, datasheet:list):
	"""Обращается к базе данных в поисках товара. Возвращает массив информации о конкретном товаре
	"""
	# call database searching for barcode
	# get product by barcode
	product = list(filter(lambda x:x["barcode"]==barcode,datasheet))
	return product

def known_product(barcode:str, datasheet:list):
	"""Проверяет наличие товара в базе данных сервиса. Переключается в дальнейшие процессы.
	"""
	return barcode in datasheet

def input_new_data():
	"""Помогает в занесении новой записи в БД в формате массива. Возвращает массив с информацией к записи.
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

#main logic
def main():
		barcode = barcode_decoder(format_image(image))
		if known_product(barcode, appdatabase):
			product = get_known_product(barcode, appdatabase)
		else:
			input_new_data()

# and go
if __name__ == '__main__':
	main()
