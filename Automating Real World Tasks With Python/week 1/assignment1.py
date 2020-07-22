#!/usr/bin/env python3

import os
from PIL import Image

old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'

for image in os.listdir(old_path):
        if '.' not in image[0]:
                img = Image.open(old_path + image)
                img.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
                img.close()