from django.contrib import admin
from firstapp.models import student 
# from firstapp.models import student ,TestDB

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ("id","cName","cSex","cBirthday","cEmail","cPhone","cAddr")
    list_filter = ("cName","cSex")
    search_fields = ('cName',)
    ordering = ('id','-id')

admin.site.register(student,studentAdmin) # 將資料庫登入到admin
# admin.site.register(TestDB)