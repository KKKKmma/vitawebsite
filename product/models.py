from django.db import models
from PIL import Image
from io import BytesIO
from home.models import Member,User
from django.core.files import File


# 商品資料    
class Product(models.Model):
    product_number = models.CharField(max_length=50,primary_key=True)
    product_name = models.CharField(max_length=50,default='')
    reservation_date = models.DateField()
    reservation_time = models.TimeField() 
    stock = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    cover_pic = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='vitawebsite_front/scr/image/',blank=False, null=False)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField()
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_user_id')

    class Meta:
        ordering = ('-modify_time',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnai(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

# 商品分類表
class classify(models.Model):
    classify_name  = models.CharField(max_length=50,primary_key=True)
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-classify_name',)

    def __unicode__(self):
        return self.product_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'