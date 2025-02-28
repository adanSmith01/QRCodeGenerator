from qr_code_generator import QRCodeGenerator
from qr_code_info_controller import QRCodeInfoController


info: str = QRCodeInfoController.validate_info()
image_name: str = QRCodeInfoController.validate_image_name()
fill_color: str = QRCodeInfoController.validate_fill_color()
back_color: str = QRCodeInfoController.validate_background_color()
logo_path: str = QRCodeInfoController.validate_logo_path()


if logo_path:
    generator = QRCodeGenerator(info, image_name, fill_color, back_color, logo_path)
else:
    generator = QRCodeGenerator(info, image_name, fill_color, back_color)

generator.generate()