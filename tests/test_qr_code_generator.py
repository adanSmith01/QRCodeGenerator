from source.qr_code_generator import QRCodeGenerator
from pathlib import Path
from PIL import Image, ImageChops
import pytest


class TestQRCodeGenerator:
    
    @pytest.mark.parametrize("info, image_name", [
        ("https://example.com", "example"), 
        ("https://www.google.com/", "google")
    ])
    def test_generate_qrcode_without_logo(self, info, image_name):
        
        qrcode_gen = QRCodeGenerator(info, image_name)
        qrcode_gen.generate()

        image_path = Path.home() / "QR_Codes" / f"{image_name}.png"

        assert Path.exists(image_path)

        Path.unlink(image_path)
        

    @pytest.mark.parametrize("info, image_name, logo", [
        ("https://example.com", "example", "logos/icon-dog.png"), 
        ("https://www.google.com/", "google", "logos/icon-google.jpg")
    ])
    def test_generate_qrcode_with_logo(self, info, image_name, logo):
        qrcode_gen_without_logo = QRCodeGenerator(info, image_name+"_1")
        qrcode_gen_with_logo = QRCodeGenerator(info, image_name+"_2", logo_path=logo)
        qrcode_gen_without_logo.generate()
        qrcode_gen_with_logo.generate()

        image_path_1 = Path.home() / "QR_Codes" / f"{image_name}_1.png"
        image_path_2 = Path.home() / "QR_Codes" / f"{image_name}_2.png"

        assert Path.exists(image_path_1)
        assert Path.exists(image_path_2)

        image_1 = Image.open(image_path_1)
        image_2 = Image.open(image_path_2)

        assert ImageChops.difference(image_1, image_2).getbbox() is not None

        image_1.close()
        image_2.close()

        Path.unlink(image_path_1)
        Path.unlink(image_path_2)

        

    


    