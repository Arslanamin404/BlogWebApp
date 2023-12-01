from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from .models import *
from django.utils import timezone


# home
def home(request):
    # Order by uploaded_at in descending order
    posts = Post.objects.order_by('-uploaded_at')
    return render(request, 'home.html', {'posts': posts})


# Add Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            Post.objects.create(title=title,
                                description=description,
                                author=request.user,
                                uploaded_at=timezone.now())
            messages.success(request, "Post Uploaded Successfully!")
            return redirect('dashboard')
        else:
            return render(request, 'add_post.html')
    else:
        return redirect('login')


# update Post
def update_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.uploaded_at = datetime.now()
            post.save()
            messages.success(request, "Post Updated Successfully!")
            return redirect('dashboard')
        else:
            return render(request, "update_post.html", {'post': post})
    else:
        return redirect('login')


# read more/add comment
def read_more(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        comment = Comment.objects.create(post=post, name=name, email=email, content=content)
        messages.success(request, "Comment added Successfully!")
        return redirect('read_more', post_id=post_id)
    else:
        # this will get comments from db
        comments = Comment.objects.filter(post=post)
        return render(request, 'read_more.html', {'post': post, 'comments': comments})



# Delete Post
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, "Post Deleted Successfully!")
    return redirect('dashboard')


# about
def about(request):
    return render(request, 'about.html')


# contact
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name,
                               email=email,
                               message=message,
                               uploaded_at=timezone.now())
        messages.success(
            request, 'Success! Thank you for reaching out. Your message has been successfully sent, and I appreciate your interest. I will get back to you as soon as possible.❣️')
        return redirect('home')
    else:
        return render(request, 'contact.html')


# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        # Filter the Post objects to only show posts by the currently logged-in user
        posts = Post.objects.filter(author=request.user)
        return render(request, 'dashboard.html', {'posts': posts})
    else:
        return redirect('login')


# signup
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if email and username and password and confirm_password:
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.warning(
                        request, "This email is already registered.")
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.warning(
                        request, "This username is already taken.")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(email=email,
                                                    username=username,
                                                    password=password)
                    user.save()
                    messages.success(
                        request, "Congratulations! You have successfully become an Author. Login Now and start posting your Blogs!")
                    author_group = Group.objects.get(name="Author")
                    user.groups.add(author_group)
                    return redirect('login')
            else:
                messages.warning(
                    request, "Password does not match. Please try again!")
                return redirect('signup')
        else:
            messages.warning(request, "Please fill out all fields!")
            return redirect('signup')
    else:
        return render(request, 'signup.html')


# login
def login(request):
    if not request.user.is_authenticated:  # chechks if user is already logged in
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.warning(
                    request, "Invalid Login credentials! Please check and try again or SignUp if you are a new user!")
                return redirect("login")
        else:
            return render(request, 'login.html')
    else:
        return redirect('dashboard')


# logout
def logout(request):
    auth.logout(request)
    return redirect('home')
