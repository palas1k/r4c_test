import os

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv

from orders.models import Order
from robots.models import Robot

load_dotenv()


@receiver(post_save, sender=Robot)
def notify_users_when_robot_available(sender, instance, created, **kwargs):
    orders = Order.objects.filter(robot_serial=instance.serial)
    for order in orders:
        try:
            send_mail(
                subject='Робот доступен',
                message=f'Добрый день!\n\nНедавно вы интересовались нашим роботом модели {instance.model}.\n'
                        f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.',
                from_email=os.getenv('DEFAULT_FROM_EMAIL'),
                recipient_list=[order.customer.email],
            )
        except Exception as e:
            print(e)
