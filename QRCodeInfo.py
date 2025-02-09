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
    __imageName: str = field(default=default_values['imageName'])
    __fillColor: str = field(default=default_values['fillColor'])
    __backColor: str = field(default=default_values['backColor'])
    __logoPath: str = field(default=default_values['logoPath'])
    __imagePath: Path = field(init=False)


    def __post_init__(self):
        """Determines the values of the attributes definitely. """

        if not self.__info: self.__info = self.default_values['info']
        if not self.__imageName: self.__imageName = self.default_values['imageName']
        if not self.__fillColor: self.__fillColor = self.default_values['fillColor']
        if not self.__backColor: self.__backColor = self.default_values['backColor']

        self.__fillColor = f"#{self.__fillColor}"
        self.__backColor = f"#{self.__backColor}"


        qrCodesDir = Path.home() / "QR_Codes"
        qrCodesDir.mkdir(exist_ok=True)

        self.__imagePath = qrCodesDir / f"{self.__imageName}.png"
    
    def get_info(self) -> dict[str, str]:
        """Returns a dictionary with the necesary qr code information. """
        
        return dict(
            info=self.__info,
            fillColor=self.__fillColor,
            backColor=self.__backColor,
            imagePath=self.__imagePath,
            logoPath=self.__logoPath
        )
    

if __name__ == '__main__':
    qrCodeInfo = QRCodeInfo()
    print(qrCodeInfo.get_info())