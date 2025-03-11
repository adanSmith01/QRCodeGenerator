from typing import Generator
from pytest import MonkeyPatch, CaptureFixture
import pytest
from source.qr_code_info_controller import QRCodeInfoController, INFO_ERROR_MESSAGE, IMAGE_NAME_ERROR_MESSAGE, HEX_COLOR_ERROR_MESSAGE, IMAGE_LOGO_ERROR_MESSAGE

class TestQRCodeInfoController:

    def validate_with_valid_input(self, validation_method, valid_input: str, monkeypatch: Generator[MonkeyPatch, None, None]) -> None:
        
        monkeypatch.setattr("builtins.input", lambda _: valid_input)
        result = validation_method()

        assert result == valid_input

    @pytest.mark.parametrize("valid_input", ["Valid Information", "Hello, world"])
    def test_validate_valid_qrcode_info(self, valid_input) -> None:
        self.validate_with_valid_input(QRCodeInfoController.validate_info, valid_input, MonkeyPatch())

    @pytest.mark.parametrize("valid_input", ["example", "proof"])
    def test_validate_valid_qrcode_image_name(self, valid_input) -> None:
        self.validate_with_valid_input(QRCodeInfoController.validate_image_name, valid_input, MonkeyPatch())
    
    @pytest.mark.parametrize("valid_input", ["#000000", "#fffff0"])
    def test_validate_valid_qrcode_fill_color(self, valid_input) -> None:
        self.validate_with_valid_input(QRCodeInfoController.validate_fill_color, valid_input, MonkeyPatch())


    @pytest.mark.parametrize("valid_input", ["#000000", "#ffffff"])
    def test_validate_valid_qrcode_back_color(self, valid_input) -> None:
        self.validate_with_valid_input(QRCodeInfoController.validate_background_color, valid_input, MonkeyPatch())


    @pytest.mark.parametrize("valid_input", ["../logos/icon-dog.png", "../logos/icon-google.jpg"])
    def test_validate_valid_qrcode_logo_path(self, valid_input) -> None:
        self.validate_with_valid_input(QRCodeInfoController.validate_logo_path, valid_input, MonkeyPatch())