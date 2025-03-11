from dataclasses import dataclass, field
from PIL import Image
import qrcode.constants
import qrcode


@dataclass
class QRCodeGenerator():
    """
    The purpose of the class is to generate the QR Code image. 
    
    Atributes:
        __info (str): The information to store in the QR code.
        __image_name (str): The name of the QR code image.
        __fill_color (str): The fill color of the QR code.
        __back_color (str): The back color of the QR code.
        __logo_path (str): The path of the logo to be inserted in the QR code.
        __qrcode_info (dict[str, str]): The information of the QR code
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
        Adds the specified logo within the QR code.

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
        img = qr.make_image(fill_color=self.__qrcode_info['fill_color'], back_color=self.__qrcode_info['back_color']).get_image()

        if(self.__qrcode_info['logo_path'] is not None):
            self.__add_logo(self.__qrcode_info['logo_path'], img)
        
        img.save(self.__qrcode_info['image_path'])


if __name__ == '__main__':
    from qr_code_info import QRCodeInfo

    qrcode_gen = QRCodeGenerator("hola", "saludo_2", logo_path="logos/icon-dog.png")
    qrcode_gen.generate()
else:
    from source.qr_code_info import QRCodeInfo
