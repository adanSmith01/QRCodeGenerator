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
IMAGE_NAME_ERROR_MESSAGE: str = "Image name cannot be null"
HEX_COLOR_ERROR_MESSAGE: str = "Hexadecimal color is invalid"
IMAGE_LOGO_ERROR_MESSAGE: str = "Logo not exist or not valid"

class QRCodeInfoController():
    """A class for to manage the input data. """

    @staticmethod
    def __validate_text(input_message: str, error_message: str) -> str:
        """
        Prompt the user to enter text and validate it.

        This method repeatedly prompts the user to enter text using the provided input prompt.
        If the user enters an empty string, an error message is displayed and the user is 
        prompted again. The method returns the validated text (without any leading or trailing 
        newline characters).

        Args:
            input_message (str): The message displayed to prompt the user for input.
            error_message (str): The message displayed when the user enters invalid input
                                (e.g., an empty string).

        Returns:
            str: The validated text provided by user.

        Raises:
            ValueError: If the user enters an empty string
        """

        while True:
            try:
                text = input(input_message).strip(" ")

                if not text:
                    raise ValueError
                
                return text
            except ValueError:
                print(error_message)
        

    @staticmethod
    def validate_info() -> str:
        """
        Prompt the user to enter the information for the QR code and validate it.

        This method uses `__validate_text` to ensure the user provides valid input.

        Returns:
            str: The validated QR code information, provided by user.
        """

        return QRCodeInfoController.__validate_text(INFO_INPUT_MESSAGE, INFO_ERROR_MESSAGE)
        

    @staticmethod
    def validate_image_name() -> str:
        """
        Prompt the user to enter the image name for the QR code and validate it.

        This method uses `__validate_text` to ensure the user provides valid input.

        Returns:
            str: The validated image name for the QR code, provided by user.
        """

        return QRCodeInfoController.__validate_text(IMAGE_NAME_INPUT_MESSAGE, IMAGE_NAME_ERROR_MESSAGE)


    @staticmethod
    def __validate_hex_color(input_message: str) -> str:
        """
        Prompt the user to enter hexadecimal color and validate it.

        This method repeatedly prompts the user to enter hexadecimal color using the provided input prompt.
        If the user enters a hexadecimal code is not 7 hexadecimal digits long, an error message is displayed 
        and the user is prompted again. The method returns the validated hexadecimal color (without any leading or trailing 
        newline characters).

        Args:
            input_message (str): The message displayed to prompt the user for input.

        Returns:
            str: The validated hexadecimal color.

        Raises:
            ValueError: If the user enters an hexadecimal color is not 7 hexadecimal digits.
        """

        while True:
            
            try:
                color = input(input_message).strip(" ")

                if not color:
                    return ""
                
                if len(color) != HEX_CODE_LEN or color[0] != "#" or not all(c in string.hexdigits for c in color[1:]): 
                    raise ValueError
                
                return color
            except ValueError:
                print(HEX_COLOR_ERROR_MESSAGE)
           

    @staticmethod
    def validate_fill_color() -> str:
        """
        Prompt the user to enter the hexadecimal color for the QR code's fill and validate it.

        This method uses `__validate_hex_color` to ensure the user provides valid input.

        Returns:
            str: The validated hexadecimal color for the QR code's fill, provided by the user.

        """
        return QRCodeInfoController.__validate_hex_color(FILL_COLOR_INPUT_MESSAGE)
           


    @staticmethod
    def validate_background_color() -> str:
        """
        Prompt the user to enter the hexadecimal color for the QR code's background and validate it.

        This method uses `__validate_hex_color` to ensure the user provides valid input.

        Returns:
            str: The validated hexadecimal color for the QR code's background, provided by the user.

        """

        return QRCodeInfoController.__validate_hex_color(BACK_COLOR_INPUT_MESSAGE) 


    @staticmethod
    def validate_logo_path() -> str:
        """
        Prompt the user to enter the logo path for the QR code and validate it. It's optional

        This method repeatedly prompts the user to enter the logo path for the QR code using the provided input prompt.
        If the user enters an logo path that does not correspond to a valid image , an error message is displayed and the user is 
        prompted again. The method returns the validated logo path (without any leading or trailing 
        white space).

        Returns:
            str: The validated logo path, provided by the user.

        Raises:
            IOError: If the user enters an logo path that does not correspond to a valid image.
        """

        while True:

            logo_path = input(LOGO_PATH_INPUT_MESSAGE).strip(" ")

            if not logo_path:
                return ""
            
            try:
                logo_path.replace("'\'", "'\\'")
                img = Image.open(logo_path)
                img.verify()

                return logo_path
            except IOError:
                print(IMAGE_LOGO_ERROR_MESSAGE)
            finally:
                img.close()
        