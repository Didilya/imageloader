import urllib.request 
import os 
from django.db import models
from django.core.files import File
from django.core.exceptions import ValidationError

class Image(models.Model):
    picture = models.ImageField(blank=True)
    image_url = models.URLField(blank=True)
    name = models.TextField()
    hight = models.TextField(blank=True)
    width = models.TextField(blank=True)


    def save(self, *args, **kwargs):  
        """
        переопределение метода save()
        """
        if self.image_url and not self.picture:  # если передан только image_url, а picture пустой
            result = urllib.request.urlretrieve(self.image_url) # сохраняем изображение из url
            self.picture.save(
                os.path.basename(self.image_url),
                File(open(result[0],'rb'))  # открываем только что сохраненное изображение
            )
            super().save(*args, **kwargs)  # А теперь можно сохранить в базу
        if not self.image_url and not self.picture:  # если image_url и picture пустые
            raise ValidationError("You have forgotten about image!")
        else:
            super().save(*args, **kwargs) # если все ок - сохранить в базу
