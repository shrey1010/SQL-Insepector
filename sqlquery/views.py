from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.core.serializers import serialize
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format
# Create your views here.

def home(request):
    q = Product.objects.all()
    data = serialize('json', q) 
    qs = list(connection.queries)
    for query in qs:
        sqlformatted = format(str(query["sql"]),reindent = True)
        print(highlight(sqlformatted,SqlLexer(),TerminalFormatter()))
    return HttpResponse(data, content_type="application/json")
    