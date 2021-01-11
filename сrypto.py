from requests import Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '2'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'be507e97-4ec8-4267-b5b9-f4fd6178311f'
}


def create_data_string(data):
    return '```' + "\nid -> {}, cryptocurrency -> {},\n price -> {} USD" \
                   "\n last_updated -> {}".format(data['data'][0]['id'],
                                                  data['data'][0]['name'],
                                                  data['data'][0]['quote']['USD']['price'],
                                                  data['data'][0]['last_updated']) + \
           "\nid -> {}, cryptocurrency -> {},\n price -> {} USD " \
           "\n last_updated -> {}\n".format(data['data'][1]['id'],
                                            data['data'][1]['name'],
                                            data['data'][1]['quote']['USD']['price'],
                                            data['data'][1]['last_updated']) + '```'


def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)


def get_data_json():
    # with open('data.json', 'r') as f:
    #     data = json.loads(f.read())

    # if time_to_request >= 5 min
    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # # else data = latest_data
    save_data(data)

    return create_data_string(data)
