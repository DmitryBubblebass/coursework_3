import json


def get_data(data):
    with open(data, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_executed_data(data):
    data = [x for x in data if 'state' in x and x['state'] == "EXECUTED"]
    return data


def get_last_values(data, count_l_v):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_l_v]
    return data


def get_format_date(data):
    new_data = data[0:10].split('-')
    return new_data[2] + '.' + new_data[1] + '.' + new_data[0]


def get_masked_cardnumber(cardnumber):
    if cardnumber.isdigit() and len(cardnumber) == 16:
        return cardnumber[0:4] + ' ' + cardnumber[4:6] + '** **** ' + cardnumber[-4:]
    else:
        return 'Номер карты не валиден'


def get_masked_billnumber(billnumber):
    if billnumber.isdigit() and len(billnumber) == 20:
        return '**' + billnumber[-4:]
    else:
        return 'Номер счета не валиден'


def get_masked_message(message):
    msg_split = message.split(' ')
    # if msg_split[0] == 'Счет':
    #     number_hidden = get_masked_billnumber(msg_split[1])
    if msg_split[1].isdigit() is True:
        if len(msg_split[1]) == 20:
            number_hidden = get_masked_billnumber(msg_split[1])
        elif len(msg_split[1]) == 16:
            number_hidden = get_masked_cardnumber(msg_split[1])
        final_message = msg_split[0] + ' ' + number_hidden
        return final_message

    else:
        if len(msg_split[2]) == 20:
            number_hidden = get_masked_billnumber(msg_split[2])
        elif len(msg_split[2]) == 16:
            number_hidden = get_masked_cardnumber(msg_split[2])
        final_message = msg_split[0] + ' ' + msg_split[1] + ' ' + number_hidden
        return final_message


def prepare_user_msg(item):
    date = get_format_date(item.get('date'))
    desc = item.get('description')

    if 'from' in item:
        from_ = get_masked_message(item.get('from'))
    else:
        from_ = ''
    to_ = get_masked_message(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    currency = item.get('operationAmount').get('currency').get('name')


    return f'{date} {desc}\n{from_} -> {to_}\n{amount} {currency}\n'
