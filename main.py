import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=9,
)

data = "https://github.com/Youniq1"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill= 'black', back_color='white')
img.save('Github Repository QR Code.png')
