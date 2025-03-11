from pathlib import Path
from source.qr_code_info import QRCodeInfo
import pytest


@pytest.fixture
def setup_qrcode_info() -> QRCodeInfo:
    info: str = "Valid information"
    image_name: str = "example"
    fill_color: str = "#000000"
    back_color: str = "#ffffff"
    logo_path: str = "logos/icon-dog.png"

    return QRCodeInfo(info, image_name, fill_color, back_color, logo_path)


class TestQRCodeInfo():
    
    @staticmethod
    def test_qr_code_info_valid(setup_qrcode_info: QRCodeInfo) -> None:
        assert setup_qrcode_info.get_info() == {
            "info": "Valid information",
            "fill_color": "#000000",
            "back_color": "#ffffff",
            "image_path": Path.home() / "QR_Codes" / "example.png",
            "logo_path": "logos/icon-dog.png"
        }

        

    
    