#! /usr/bin/env python3

import os 
import requests


BASEPATH_SUPPLIER_TEXT_DES = os.path.expanduser('~') + '/supplier-data/descriptions/'
list_text_files = os.listdir(BASEPATH_SUPPLIER_TEXT_DES)

BASEPATH_SUPPLIER_IMAGE = os.path.expanduser('~') + '/supplier-data/images/'
list_image_files = os.listdir(BASEPATH_SUPPLIER_IMAGE)
list_images = [image_name for image_name in list_image_files if '.jpeg' in image_name]


list = []
for text_file in list_text_files:
	with open(BASEPATH_SUPPLIER_TEXT_DES + text_file, 'r') as f:
		data = {"name":f.readline().rstrip("\n"),
                "weight":int(f.readline().rstrip("\n").split(' ')[0]),
                "description":f.readline().rstrip("\n")}

		for image_file in list_images:
			if image_file.split('.')[0] in text_file.split('.')[0]:
				data['image_name'] = image_file

		list.append(data)
            
for item in list:
    resp = requests.post('http://127.0.0.1:80/fruits/', json=item)
    if resp.status_code != 201:	
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))
