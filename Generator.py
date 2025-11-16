import qrcode

class Generator:
    def __init__(self, url):
        self.url = url


    def generate(self):
        qr = qrcode.QRCode()
        qr.add_data(self.url)
        qr.make()
        img = qr.make_image()
        img.show()
