from django.db import connection
from models import *


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


class IndicatorProcessor(object):

    """docstring for IndicatorProcessor"""

    def __init__(self, arg):
        super(IndicatorProcessor, self).__init__()
        self.arg = arg

    def factory(type):
    # return eval(type + "()")
        if type == "Sum":
            return IndicatorProcessorForSum()
        assert 0, "Bad type creation: " + type
    factory = staticmethod(factory)

    def process(self, start, end, indicator):
        """
        Override behavior in order to process the implementation
        """
        return 0


class IndicatorProcessorForSum(IndicatorProcessor):

    def process(self, start, end, indicator):
        QUERY_FORMAT = """
        	SELECT SUM(%s) AS stat FROM %s WHERE timestamp>=%s AND timestamp<=%s 
        	AND location IN (%s) AND source IN (%s)
        """
        FIELD = 'value'
        DB = indicator.source()
        LOCATIONS = ','.join(indicator.locations)
        SOURCES = ','.join(indicator.sources)

        QUERY = QUERY_FORMAT % (FIELD, DB, start, end, LOCATIONS, SOURCES,)

        cursor = connection.cursor()
        cursor.execute(QUERY)

        stat = dictfetchall(cursor)
        return stat[0]['stat']
