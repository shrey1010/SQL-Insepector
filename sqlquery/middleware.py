
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format
from django.conf import settings
from decimal import Decimal

def test_middleware(get_response):

    def middleware(request):
        print("before")
        response = get_response(request)
        print("after")
        return response
    
    return middleware


def sql_middleware(get_response):

    def middleware(request):
        response = get_response(request)

        if settings.DEBUG:
            num_queries = len(connection.queries)
            total_execution_time = Decimal()
            check_duplicates = set()
            for query in connection.queries:
                total_execution_time += Decimal(query["time"])
                check_duplicates.add(query["sql"])
                sqlformatted = format(str(query["sql"]),reindent = True)
                print(highlight(sqlformatted,SqlLexer(),TerminalFormatter()))

            print(f"Total Queries Executed : {num_queries}")
            print(f"Duplicate Queries Executed : {num_queries - len(check_duplicates)}")
            print(f"Total Time Taken : {total_execution_time}")
            print("=====================================")

        return response
    return middleware