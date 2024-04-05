from django.urls import path
from .import views
# from .views import signup,user_login

urlpatterns=[
    path('',views.home,name='home'),
    # path('home2',views.home2,name='home2'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('book',views.book_list,name='book_list'),
    path('create/',views.create_book,name='create_book'),
    path('update/<int:pk>/',views.update_book,name='update_book'),
    path('delete/<int:pk>/',views.delete_book,name='delete_book')

]