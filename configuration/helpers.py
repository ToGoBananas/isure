from .models import Currency
from policies.models import PolicyBase
import requests
from xml.etree import ElementTree
import datetime


def get_cbr_info():
    currency = Currency.objects.get_or_create(pk=1)[0]

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=')

    tree = ElementTree.fromstring(response.content)
    for valute in tree:
        valute_id = valute.get('ID')
        if valute_id == 'R01235':
            currency.usd = valute[-1].text.replace(',', '.')
        elif valute_id == 'R01239':
            currency.euro = valute[-1].text.replace(',', '.')

    currency.save()


def get_bordereau(start=None, end=None):
    policies = None
    if not start or not end:
        policies = PolicyBase.objects.filter(created_date=datetime.datetime.today())
    else:
        policies = PolicyBase.objects.filter(created_date__range=(start, end))