import os
import qrcode

url = input("Enter the URL: ").strip()

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = os.path.join(desktop_path, "image.png")

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Qr Code Generated and saved in desktop!")