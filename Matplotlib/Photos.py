from PIL import Image
from fpdf import FPDF

file1_path = 'Zdjęcie WhatsApp 2024-12-23 o 15.52.29_fad8b491.jpg'
file2_path = 'Zdjęcie WhatsApp 2024-12-23 o 15.52.26_e7ec4a07.jpg'
# Zdjęcie WhatsApp 2024-12-23 o 15.52.25_db669b30.jpg

im1 = Image.open(file1_path)
im2 = Image.open(file2_path)

dpi = 300
a4_width, a4_height = int(8.3 * dpi), int(11.7 * dpi)

def resize_image_to_half_a4(image, a4_width, a4_height):
    target_height = a4_height // 2
    aspect_ratio = image.width / image.height
    target_width = int(target_height * aspect_ratio)
    if target_width > a4_width:
        target_width = a4_width
        target_height = int(target_width / aspect_ratio)
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)

im1_resized = resize_image_to_half_a4(im1, a4_width, a4_height)
im2_resized = resize_image_to_half_a4(im2, a4_width, a4_height)

im1_resized_path = 'im1_resized.jpg'
im2_resized_path = 'im2_resized.jpg'
im1_resized.save(im1_resized_path)
im2_resized.save(im2_resized_path)

pdf = FPDF(unit="pt", format=[a4_width, a4_height])
pdf.add_page()
pdf.image(im1_resized_path, x=(a4_width - im1_resized.width) / 2, y=0, w=im1_resized.width, h=im1_resized.height)
pdf.image(im2_resized_path, x=(a4_width - im2_resized.width) / 2, y=a4_height / 2, w=im2_resized.width, h=im2_resized.height)

output_pdf_path = 'combined_a4_1.pdf'
pdf.output(output_pdf_path)