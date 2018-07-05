import requests
import keton
from yobit import get_btc
from time import sleep

token = keton.token


#https://api.telegram.org/bot582019256:AAGi-KLHwhu8KBgTN-lYTybVZa_DoPEfy1A/sendmessage?chat_id=378341841&text=hello%20bitch!
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    vv = requests.get(url)
    return vv.json()

def get_message():
    # new message, get update_id each update, записывать в п
    # переменную, сравнивать с update_id последнего эл-та в
    # списке Result

    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text}
        return message
    return None



def send_message(chat_id, text='Wait a second, plz...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    # d = get_updates()

    # with open('updates.json', 'w') as file:
    #    json.dump(d, file,  indent=2, ensure_ascii=False)



    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/ethbtc':
                send_message(chat_id, get_btc())
        else:
            continue

        sleep(2)


if __name__ == '__main__':
    main()