import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Monitor test cron"

    def handle(self, *args, **options):
        instance = PrintSomething()
        instance()


class PrintSomething(object):

    def __call__(self):
        print('ahihi ahaha')
