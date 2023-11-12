import pyqrcode
s="Salman"
url=pyqrcode.create(s)
url.svg("qr.svg",scale=8)


