from dataclasses import dataclass, field
from PIL import Image
import qrcode.constants
from QRCodeInfo import QRCodeInfo
import qrcode

@dataclass
class QRCodeGenerator():
    """
    The purpose of the class is to generate the QR Code image. 
    
    Atributes:
        __info (str): The information to store in the QR code.
        __imageName (str): The name of the QR code image.
        __fillColor (str): The fill color of the QR code.
        __backColor (str): The back color of the QR code.
        __logoPath (str): The path of the logo to be inserted in the QR code.
        __qrCodeInfo (dict[str, str]): The information of the QR code
    """
    
    __info: str = field(default=None)
    __imageName: str = field(default=None)
    __fillColor: str = field(default=None)
    __backColor: str = field(default=None)
    __qrCodeInfo: dict[str, str] = field(init=False)
    logoPath: str = field(default=None)

    def __post_init__(self) -> None:
        qrCodeInfo = QRCodeInfo(self.__info, self.__imageName, self.__fillColor, self.__backColor, self.logoPath)
        self.__qrCodeInfo = qrCodeInfo.get_info()
        
    
    def __add_logo(self, logoPath:str, imageCode: Image) -> None:
        """
        Adds the specified logo into the QR code

        Args:
            logoPath (str): The path of the logo to be inserted in the QR code
            imageCode (Image): The QR code image proccesed
        """

        logo = Image.open(logoPath)
        logo.convert('RGBA')
        imageCode.convert('RGBA')
        logo_size = (logo.size[0] // 4, logo.size[1] // 4)
        logo = logo.resize(logo_size, Image.Resampling.LANCZOS)
            
        pos = ((imageCode.size[0] - logo.size[0]) // 2, (imageCode.size[1] - logo.size[1]) // 2)
        imageCode.paste(logo, pos)
        logo.close()

    def generate(self) -> None:
        """Generates the QR code image from the specified information. """
       
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=15,
            border=4
        )

        qr.add_data(self.__qrCodeInfo['info'])
        qr.make()
        img = qr.make_image(fill_color=self.__qrCodeInfo['fillColor'], back_color=self.__qrCodeInfo['backColor']).get_image()

        if(self.__qrCodeInfo['logoPath'] is not None):
            self.__add_logo(self.__qrCodeInfo['logoPath'], img)
        
        img.save(self.__qrCodeInfo['imagePath'])


if __name__ == '__main__':
    qrCodeGenerator = QRCodeGenerator()
    qrCodeGenerator.generate()
