from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        
        widgets = {
            #Добавление класса form-control  
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
   			'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тэг статьи'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
   			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            #Добавление класса form-control  
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
   			'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тэг статьи'}),
   			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}