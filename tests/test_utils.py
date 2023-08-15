import pytest

import src.utils


@pytest.fixture
def test_dictionary():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]


right_answer_test_get_executed_data = [{'date': '2019-08-26T10:50:58.294041',
                                        'description': 'Перевод организации',
                                        'from': 'Visa Platinum 1246377376343588',
                                        'id': 441945886,
                                        'operationAmount': {'amount': '31957.58',
                                                            'currency': {'code': 'RUB', 'name': 'руб.'}},
                                        'state': 'EXECUTED',
                                        'to': 'Счет 64686473678894779589'},
                                       {'date': '2018-06-30T02:08:58.425572',
                                        'description': 'Перевод организации',
                                        'from': 'Счет 75106830613657916952',
                                        'id': 939719570,
                                        'operationAmount': {'amount': '9824.07',
                                                            'currency': {'code': 'USD', 'name': 'USD'}},
                                        'state': 'EXECUTED',
                                        'to': 'Счет 11776614605963066702'},
                                       {'date': '2018-03-23T10:45:06.972075',
                                        'description': 'Открытие вклада',
                                        'id': 587085106,
                                        'operationAmount': {'amount': '48223.05',
                                                            'currency': {'code': 'RUB', 'name': 'руб.'}},
                                        'state': 'EXECUTED',
                                        'to': 'Счет 41421565395219882431'},
                                       {'date': '2019-04-04T23:20:05.206878',
                                        'description': 'Перевод со счета на счет',
                                        'from': 'Счет 19708645243227258542',
                                        'id': 142264268,
                                        'operationAmount': {'amount': '79114.93',
                                                            'currency': {'code': 'USD', 'name': 'USD'}},
                                        'state': 'EXECUTED',
                                        'to': 'Счет 75651667383060284188'}]

right_answer_test_get_last_values = [{'date': '2019-08-26T10:50:58.294041',
                                      'description': 'Перевод организации',
                                      'from': 'Visa Platinum 1246377376343588',
                                      'id': 441945886,
                                      'operationAmount': {'amount': '31957.58',
                                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                                      'state': 'EXECUTED',
                                      'to': 'Счет 64686473678894779589'},
                                     {'date': '2019-04-04T23:20:05.206878',
                                      'description': 'Перевод со счета на счет',
                                      'from': 'Счет 19708645243227258542',
                                      'id': 142264268,
                                      'operationAmount': {'amount': '79114.93',
                                                          'currency': {'code': 'USD', 'name': 'USD'}},
                                      'state': 'EXECUTED',
                                      'to': 'Счет 75651667383060284188'},
                                     {'date': '2018-06-30T02:08:58.425572',
                                      'description': 'Перевод организации',
                                      'from': 'Счет 75106830613657916952',
                                      'id': 939719570,
                                      'operationAmount': {'amount': '9824.07',
                                                          'currency': {'code': 'USD', 'name': 'USD'}},
                                      'state': 'EXECUTED',
                                      'to': 'Счет 11776614605963066702'},
                                     {'date': '2018-03-23T10:45:06.972075',
                                      'description': 'Открытие вклада',
                                      'id': 587085106,
                                      'operationAmount': {'amount': '48223.05',
                                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                                      'state': 'EXECUTED',
                                      'to': 'Счет 41421565395219882431'}]


def test_get_executed_data(test_dictionary):
    assert src.utils.get_executed_data(test_dictionary) == right_answer_test_get_executed_data


def test_get_last_values():
    assert src.utils.get_last_values(right_answer_test_get_executed_data, 5) == right_answer_test_get_last_values


def test_get_format_date():
    assert src.utils.get_format_date('2018-03-23T10:45:06.972075') == '23.03.2018'


def test_get_masked_cardnumber():
    assert src.utils.get_masked_cardnumber('1246377376343588') == '1246 37** **** 3588'
    assert src.utils.get_masked_cardnumber('124637737634358') == 'Номер карты не валиден'


def test_get_masked_billnumber():
    assert src.utils.get_masked_billnumber('75106830613657916952') == '**6952'
    assert src.utils.get_masked_billnumber('7510683061365791695') == 'Номер счета не валиден'


def test_get_masked_message():
    assert src.utils.get_masked_message('Visa Platinum 1246377376343588') == 'Visa Platinum 1246 37** **** 3588'
    assert src.utils.get_masked_message('Счет 75106830613657916952') == 'Счет **6952'
    assert src.utils.get_masked_message("MasterCard 7158300734726758") == 'MasterCard 7158 30** **** 6758'
