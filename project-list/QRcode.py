import qrcode
img_save = input("Enter The Name of File: ")
def generator_qrcode(text):

    qr = qrcode.QRCode(
         version = 1,
         error_correction = qrcode.constants.ERROR_CORRECT_L,
         box_size = 12,
         border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_save + ".png")

URL = input("Enter The URL= ")
generator_qrcode(URL)