from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django import forms
from django.urls import reverse
from .models import Image


class ImageList(ListView):
    Image.objects.all().delete()  
    model=Image

class ImageCreate(CreateView):
    """
    для создания нового изображения
    """
    model = Image
    fields = ['picture', 'image_url', 'name', ]
    def get_success_url(self): # при успешной загрузке переходим на стр. с изменением размеров
        return reverse('detail', args=[self.object.id])  


class SizeForm(forms.Form):
    hight = forms.CharField()
    width = forms.CharField()

class ImageDetail(DetailView):
    """
    отображение информации об изображении
    """
    model = Image

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['image_form'] = SizeForm()
        return context
    def post(self, request, *args, **kwargs):
        image_form = SizeForm(request.POST)
        if image_form.is_valid():
            image =  self.get_object()
            image.hight = image_form.cleaned_data['hight'] # передаем новую высоту
            image.width = image_form.cleaned_data['width'] # передаем новую ширину
            image.save() # А теперь можно сохранить в базу
        else:
            raise Exception
        return redirect(reverse('detail', args=[self.get_object().id])) # обновляем страницу 
      