import pyqrcode

message = "Salman"

url=pyqrcode.create(message)
url.svg("qr.svg",scale=8)


