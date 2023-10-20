import segno
link = input("enter  the url link")
qr = segno.make_qr(link)
qr.save("output.png",scale=20)
