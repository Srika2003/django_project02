from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate 
from .forms import SignupForm,LoginForm
# from django.shortcuts import render,redirect
from .models import Book
import datetime

# Create your views here.
def home(request):
    d=datetime.datetime.now()
    data={'time':d}
    return render(request,'index.html',context=data)

# def home2(request):
#     return render(request,'home2.html')


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('home')  
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})  
    
def user_login(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('book_list')  
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})

def book_list(request):
    books=Book.objects.all()
    d=datetime.datetime.now()
    count=0
    for book in books:
        count=count+1
    return render(request,'book_list.html',{"books":books,"time":d,"count":count})

def create_book(request):
    if request.method=='POST':
        bookname=request.POST.get('bookname')
        bookdescription=request.POST.get('bookdescription')
        bookauthor=request.POST.get('bookauthor')
        bookprice=request.POST.get('bookprice')
        # available=request.POST.get('available')
        Book.objects.create(bookname=bookname,bookdescription=bookdescription,bookauthor=bookauthor,bookprice=bookprice)
        return redirect('book_list')
    return render(request,'create_book.html')

def update_book(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method=="POST":
        bookname=request.POST.get('bookname')
        bookdescription=request.POST.get('bookdescription')
        bookauthor=request.POST.get('bookauthor')
        bookprice=request.POST.get('bookprice')
        # available=request.POST.get('available')
        book.bookname=bookname
        book.bookdescription=bookdescription
        book.bookauthor=bookauthor
        book.bookprice=bookprice
        # book.available=available
        book.save()
        return redirect('book_list')
    return render(request,'update_book.html',{'book':book})

def delete_book(request,pk):
    book=Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')






    

