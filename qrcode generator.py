import qrcode
data = input("Enter the text or url for the qr code: ")
image = qrcode.make(data)
image.save("qrcodeimage.png")

