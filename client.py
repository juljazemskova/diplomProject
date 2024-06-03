import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    price_sqft = float(input('Введите price_sqft: '))
    sqft = int(input('Введите sqft: '))
    lotsize = float(input('Введите lotsize: '))
    population = float(input('Введите population: '))
    distance_mean = float(input('Введите distance_mean: '))
    rating_hand = int(input('Введите rating_hand: '))
    schools_count = float(input('Введите schools_count: '))
    r = requests.post('http://localhost:5000/predict', json=[price_sqft, sqft, lotsize, population, distance_mean, rating_hand, schools_count])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)