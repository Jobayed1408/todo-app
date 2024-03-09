from django import forms 
import django_filters
from book.models import TaskModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        
        model = TaskModel
        # fields = "__all__"
        fields = ['taskTitle', 'taskDescription','priority' ,'is_completed','due_date'] 
        labels = {
            'taskTitle' : 'Task Title' 
            
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'placeholder':'Ex: 20/12/2023'})
        }
     
        
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username' , 'first_name', 'last_name', 'email', 'password1', 'password2']

       
