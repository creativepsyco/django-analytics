from django.db import connection
from random import randint, choice
import string
import time
from django.core.management.base import BaseCommand, CommandError



# Sane constants
LOCATIONS = ('SG', 'IN', 'VN')
PRODUCTS = ('coffee_sale',)

class Command(BaseCommand):
    args = 'Nothing'
    help = 'Generates some sample data'

    def handle(self, *args, **options):
        cursor = connection.cursor()


        self.stdout.write("Generating Table")

        VALUE_FIELD = 'value'
        cursor.execute('drop table if exists coffee_sale')
        cursor.fetchone()

        QUERY_A = """
			create table coffee_sale(
				`id` integer primary key autoincrement,
				`uid` int unsigned not null,
				`location` char(10) not null,
				`timestamp` int unsigned not null,
				`source` int unsigned not null,
				`%s` int unsigned not null
			)
			""" % (VALUE_FIELD)

        cursor.execute(QUERY_A)
        cursor.fetchone()
        self.stdout.write("Created Coffee Sale Table")
        for x in xrange(1, 10):
            UID = randint(1, 100)
            LOCATION = ''.join(choice(string.ascii_uppercase)for x in range(4))
            TIMESTAMP = int(time.time()) - randint(400, 3000)
            QUERY = """
			insert into coffee_sale(uid, location, timestamp, source, `%s`) VALUES (%s, '%s', %s, %s, %s)
			""" % (VALUE_FIELD, UID, LOCATION, TIMESTAMP, randint(1, 4), randint(1, 100))

            # self.stdout.write("Query %s" % QUERY)

            cursor.execute(QUERY)
            cursor.fetchone()
