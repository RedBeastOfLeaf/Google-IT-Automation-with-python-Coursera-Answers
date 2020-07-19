#!/usr/bin/env python3

import os
from PIL import Image

path = os.path.expanduser('~') + '/supplier-data/images/'
		
for image in os.listdir(path):
	if '.tiff' in image and '.' not in image[0]:
		img = Image.open(path + image)
		img.resize((600, 400)).convert("RGB").save(path + image.split('.')[0] + '.jpeg' , 'jpeg')
		img.close()
