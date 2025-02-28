from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class QRCodeInfo():
    """
    Define the information for qr code.

    Atributes:
        __info (str): The information to store in the QR code.
        __imageName (str): The name of the QR code image.
        __fillColor (str): The fill color of the QR code.
        __backColor (str): The back color of the QR code.
        __logoPath (str): The path of the logo to be inserted in the QR code.
        __imagePath (str): The path of the resulting image.
    """

    default_values = {
        "info": "Text example", 
        "imageName": "example", 
        "fillColor": "000000", 
        "backColor": "ffffff",
        "logoPath": "test-logo/icon-dog.png"
    }

    __info: str = field(default=default_values['info'])
    __image_name: str = field(default=default_values['imageName'])
    __fill_color: str = field(default=default_values['fillColor'])
    __back_color: str = field(default=default_values['backColor'])
    __logo_path: str = field(default=default_values['logoPath'])
    __image_path: Path = field(init=False)


    def __post_init__(self):
        """Determines the values of the attributes definitely. """

        if not self.__info: self.__info = self.default_values['info']
        if not self.__image_name: self.__image_name = self.default_values['imageName']
        if not self.__fill_color: self.__fill_color = self.default_values['fillColor']
        if not self.__back_color: self.__back_color = self.default_values['backColor']

        self.__fill_color = f"#{self.__fill_color}"
        self.__back_color = f"#{self.__back_color}"


        qrcodes_dir = Path.home() / "QR_Codes"
        qrcodes_dir.mkdir(exist_ok=True)

        self.__image_path = qrcodes_dir / f"{self.__image_name}.png"
    
    def get_info(self) -> dict[str, str]:
        """Returns a dictionary with the necesary qr code information. """
        
        return dict(
            info=self.__info,
            fillColor=self.__fill_color,
            backColor=self.__back_color,
            imagePath=self.__image_path,
            logoPath=self.__logo_path
        )
    

if __name__ == '__main__':
    qrcode_info = QRCodeInfo()
    print(qrcode_info.get_info())