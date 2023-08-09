import json


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_executed_data(data):
    data = [x for x in data if 'state' in x and x['state'] == "EXECUTED"]
    return data


def get_last_values(data, count_l_v):
    data = sorted(data, key=lambda x: x['data'], reverse=True)
    data = data[:count_l_v]
    return data


def get_format_data(data):
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


def get_masked_massage(massage):
    msg_split = massage.split(' ')
    if msg_split[0] == 'Счет':
        number_hidden = get_masked_billnumber(msg_split[1])
    else:
        number_hidden = get_masked_cardnumber(msg_split[1])
    return number_hidden


# def prepare_user_msg(item):
#     date = get_date(item.get('date'))
#     desc = item.get('description')
#     from_ = mask_from_to_msg(item.get('from'))
#     to_ = mask_from_to_msg(item.get('to'))
#     amount = item.get('operationAmount').get('amount')
#     currency = item.get('operationAmount').get('currency').get('name')
#
#     # Переменная from_ может быть пустая, тогда '->' не надо. Если не пусто, то надо
#     if from_:
#         from_ = from_ + ' -> '
#
#     return f'{date} {desc}\n{from_}{to_}\n{amount} {currency}'
