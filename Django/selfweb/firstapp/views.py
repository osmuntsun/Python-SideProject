from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import pandas as pd
# from firstapp.models import TestDB

# Create your views here.
def sayhello(request):
    return HttpResponse('hello 妳好')

def hello2(request,username):
    return HttpResponse(f'hello,{username}')

def hello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())

def hello4(request,username):
    now = datetime.now()
    return render(request,"hello4.html",locals())

def hello(request):
    context = {}
    
    # 表示會載入 templates/blog/index.html
    return render(request, 'index.html', context)

# df = pd.read_csv('./static/data/stock.csv')
# print(df['Date'])
# for i in range(len(df['Date'])):
#     TestDB.objects.create(cName=df['Date'][i],cSex='F')

# TestDB.objects.all().delete()