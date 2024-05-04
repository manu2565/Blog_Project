from django.shortcuts import render, redirect

# Create your views here.

from .form import *
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'Blogs': BlogModel.objects.all()}
    return render(request, 'home.html', context)


def login_view(request):
    return render(request, 'login.html')


def Blog_detail(request, slug):
    context = {}
    try:
        Blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['Blog_obj'] = Blog_obj
    except Exception as e:
        print(e)
    return render(request, 'Blog_detail.html', context)


def see_Blog(request):
    context = {}

    try:
        Blog_objs = BlogModel.objects.filter(user=request.user)
        context['Blog_objs'] = Blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_Blog.html', context)


def add_Blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            Blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(Blog_obj)
            return redirect('/add-Blog/')
    except Exception as e:
        print(e)

    return render(request, 'add_Blog.html', context)


def Blog_update(request, slug):
    context = {}
    try:

        Blog_obj = BlogModel.objects.get(slug=slug)

        if Blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': Blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            Blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )

        context['Blog_obj'] = Blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_Blog.html', context)


def Blog_delete(request, id):
    try:
        Blog_obj = BlogModel.objects.get(id=id)

        if Blog_obj.user == request.user:
            Blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-Blog/')


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')