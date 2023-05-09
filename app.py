import qrcode

# Define the data you want to encode in the QR code
data = "MPESA:+254798055201"

# Create a QR code instance with the data
qr = qrcode.QRCode(version=None, box_size=10, border=4)
qr.add_data(data)

# Generate the QR code image as a PNG file
img = qr.make_image(fill_color="black", back_color="white")
img.save("mpesa_qr.png")
