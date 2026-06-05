# staci pouzit split s balastem

text = "BBALASTBALASTRBALASTABALASTBALASTBALASTTBALASTBALASTIBALASTBALASTBALASTSLBALASTBALASTBALASTABALASTBALASTVBALASTBALASTA"

i = 0
while i < len(text):
    while text[i:i+6] == "BALAST":
        text = text[:i] + text[i+6:]
    i += 1

print(text)