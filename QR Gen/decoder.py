from PIL import Image
from pyzbar.pyzbar import decode

# <QR Code Image> · image.jpg, image.png, image.gif
result = decode(Image.open('qr.png'))
print(result)