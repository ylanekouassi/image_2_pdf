from PIL import Image

file = Image.open("me.jpg")

#file.show()

file_convert = file.convert("RGB")

pdf_file = file.save("me.pdf")