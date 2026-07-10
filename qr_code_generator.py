import qrcode

input_data = input("Enter the data you want to encode in QR code: ").strip()
filename = input("Enter the filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(input_data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')
