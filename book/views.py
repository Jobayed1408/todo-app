from django.shortcuts import render, redirect
from book.forms import TaskForm, RegistrationForm
from book.models import TaskModel
from django.contrib.auth import login, logout, authenticate
# from .forms import 

# Create your views here.

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key 

def home(request): 
    return render(request, 'base.html') 



def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('store_book') 
    return render(request, 'store_book.html', {'form': form})  


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(username = user_name, password = password) 
        print(user) 
        if(user == None): 
            return render(request, 'login.html' )  
        login(request,user) 
        return redirect('store_book') 
    return render(request, 'login.html')  




def user_logout(request):          
    logout(request)           
    return redirect('user_login')    




def store_book(request): 
    if request.method == 'POST': 
        book = TaskForm(request.POST) 
        print("User Id", request.user.id) 
        book.instance.user = request.user
        if book.is_valid():
            book.save()
            print(book.cleaned_data) 
            return redirect('show_book')
    
    else:
        book = TaskForm() 
     
    return render(request, 'store_book.html', {'form':book}) 



def show_book(request):
    book = request.user.my_task.all().order_by('-priority').values()
    print(book)
    return render(request, 'show_book.html', {'data':book}) 



def edit_task(request, id):
    book = TaskModel.objects.get(pk = id) 
    form = TaskForm(instance=book) 
    if request.method == 'POST':
        book = TaskForm(request.POST, instance=book)
        if book.is_valid():
            book.save()
            return redirect('show_book')
    else:
        book = TaskForm() 
        
    return render(request, 'store_book.html', {'form':form}) 





def delete_task(request, id):
    book = TaskModel.objects.get(pk = id).delete()  
    return redirect('show_book')




def complete(request, id):
    book = TaskModel.objects.get(pk = id)
    TaskModel.objects.get(pk = id).delete()   
    return render(request, 'complete_task.html', {'book':book}) 


