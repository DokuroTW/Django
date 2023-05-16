from django.db import models

# Create your models here.
class NewsTable(models.Model):
    catego = models.CharField(max_length=10,null=False) #類別
    fakename=models.CharField(max_length=20,null=False) #匿名
    title=models.CharField(max_length=50,null=False)    #標題
    message=models.TextField(null=False)                #內容
    pubtime=models.DateField(auto_now=True)             #發布時間
    enable=models.BooleanField(default=False)           #是否顯示
    press=models.IntegerField(default=0)                #瀏覽次數
    def __str__(self):
        return self.title