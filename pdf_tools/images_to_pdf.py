from PIL import Image
import os; os.chdir(r'C:\Users\user\path')

image_1 = Image.open("1.jpg")
image_2 = Image.open("2.jpg")

im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')

image_list = [im_2]
im_1.save("output.pdf", save_all=True, append_images=image_list)
