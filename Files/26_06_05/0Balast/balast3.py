# staci pouzit split s balastem

text = "BBALASTBALASTRBALASTABALASTBALASTBALASTTBALASTBALASTIBALASTBALASTBALASTSLBALASTBALASTBALASTABALASTBALASTVBALASTBALASTA"

found = text.find("BALAST")
while found != -1:
    text = text[:found] + text[found+6:]
    found = text.find("BALAST")
print(text)