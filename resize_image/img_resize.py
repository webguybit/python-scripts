from PIL import Image
import PIL
import os
import glob

# image_file = '/media/webguy/ubstrg/permitted_storage/VSCODE_GIT/GUK-EYE-HOSPITAL/static/images/background/admin_login.jpg'
image_file = './c1_admin.jpg'


picture = Image.open(image_file)

picture.save('./c2_admin.jpg', optimize=True,quality=5)