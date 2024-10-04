from django.db import models

# Create your models here.

class student(models.Model):
    cName = models.CharField(max_length=20,null=False) # 設定字串欄位 最大20長度 不可空白
    cSex = models.CharField(max_length=2,default='M',null=False) # 設定字串欄位 最大2 不可空白
    cBirthday = models.DateField(null=False) # 日期格式
    cEmail = models.EmailField(max_length=100, blank=True, default='') # 建立Email欄位 最大100字元 欄位可空白 預設字為空
    cPhone = models.CharField(max_length=50,blank=True,default='') # 字串欄位 可空白 預設值為空字串
    cAddr = models.CharField(max_length=255,blank=True,default='') # 字串欄位 可空白 預設值為空字串

    def __str__(self):
        return self.cName # 在管理介面以名字顯示
    
# class TestDB(models.Model):
#     cName = models.CharField(max_length=20,null=False) # 設定字串欄位 最大20長度 不可空白
#     cSex = models.CharField(max_length=2,default='M',null=False) # 設定字串欄位 最大2 不可空白

#     def __str__(self):
#         return self.cName