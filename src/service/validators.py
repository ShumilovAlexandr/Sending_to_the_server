def correct_filtering_fields(tag):
    dictionary = {'tag': tag, 'mobile_operator_code': 'mobile_operator_code'}
    try:
        value = dictionary.get('tag', 'mobile_operator_code')
        return value
    except ValueError:
        print('Проверьте правильность введенных данных')
