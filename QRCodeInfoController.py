import string
from PIL import Image


HEX_CODE_LEN: str = 7

# Input messages
INFO_INPUT_MESSAGE: str = "Enter the information to be stored in the QR code: "
IMAGE_NAME_INPUT_MESSAGE: str = "QR code image name: "
FILL_COLOR_INPUT_MESSAGE: str = "Enter fill color (hexadecimal code) or press ENTER: "
BACK_COLOR_INPUT_MESSAGE: str = "Enter background color (hexadecimal code) or press ENTER: "
LOGO_PATH_INPUT_MESSAGE: str = "Enter the absolute path of the logo image file. If you do not want a logo, press ENTER: "

# Error messages
INFO_ERROR_MESSAGE: str = "Information cannot be null"
IMAGE_NAME_ERROR_MESSAGE: str = "QR code image name: "
IMAGE_LOGO_ERROR_MESSAGE: str = "Image not exist or not valid"

class QRCodeInfoController():
    
    @staticmethod
    def __set_valid_text(input_message: str, error_message: str) -> str:
        while True:
            text = input(input_message)
            if not text: 
                print(error_message)
            else: 
                return text

    @staticmethod
    def set_info() -> str:
        return QRCodeInfoController.__set_valid_text(INFO_INPUT_MESSAGE, INFO_ERROR_MESSAGE)
        
    @staticmethod
    def set_image_name() -> str:
        return QRCodeInfoController.__set_valid_text(IMAGE_NAME_INPUT_MESSAGE, IMAGE_NAME_ERROR_MESSAGE)

    @staticmethod
    def __set_color_hex(inputMessage: str) -> str:
        while True:
            color = input(inputMessage)
            if color == "" or (len(color) == HEX_CODE_LEN and all(c in string.hexdigits for c in color)): 
                return color

    @staticmethod
    def set_fill_color_hex() -> str:
        return QRCodeInfoController.__set_color_hex(FILL_COLOR_INPUT_MESSAGE)    

    @staticmethod
    def set_background_color_hex() -> str:
        return QRCodeInfoController.__set_color_hex(BACK_COLOR_INPUT_MESSAGE) 

    @staticmethod
    def set_logo_path() -> str:
        while True:
            logoPath = input(LOGO_PATH_INPUT_MESSAGE)

            if not logoPath:
                break
            
            logoPath.replace("'\'", "'\\'")

            try:
                img = Image.open(logoPath)
                img.verify()
                return logoPath
            except IOError:
                print(IMAGE_LOGO_ERROR_MESSAGE)
            finally:
                img.close()
        