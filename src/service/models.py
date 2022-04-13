from django.db import models
from django.utils import timezone
from .validators import correct_filtering_fields


class Mailing(models.Model):
    """Модель Рассылка с полями"""
    date_and_time_of_mailing = models.DateTimeField(verbose_name='Дата и время рассылки')
    message = models.CharField(max_length=100,
                               verbose_name='Текст сообщения')
    property_filter = models.JSONField(max_length=200, validators=[correct_filtering_fields],
                                       verbose_name='Фильтры свойств клиента')
    date_and_time_of_the_end_of_the_mailing_list = models.\
        DateTimeField(verbose_name='Дата и время окончания рассылки')

    def __str__(self):
        return self.message


class Client(models.Model):
    """Модель Клиент с полями"""
    number_of_phone = models.IntegerField(verbose_name='Номер телефона')
    mobile_operator_code = models.IntegerField(verbose_name='Код оператора')
    tag = models.CharField(max_length=20, verbose_name='Тег')
    time_zone = models.CharField(default=timezone.now, max_length=4,
                                 verbose_name='Часовой пояс')


class Message(models.Model):
    """Модель Сообщение с полями"""
    READY_TO_SENT = 'ready_to_sent',
    SENT = 'sent',
    CANCELLED = 'cancelled'
    SENDING_STATUS_CHOICES = [
        ('READY_TO_SENT', 'Готово к отправке'),
        ('SENT', 'Отправлено'),
        ('CANCELLED', 'Отменено'),
    ]
    date_and_time_of_creation = models.\
        DateTimeField(verbose_name='Дата и время создания')
    sending_status = models.CharField(max_length=20, choices=SENDING_STATUS_CHOICES,
                                      verbose_name='Статус отправки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE,
                                verbose_name='ID рассылки',
                                related_name='id_mailing')
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               verbose_name='ID клиента')
