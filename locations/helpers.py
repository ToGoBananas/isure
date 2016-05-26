YANDEX_KEY = 'AMJgP1cBAAAA8jWkQgIAQ3qoR1vsqGWdjyU6UOdBVoABqSwAAAAAAAAAAABD6NmpANl71MDDKEkQzb7W5jNyHw=='
import requests


def get_address_by_geocode(geocode):
    address = 'https://geocode-maps.yandex.ru/1.x/?apikey='+YANDEX_KEY+'&geocode='+geocode+'&format=json'
    response = requests.get(address)
    address = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
    return address
