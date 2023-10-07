import segno
#Segno is Pure Python QR Code generator with no dependencies.

slts_qrcode = segno.make_qr("https://engrabdulaziz.com/company")
slts_qrcode.save(
    "GroupofCompanyQRCodeWeb.png",
    scale=20,
)
