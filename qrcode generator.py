import qrcode
data = input("enter the text or URL for the QR code: ")
fileName = input ("enter the filename: ")
image = qrcode.make(data)
image.save(fileName )
print(f"QR code saved as {fileName}.")


