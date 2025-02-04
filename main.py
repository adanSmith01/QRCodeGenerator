from QRCodeGenerator import QRCodeGenerator
from QRCodeInfoController import QRCodeInfoController
from PIL import Image

info: str = QRCodeInfoController.set_info()
imageName: str = QRCodeInfoController.set_image_name()
fillColor: str = QRCodeInfoController.set_fill_color_hex()
backColor: str = QRCodeInfoController.set_background_color_hex()
logoPath: str = QRCodeInfoController.set_logo_path() 

if logoPath:
    generator = QRCodeGenerator(info.strip("\n"), imageName.strip("\n"), fillColor.strip("\n"), backColor.strip("\n"), logoPath.strip("\n"))
else:
    generator = QRCodeGenerator(info.strip("\n"), imageName.strip("\n"), fillColor.strip("\n"), backColor.strip("\n"))

generator.generate()