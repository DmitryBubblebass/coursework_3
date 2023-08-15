import utils

data = utils.get_data('operations.json')

data = utils.get_executed_data(data)

data = utils.get_last_values(data, 5)

for item in data:
    print(utils.prepare_user_msg(item))


