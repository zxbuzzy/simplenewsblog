from typing import ItemsView
from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',  'body', 'category')
        
        widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
   			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
   			'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id': 'username', 'type':'hidden'}),
			# 'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
   			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'category')
        
        widgets = {
            #Добавление класса form-control  
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
   			'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тэг статьи'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
   			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}