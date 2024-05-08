from django.db import models

class Pereval(models.Model):
    CHOICE_STATUS = (
        ("new", 'новый'),
        ("pending", 'в работе'),
        ("accepted", 'принятно'),
        ("rejected", 'отклонено'),
    )
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_title = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default="new")

    #ключи

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='users')
    coord = models.ForeignKey('Coord', on_delete=models.CASCADE, related_name='coord')
    level = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='level')

class User(models.Model):
    name = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

class Coord(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    height = models.IntegerField(default=0)

class Level(models.Model):
    CHOICE_LEVEL = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('4A', '4A'),
    )
    winter = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    summer = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    autumn = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    spring = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")

class PerevalImages(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images', blank=True)

