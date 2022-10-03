# pip install ConfigObj
# pip install beautifulsoup4
# pip install requests
# pip install python-telegram-bot
# pip install opencv-python


from configobj import ConfigObj
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import requests
import telegram
import cv2
import os

config_last_date_event = ConfigObj("last_date_event.properties")
config = ConfigObj("config.properties")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}


link_qr_test = 'http://nikekichijoji.jp/blog/2022/09/0926qr.jpg'

print('HELLO')


def decode_qr(url):
    with open('qr.jpg', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

    img = cv2.imread('qr.jpg')
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)
    print('QR VALUE', value)
    os.remove('qr.jpg')
    return value


def send_event_message(message):
    try:
        telegram_notify = telegram.Bot(config['TELE_TOKEN'])

        telegram_notify.send_message(chat_id=config['TELE_CHAT_ID'], text=message,
                                     parse_mode='Markdown')
    except Exception as ex:
        print(ex)


def str_config_2_date(src):
    target = datetime.strptime(src, '%m.%d,%Y').date()
    return target


def modify_qr_value(qr_value):
    arr = qr_value.split('?')
    return arr


def nike_harajuku():
    now = datetime.today()
    now_japan = (now + timedelta(hours=2)).date()
    print('----------------> START NIKE HARAJUKU<------------------', (now + timedelta(hours=2)).time())
    link = 'http://nikeharajuku.jp/blog/index.php'
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    date_soup_on_web = soup.find(class_="edate").text
    date_on_web = datetime.strptime(date_soup_on_web, '%m.%d,%Y').date()

    if (now_japan - date_on_web).days == 0:
        print('********** ĐANG CÓ EVENT **********')
        if (now_japan - str_config_2_date(config_last_date_event['NIKE_HARAJUKU'])).days < 0:
            value_qr = decode_qr(link_qr_test)
            if modify_qr_value(value_qr)[1]:
                send_event_message('Event Nike Harajuku: ', + now_japan.strftime("%d/%m/%Y"))
                send_event_message(modify_qr_value(value_qr)[1])
                config_last_date_event['NIKE_HARAJUKU'] = date_soup_on_web
                config_last_date_event.write()
    else:
        print('*********** HIỆN TẠI CHƯA CÓ EVENT ************')
    print('----------------> END NIKE HARAJUKU <------------------')


def nike_osaka():
    now = datetime.today()
    now_japan = (now + timedelta(hours=2)).date()
    print('----------------> START NIKE OSAKA<------------------', (now + timedelta(hours=2)).time())
    link = 'http://nikeosaka.jp/blog/'
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    date_soup_on_web = soup.find(class_="date").text
    date_on_web = datetime.strptime(date_soup_on_web, '%m.%d,%Y').date()

    if (now_japan - date_on_web).days == 0:
        print('********** ĐANG CÓ EVENT **********')
        if (now_japan - str_config_2_date(config_last_date_event['NIKE_OSAKA'])).days < 0:
            value_qr = decode_qr(link_qr_test)
            if modify_qr_value(value_qr)[1]:
                send_event_message('Event Nike OSAKA: ', + now_japan.strftime("%d/%m/%Y"))
                send_event_message(modify_qr_value(value_qr)[1])
                config_last_date_event['NIKE_OSAKA'] = date_soup_on_web
                config_last_date_event.write()
    else:
        print('*********** HIỆN TẠI CHƯA CÓ EVENT ************')
    print('----------------> END NIKE OSAKA<------------------')


def nike_kichijoji():
    now = datetime.today()
    now_japan = (now + timedelta(hours=2)).date()
    print('----------------> START NIKE KICHIJOJI<------------------', (now + timedelta(hours=2)).time())
    link = 'http://nikekichijoji.jp/blog/'
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    date_soup_on_web = soup.find(class_="date").text
    date_on_web = datetime.strptime(date_soup_on_web, '%m.%d,%Y').date()

    if (now_japan - date_on_web).days == 0:
        print('********** ĐANG CÓ EVENT **********')
        if (now_japan - str_config_2_date(config_last_date_event['NIKE_KICHIJOJI'])).days < 0:
            value_qr = decode_qr(link_qr_test)
            if modify_qr_value(value_qr)[1]:
                send_event_message('Event Nike KICHIJOJI: ', + now_japan.strftime("%d/%m/%Y"))
                send_event_message(modify_qr_value(value_qr)[1])
                config_last_date_event['NIKE_KICHIJOJI'] = date_soup_on_web
                config_last_date_event.write()
    else:
        print('*********** HIỆN TẠI CHƯA CÓ EVENT ************')
    print('----------------> END NIKE KICHIJOJI<------------------')


def nike_fukuoka():
    now = datetime.today()
    now_japan = (now + timedelta(hours=2)).date()
    print('----------------> START NIKE FUKUOKA<------------------', (now + timedelta(hours=2)).time())
    link = 'http://nikefukuoka.jp/'
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    date_soup_on_web = soup.find(class_="date").text
    date_on_web = datetime.strptime(date_soup_on_web, '%m.%d,%Y').date()

    if (now_japan - date_on_web).days == 0:
        print('********** ĐANG CÓ EVENT **********')
        if (now_japan - str_config_2_date(config_last_date_event['NIKE_FUKUOKA'])).days < 0:
            value_qr = decode_qr(link_qr_test)
            if modify_qr_value(value_qr)[1]:
                send_event_message('Event Nike FUKUOKA: ', + now_japan.strftime("%d/%m/%Y"))
                send_event_message(modify_qr_value(value_qr)[1])
                config_last_date_event['NIKE_FUKUOKA'] = date_soup_on_web
                config_last_date_event.write()
    else:
        print('*********** HIỆN TẠI CHƯA CÓ EVENT ************')
    print('----------------> END NIKE FUKUOKA<------------------')


def main():
    while True:
        try:
            nike_harajuku()
        except Exception as e:
            print(e)
            pass

        try:
            nike_osaka()
        except Exception as e:
            print(e)
            pass

        try:
            nike_kichijoji()
        except Exception as e:
            print(e)
            pass

        try:
            nike_fukuoka()
        except Exception as e:
            print(e)
            pass

        time.sleep(180)


if __name__ == "__main__":
    main()