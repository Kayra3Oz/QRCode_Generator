import qrcode
import Validator

class Generator:
    def __init__(self, url):
        self.url = url


    def generate(self):

        isValid = Validator.validate(self.url)
        if not isValid:
            print("Invalid URL")
            return -1

        qr = qrcode.QRCode()
        qr.add_data(self.url)
        qr.make()
        img = qr.make_image()
        img.show()
