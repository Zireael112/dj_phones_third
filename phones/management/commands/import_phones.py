import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            values = list(phone.values())
            new_phone = Phone.objects.create(
                id=int(values[0]),
                name=values[1],
                image=values[2],
                price=int(values[3]),
                release_date=values[4],
                lte_exists=values[5],
                slug=slugify(values[1]),
            )

