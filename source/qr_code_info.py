from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class QRCodeInfo():
    """
    Define the information for qr code.

    Atributes:
        __info (str): The information to store in the QR code.
        __image_name (str): The name of the QR code image.
        __fill_color (str): The fill color of the QR code.
        __back_color (str): The back color of the QR code.
        __logo_path (str): The path of the logo to be inserted in the QR code.
        __image_path (str): The path of the resulting image.
    """

    default_values = {
        "info": "Text example", 
        "image_name": "example", 
        "fill_color": "#000000", 
        "back_color": "#ffffff",
        "logo_path": "logos/icon-dog.png"
    }

    __info: str = field(default=default_values['info'])
    __image_name: str = field(default=default_values['image_name'])
    __fill_color: str = field(default=default_values['fill_color'])
    __back_color: str = field(default=default_values['back_color'])
    __logo_path: str = field(default=default_values['logo_path'])
    __image_path: Path = field(init=False)


    def __post_init__(self):
        """Determines the values of the attributes definitely. """

        if not self.__info: self.__info = self.default_values['info']
        if not self.__image_name: self.__image_name = self.default_values['image_name']
        if not self.__fill_color: self.__fill_color = self.default_values['fill_color']
        if not self.__back_color: self.__back_color = self.default_values['back_color']

        qrcodes_dir = Path.home() / "QR_Codes"
        qrcodes_dir.mkdir(exist_ok=True)

        self.__image_path = qrcodes_dir / f"{self.__image_name}.png"
    
    def get_info(self) -> dict[str, str]:
        """Returns a dictionary with the necesary qr code information. """
        
        return dict(
            info=self.__info,
            fill_color=self.__fill_color,
            back_color=self.__back_color,
            image_path=self.__image_path,
            logo_path=self.__logo_path
        )
    

if __name__ == '__main__':
    qrcode_info = QRCodeInfo()
    print(qrcode_info.get_info())