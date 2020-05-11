# for accesing url from the web
import requests
# Import beautiful soup to genrate or scrapping dat from the web
from bs4 import BeautifulSoup
# Using this for sending email 
import smtplib
# Using to import time for time function
import time

# Url of the  website you want to do the web scrapping
URL = 'https://www.amazon.in/PS4-Slim-console-Free-Games/dp/B07ZFKSP88/ref=sr_1_1?dchild=1&keywords=ps4&qid=1589178127&sr=8-1/'

# header is the user agent which can be found for your pc by going to serach engine and type user agent and copy the heading
headers = {"User-Agent": 'URL'}

# defing a new function which function to check the price
def check_price():
    # page variable to get the url and header
    page = requests.get(URL, headers=headers)
    # for getting the required data from web
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text().replace(',','.')
    converted_price = float(price[0:9])

    print(title.strip())
    print(converted_price) 


    if(converted_price < 17.000):
        send_mail()



# function to send mail
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender mail','Reciever mail')

    subject = "Hey Price fell down"
    body = "Check the link Regards Python bot https://www.amazon.in/PS4-Slim-console-Free-Games/dp/B07ZFKSP88/ref=sr_1_1?dchild=1&keywords=ps4&qid=1589178127&sr=8-1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender email',
        'reciever email',
        msg
    )
    print("Hey email has been sent")

    server.quit()

while True:
    check_price()
    time.sleep(60)    


# if you like this code ping on my github




