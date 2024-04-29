from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login, get_user_model
from .models import Comment, Post,UserAccessLog
from django.contrib.auth.decorators import login_required
from myapp.permissions import check_is_creator_or_admin
from django.contrib.auth.models import User

# Create your views here.


#get_user_model().objects.filter(username="admin").exists()

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
    else:
        return redirect("login")




def home(request):
    posts = Post.objects.all()

    return render(request, "home.html", {"posts": posts})


@login_required
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        new_post = Post.objects.create(
            title=title, content=content, creator=request.user
        )
        return redirect("detail", new_post.pk)

    return render(request, "new.html")

from django.utils.timezone import now
from functools import wraps

def log_user_access(view_func):
    @wraps(view_func)
    def _wrapped_view(request, post_pk):
        # 뷰 함수 호출 전 로깅
        if request.user.is_authenticated:
            UserAccessLog.objects.create(post=Post.objects.get(pk=post_pk),user=request.user)
        # 원래의 뷰 함수 호출
        return view_func(request, post_pk)
    return _wrapped_view

@login_required
@log_user_access
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    log = post.logs.all()[len(post.logs.all())-1]
    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content, creator=request.user)
        return redirect("detail", post_pk)

    return render(request, "detail.html", {"post": post,'log':log})


@login_required
@check_is_creator_or_admin(Post, "post_pk")
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail", post_pk)

    return render(request, "edit.html", {"post": post})


@login_required
@check_is_creator_or_admin(Post, "post_pk")
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")


@login_required
@check_is_creator_or_admin(Comment, "comment_pk")
def delete_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect("detail", post_pk)
