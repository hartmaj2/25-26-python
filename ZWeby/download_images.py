# Example of a program that downloads all the pictures from the list

import requests

PHOTO_NUMBERS = [7, 34, 45, 109, 186, 214, 263, 271, 272, 273, 279, 280, 290, 298, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358] # your list

def get_photo(img_num : int):

    url = f"https://www.promoce.cz/administrace/action/fotos/20080/{img_num:04d}.jpg"
    r = requests.get(url, timeout=20)

    # print(url)
    with open(f"fotky/{img_num:4d}.jpg", "wb") as f:
        f.write(r.content)

for num in PHOTO_NUMBERS:
    get_photo(num)