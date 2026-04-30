import qrcode

# YouTube linkingiz
url = "https://www.youtube.com/watch?v=hBSf3WdJ-qg"

# QR yaratish
img = qrcode.make(url)

# Saqlash
img.save("last_qrcode.png")

print("QR code tayyor bo‘ldi!")