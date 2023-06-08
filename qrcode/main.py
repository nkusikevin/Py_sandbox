import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Prompt the user to enter the data to be encoded in the QR code
data = input("Enter the data to be encoded: ")

# Prompt the user to enter the filename for the QR code image
filename = input("Enter the filename for the QR code image (with extension): ")

# Generate the QR code
generate_qr_code(data, filename)

