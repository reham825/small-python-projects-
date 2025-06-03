import qrcode
<<<<<<< HEAD
data = input("enter the text or URL for the QR code: ")
fileName = input ("enter the filename: ")
image = qrcode.make(data)
image.save(fileName )
print(f"QR code saved as {fileName}.")
=======
data = input("Enter the text or url for the qr code: ")
image = qrcode.make(data)
image.save("qrcodeimage.png")

>>>>>>> 5523eefd482ed967212cb36ea099b9b95f792869
