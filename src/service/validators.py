import re

from django.forms import ValidationError

def correct_filtering_fields(tag):
    dictionary = {'tag': tag, 'mobile_operator_code': 'mobile_operator_code'}
    try:
        value = dictionary.get('tag', 'mobile_operator_code')
        return value
    except ValueError:
        print('Проверьте правильность введенных данных')


def correct_number_phone(number_of_phone):
    rule = re.compile(r'^[7]\d{10}$')

    if not rule.search(str(number_of_phone)):
        raise ValidationError('Проверьте правильность введенного номера')
