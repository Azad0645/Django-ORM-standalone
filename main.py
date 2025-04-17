import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':
    total_passcards = Passcard.objects.count()
    active_passcards = Passcard.objects.filter(is_active=True).count()

    print(f'Всего пропусков: {total_passcards}')
    print(f'Активных пропусков: {active_passcards}')