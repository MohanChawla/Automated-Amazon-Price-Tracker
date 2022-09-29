import requests
import smtplib
from bs4 import BeautifulSoup

EMAIL = "cmchawla94@gmail.com"
PASSWORD = "dummy_text"

ALERT_PRICE = 170
URL = "https://www.amazon.com/dp/B09JL41N9C/ref=fs_a_bt2_us1"
headers = {
    'Accept-Language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    'User-Agent': "cMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
title = soup.find(id="productTitle").get_text().strip()

price = soup.find(name='span', class_='a-offscreen').getText()
price_float = float(price.split("$")[1])

if price_float < ALERT_PRICE:
    msg = f"{title} is now available at {price_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{msg}\n{URL}"
        )
