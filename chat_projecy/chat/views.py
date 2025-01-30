from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login  # Import authenticate and login
from django.db.models import Q  # Import Q for complex queries
from .models import ChatMessage  # Updated import

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # Create user and save
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user.save()
        print("User created successfully")
        
        # Redirect to chat room after registration
        return redirect('chat_room', room_name='default')  # Ensure 'default' is a valid room name
    else:
        return render(request, "chat/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('chat_room', room_name='default')  # Redirect to chat room after login
    return render(request, "chat/login.html")

def chat_room_view(request, room_name):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated

    users = User.objects.exclude(id=request.user.id)  # Fetch all users except the current user
    messages = ChatMessage.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('timestamp')
    return render(request, "chat_room.html", {"room_name": room_name, "users": users, "messages": messages})

def home_view(request):
    return render(request, "home.html")

def chat(request, receiver_id):
    users = User.objects.exclude(id=request.user.id)
    messages = ChatMessage.objects.filter(
        Q(sender=request.user, receiver=receiver_id) |
        Q(sender=receiver_id, receiver=request.user)
    ).order_by('timestamp')
    return render(request, 'chat.html', {'users': users, 'messages': messages, 'receiver_id': receiver_id})
