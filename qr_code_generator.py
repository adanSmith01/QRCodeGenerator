from dataclasses import dataclass, field
from PIL import Image
import qrcode.constants
from qr_code_info import QRCodeInfo
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
    __image_name: str = field(default=None)
    __fill_color: str = field(default=None)
    __back_color: str = field(default=None)
    __qrcode_info: dict[str, str] = field(init=False)
    logo_path: str = field(default=None)

    def __post_init__(self) -> None:
        info = QRCodeInfo(self.__info, self.__image_name, self.__fill_color, self.__back_color, self.logo_path)
        self.__qrcode_info = info.get_info()
        
    
    def __add_logo(self, logo_path:str, image_code: Image) -> None:
        """
        Adds the specified logo into the QR code.

        Args:
            logo_path (str): The path of the logo to be inserted in the QR code
            image_code (Image): The QR code image proccesed
        
        """

        logo = Image.open(logo_path)
        logo.convert('RGBA')
        image_code.convert('RGBA')
        logo_size = (logo.size[0] // 4, logo.size[1] // 4)
        logo = logo.resize(logo_size, Image.Resampling.LANCZOS)
            
        pos = ((image_code.size[0] - logo.size[0]) // 2, (image_code.size[1] - logo.size[1]) // 2)
        image_code.paste(logo, pos)
        logo.close()

    def generate(self) -> None:
        """ Generates the QR code image from the specified information. """
       
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=15,
            border=4
        )

        qr.add_data(self.__qrcode_info['info'])
        qr.make()
        img = qr.make_image(fill_color=self.__qrcode_info['fillColor'], back_color=self.__qrcode_info['backColor']).get_image()

        if(self.__qrcode_info['logoPath'] is not None):
            self.__add_logo(self.__qrcode_info['logoPath'], img)
        
        img.save(self.__qrcode_info['imagePath'])


if __name__ == '__main__':
    qrcode_gen = QRCodeGenerator()
    qrcode_gen.generate()
