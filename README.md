# python-qr-code-generator
QR Code Generator (Python)

Description
-----------
This is a simple Python script that generates a QR code from a user-provided URL
and saves the generated image directly to the user's Desktop as "image.png".

The project is useful for quickly creating QR codes for websites,
or any URL.

Requirements
------------
- any coding program
- Python 3.x
- qrcode library

Install dependencies in terminal with:
pip install qrcode[pil]

How It Works
------------
1. The script asks the user to enter a URL.
2. It automatically detects the current user's Desktop path.
3. A QR code is generated from the entered URL.
4. The QR code image is saved as "image.png" on the Desktop.

Usage
-----
Run the script using:
python script.py

Then enter a URL when prompted, for example:
(https://www.linkedin.com/in/sidahmed-rebouh-99501b3a8/)

Output
------
- A file named "image.png" will appear on the Desktop.
- Scanning the QR code opens the entered URL.

Notes
-----
- The Desktop path is detected dynamically, so the script works for any user.
- You can change the filename or customize the QR code size and colors easily.
