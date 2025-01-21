from dataclasses import dataclass
from PIL import Image
import qrcode.constants
import QRCodeInfo
import qrcode

@dataclass
class QRCodeGenerator():
    __qrCodeInfo: dict[str, str]

    def __post_init__(self):
        if not isinstance(self.__qrCodeInfo, dict):
            raise ValueError("The qr code information is not valid.")
        
    
    def __add_logo(self, logo:Image, imageCode: Image):
        logo.convert('RGBA')
        imageCode.convert('RGBA')

        logo_size = (logo.size[0] // 4, logo.size[1] // 4)
        logo = logo.resize(logo_size, Image.Resampling.LANCZOS)
            
        pos = ((imageCode.size[0] - logo.size[0]) // 2, (imageCode.size[1] - logo.size[1]) // 2)
        imageCode.paste(logo, pos)

    def generate(self) -> None:
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=15,
            border=4
        )

        qr.add_data(self.__qrCodeInfo['info'])
        qr.make()
        img = qr.make_image(fill_color=self.__qrCodeInfo['fillColor'], back_color=self.__qrCodeInfo['backColor']).get_image()

        if(self.__qrCodeInfo['logo'] is not None):
            self.__add_logo(self.__qrCodeInfo['logo'], img)
            self.__qrCodeInfo['logo'].close()
        
        img.save(self.__qrCodeInfo['imagePath'])


if __name__ == '__main__':
    Logo = Image.open(f"test-logo/icon-dog.png")
    qrCodeInfo = QRCodeInfo.QRCodeInfo(logo=Logo)
    qrCodeGenerator = QRCodeGenerator(qrCodeInfo.getInfo())
    
    qrCodeGenerator.generate()
