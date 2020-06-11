from django.shortcuts import render,get_object_or_404,redirect
from .models import Author, Category, Article, Category, Commentd
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CreateForm, Register_Form, AuthorForm, CommentForm, CatergoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View

# Create your views here.


class index(View):
    def get(self, request):
        post = Article.objects.all()
        search = request.GET.get('q')
        if search:
            post = post.filter(
            Q(title__icontains=search) | Q(body__icontains=search)
        )

        paginator = Paginator(post, 2)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'post': page_obj
        }

        return render(request, 'index.html', context)

def profile(request,name):
    return render(request, 'profile.html')
def single_info(request, id):
    post = get_object_or_404(Article, pk=id)
    get_comment = Commentd.objects.filter(post=id)
    commenform = CommentForm(request.POST or None, request.FILES or None)
    if commenform.is_valid():
        instance = commenform.save(commit=False)
        instance.post = post
        instance.save()
    
    first = Article.objects.first()
    last=Article.objects.last()
    context = {
        "post": post,
        "first": first,
        "last": last,
        'commenform': commenform,
        'get_comment': get_comment,
        
    }
    
    return render(request, 'single.html',context)
    

def category_info(request, abc):
    cat = get_object_or_404(Category, name=abc)
    post = Article.objects.filter(category=cat.id)
    context = {
        'cat':cat,
        'post':post
    }    
    return render(request, 'category.html',context)

def getlogin(request):
    msg=None
    if request.user.is_authenticated:
        return redirect('Blog:index')
    else:
        if request.method == "GET":
            user = request.GET.get('user')
            passe = request.GET.get('pass')
            auth = authenticate(request, username=user, password=passe)
            if auth is not None:
                login(request, auth)
                return redirect('Blog:index')
            else:
                msg="sorry your username and password is missmatched "
    return render(request,'login.html',{'msg':msg})


def getlogout(request):
    logout(request)
    return redirect('Blog:index')


def create(request):
    if request.user.is_authenticated:
        u = get_object_or_404(Author, name=request.user.id)
        form = CreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = u
            instance.save()
            return redirect('Blog:index')
        else:
            return render(request, 'create.html', {'form': form})
    else:
        return redirect('Blog:login')


def get_update(request,pid):
    if request.user.is_authenticated:
        u = get_object_or_404(Author, name=request.user.id)
        post = get_object_or_404(Article,id=pid)
        form = CreateForm(request.POST or None, request.FILES or None,instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = u
            instance.save()
            return redirect('Blog:login_profile')
        else:
            return render(request, 'create.html', {'form': form})
    else:
        return redirect('Blog:login')


def get_delete(request,pid):
    if request.user.is_authenticated:
       post = get_object_or_404(Article, id=pid)
       post.delete()
       return redirect('Blog:login_profile')
    else:
        return redirect('Blog:login')


def registration(request):
    form = Register_Form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Registration is Succeessful")
        return redirect('Blog:login')
    return render(request, 'registration.html',{"form":form})
















def login_profile(request):
    if request.user.is_authenticated:
        user=get_object_or_404(User,id=request.user.id)
        author_pic = Author.objects.filter(name=user.id)
        if author_pic:
            author_user=get_object_or_404(Author,name=request.user.id)
            post = Article.objects.filter(article_author=author_user.id)
            return render(request, 'loged_in_profile.html', {'post': post, 'user': author_user})
        else:
            form = AuthorForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.name=user
                instance.save()
                return redirect('Blog:login_profile')
            return render(request, 'author_form.html', {'form': form})
            

    else:
        return redirect('Blog:login')

def get_topic(request):
    post = Category.objects.all()
    return render(request, 'topic.html', {"post": post})


def create_topics(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            form = CatergoryForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('Blog:topic')
            return render(request, 'topic_create.html', {"form": form})
        else:
            messages.success(request, "U are not staff or superuser")
    else:
        return redirect("Blog:login")
