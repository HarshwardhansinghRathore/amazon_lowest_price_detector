import requests
import bs4
import smtplib
import os

product_URL = 'https://www.amazon.in/Oculus-Advanced-All-One-Virtual/dp/B08F7PTF54/ref=sr_1_1?crid=M1LRYZHEDPPJ&keywords=oculus+quest+2&qid=1637137798&qsid=260-9723480-6398813&sprefix=ocul%2Caps%2C328&sr=8-1&sres=B08F7PTF54%2CB08F7PTF53%2CB07B4NLKKF%2CB07R969TWG%2CB07PRDGYTW%2CB08P3JK89F%2CB08M9R5ZHY%2CB076CWS8C6%2CB08VHFCFXZ%2CB08MW3SBDK%2CB08VHGR4RM%2CB08VHG7NV3%2CB073X8N1YW%2CB08P8P54Y8%2CB07PTMKYS7%2CB08YNY9YGZ&srpt=VIRTUAL_REALITY_HEADSET'
headers = {
    "Accept-Language": 'en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

response = requests.get(url=product_URL, headers=headers)
raw_text = response.text
html_code = bs4.BeautifulSoup(raw_text, 'lxml')
raw_price = html_code.find(name='span', class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text()
print(raw_price)
price_str = raw_price.split('₹')[1].split('.')[0]
print(price_str)
current_product_price = int(price_str.replace(',', ''))
minimum_price_for_buying = 50000
if current_product_price <= minimum_price_for_buying:
    email = 'hr1566027@gmail.com'
    app_pass_w = os.environ['PASSWORD']
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=email, password=app_pass_w)
    connection.sendmail(from_addr=email, to_addrs='hrathore076@gmail.com', msg=f'Subject:low product price alert\n\n the product which you wish to buy has a new price as low as {price_str} which is less than your limit')
    connection.close()
