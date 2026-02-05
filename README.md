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
- Python 3.x
- qrcode library
- Pillow library (used internally by qrcode)

Install dependencies with:
pip install qrcode[pil]

Files
-----
- script.py : Main Python script that generates the QR code

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
https://www.linkedin.com/in/your-profile

Output
------
- A file named "image.png" will appear on the Desktop.
- Scanning the QR code opens the entered URL.

Notes
-----
- The Desktop path is detected dynamically, so the script works for any user.
- You can change the filename or customize the QR code size and colors easily.

Author
------
Rebouhtvhardware
