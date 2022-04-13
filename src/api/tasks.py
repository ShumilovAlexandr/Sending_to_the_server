import requests

from src.service.celery import app
from src.settings import TOKEN, URL


@app.task(bind=True, default_retry_delay=5 * 60)
def sending_letter(tag, mobile_operator_code, message, date_and_time_of_mailing,
                   date_and_time_of_the_end_of_the_mailing_list):
    head = {'Authorization': f'Bearer {TOKEN}'}
    post_params = {'tag': tag, 'mobile_operator_code': mobile_operator_code, 'message': message,
                   'date_and_time_of_mailing': date_and_time_of_mailing,
                   'date_and_time_of_the_end_of_the_mailing_list': date_and_time_of_the_end_of_the_mailing_list}
    response = requests.post(URL, headers=head, params=post_params)
    return response
