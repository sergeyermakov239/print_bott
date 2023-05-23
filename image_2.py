from PIL import Image

image_1 = Image.open(r'C:/Users/telegrambot/Desktop/Python/instruction.jpg')
im_1 = image_1.convert('RGB')
im_1.save(r'C:/Users/telegrambot/Desktop/Python/instruction1.pdf')