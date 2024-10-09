def main():
    import requests
    import json

    BRA_cities = (
        'belo-horizonte',
        'brasilia',
        'curitiba',
        'fortaleza',
        'porto-alegre',
        'recife',
        'rio-de-janeiro',
        'salvador',
        'sao-paulo'
        )

    cities_dict = {}
    cities_json = {}
    
    input('press any key')

    for city in BRA_cities:
        print(city.replace('-', ' ').title())
        api_url = 'https://api.midway.tomtom.com/ranking/liveHourly/' + 'BRA_' + city
        req =  requests.get(api_url)
        req_json = req.json()
        cities_json[city] = req_json['data']

    try:
        with open('dados/tomtom-data.json', 'r') as file:
            data = json.load(file)
        for city in cities_json.keys:
            data[city].append(cities_json[city])
        with open('dados/tomtom-data.json', 'w') as file:
            json.dump(data, file)
    except:
        with open('dados/tomtom-data.json', 'w') as file:
            json.dump(cities_json, file)
    input('press any key')

if __name__ == '__main__':
    main()