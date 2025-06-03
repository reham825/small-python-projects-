import qrcode
qr = qrcode.QRCode(box_size=10, border= 5)
data = input("enter the text or URL for the QR code: ")
fileName = input ("enter the filename: ")
qr.add_data(data)
qr.make(fit =True)
image = qr.make_image(fill_color= "red", back_color="black")
image.save(fileName )
# image = qrcode.make(data)
#
# print(f"QR code saved as {fileName}.")


