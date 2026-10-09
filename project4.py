import qrcode
data=input("Enter website name or URL:")
filename=input("Enter the name of the file:")
qr=qrcode.QRCode(box_size=20,border=10)
qr.add_data(data)
image=qr.make_image(fill='black',back_color='white')
image.save(filename)
print(filename)
