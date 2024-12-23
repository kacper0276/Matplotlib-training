from PIL import Image

image = Image.open('Zdjęcie WhatsApp 2024-12-23 o 15.52.28_ae9c1dc8.jpg')

mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)

mirrored_image.save('odwrocone.jpg')