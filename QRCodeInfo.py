from dataclasses import dataclass, field
from PIL import Image
from pathlib import Path

@dataclass
class QRCodeInfo():
    __info: str
    __imageName: str
    __fillColor: str
    __backColor: str
    logo: Image = None
    __imagePath: Path = field(init=False)

    def __post_init__(self):
        if not self.__info or self.__info in ("", " "):
            self.__info = "Text example"

        if not self.__imageName or self.__imageName in ("", " "):
            self.__imageName = "example"

        if not self.__fillColor or self.__fillColor in ("", " "):
            self.__fillColor = "000000"

        if not self.__backColor or self.__backColor in ("", " "):
            self.__backColor = "ffffff"

        self.__fillColor = f"#{self.__fillColor}"
        self.__backColor = f"#{self.__backColor}"

        if not Path.exists(Path(Path.home(), "QR_Codes")):
            Path.mkdir(Path(Path.home(), "QR_Codes"))
        
        self.__imagePath = Path(Path.home(), "QR_Codes", f"{self.__imageName}.png")
    
    def getInfo(self) -> dict[str, str]:
        return dict(
            info=self.__info,
            fillColor=self.__fillColor,
            backColor=self.__backColor,
            imagePath=self.__imagePath,
            logo=self.logo
        )
    
if __name__ == '__main__':
    img = Image.open("test-logo/icon-facebook.png")
    qrCodeInfo = QRCodeInfo(logo=img)
    print(qrCodeInfo.getInfo())