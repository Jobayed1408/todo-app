from django.urls import path
from book.views import home, store_book, show_book, edit_task, delete_task, complete,registration,user_login, user_logout
urlpatterns = [
    path('', home),
    path('store_book/', store_book, name = "store_book"),
    path('show_book/', show_book, name = "show_book"),
    path('registration/', registration, name = "registration"),  
    path('user_login/', user_login, name = "user_login"),  
    path('logout/', user_logout, name = "user_logout"),  
    path('edit_task/<int:id>', edit_task, name = "edit_task"),  
    path('delete_task/<int:id>', delete_task, name = "delete_task"),  
    path('complete_task/<int:id>', complete, name = "complete"),  
]

