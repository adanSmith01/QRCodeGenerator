import string
from pathlib import Path
from QRCodeInfo import QRCodeInfo
from QRCodeGenerator import QRCodeGenerator
from PIL import Image

HEX_CODE_LEN: str = 7

while True:
    info = input("Enter the information to be stored in the QR code: ")
    if info == "": print("Information cannot be null")
    else: break

while True:
    imageName = input("QR code image name: ")
    if imageName == "": print("Imagen name cannot be null")
    else: break

while True:
    fillColorHex = input("Enter fill color (hexadecimal code) or press ENTER: ")
    if fillColorHex == "" or (len(fillColorHex) == HEX_CODE_LEN and all(c in string.hexdigits for c in fillColorHex)): break

while True:
    backColorHex = input("Enter background color (hexadecimal code) or press ENTER: ")
    if backColorHex == "" or (len(backColorHex) == HEX_CODE_LEN and all(c in string.hexdigits for c in backColorHex)): break

while True:
    logo_path = input("Enter the absolute path of the logo image file. If you do not want a logo, press ENTER: ")

    if not logo_path:
        break
    
    logo_path.replace("'\'", "'\\'")

    try:
        with Image.open(logo_path) as img:
            img.verify()
        
        break
    except IOError:
        print("Image not exist or not valid")


try: 
    if logo_path:
        qrCodeInfo = QRCodeInfo(info.strip("\n"), imageName.strip("\n"), fillColorHex.strip("\n"), backColorHex.strip("\n"), Image.open(logo_path))
    else:
        qrCodeInfo = QRCodeInfo(info.strip("\n"), imageName.strip("\n"), fillColorHex.strip("\n"), backColorHex.strip("\n"))

    generator = QRCodeGenerator(qrCodeInfo.getInfo())
    generator.generate()
except ValueError as e:
    print(f"Message: {e}")