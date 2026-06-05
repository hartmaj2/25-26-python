# idea:
#    stavy: 
#       zahazuji vs. nechavam si
#       prechod mezi stavy kdyz narazim na X

inp = "XEOHGAXZXGHAGXADXEOHGEXEXDGHLAHHHALXJTXLKDGSLEIHCXEHXEHGHOEHLXESLXDHHEELLLHSOEPRASEXOXSLONXKOXGHLHGZEBRAJFDLXNVXFHLHHHLAXALIXSOVANOCXNXHHLOEXKAXHEALLX"
reading_balast = False
out = ""

for c in inp:
    if c == "X":
        reading_balast = not reading_balast
        continue
    if not reading_balast:
        out += c

print(out)