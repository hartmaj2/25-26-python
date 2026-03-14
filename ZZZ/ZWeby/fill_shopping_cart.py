# Example of a program that sends a request and fills a shoping cart with images by numbers from the list

import requests

PHOTO_NUMBERS = [7, 34, 45, 109, 186, 214, 263, 271, 272, 273, 279, 280, 290, 298, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358]          # your list
ACTION_ID = "20080"
ARTICLE_ID = "1810"

URL = "https://www.promoce.cz/cz/response.php"

# the Cookie header string can be found in Inspect -> Network and then looking at some request header
COOKIE = "PHPSESSID=4aegllsc62ej0ladovrvahrbd5"  # paste full Cookie header string from your browser, or keep None to test

s = requests.Session()

if COOKIE:
    s.headers["Cookie"] = COOKIE

for n in PHOTO_NUMBERS:
    data = {
        "insert_action_id": ACTION_ID,
        "all_on_cd": "0",
        "on_cd": "1",
        "insert_article_id": ARTICLE_ID,
        "insert_count": "1",
        "insert_type": "foto",
        "insert_foto_name": f"{n:04d}.jpg",   # 0001.jpg etc.
        # "insert_foto_number": str(n),
    }
    r = s.post(URL, data=data, timeout=20)
    print(n, r.status_code, r.text[:120].replace("\n", " "))
