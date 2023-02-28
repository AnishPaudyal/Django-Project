from django.shortcuts import render, redirect
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm, Sellform,Commentform
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
from .models import Sell,brand,category,Comment

def productdetail(request,id):
    product = Sell.objects.get(id=id)
    comment = Comment.objects.filter(product=product)
    if request.method == "POST":
        Commentforms = Commentform(request.POST)
        if Commentforms.is_valid():
            commen = Commentforms.save(commit=False)
            commen.owner = request.user
            commen.product = product
            commen.save()
        else:
            messages.error(request, 'Something went wrong')
    else:
        Commentforms = Commentform()
    return render(request, 'main/detail.html',
                  {'Commentforms': Commentforms, 'sell': product, 'comment': comment, 'name': product.name})


def homepage(request):
    return render(request=request, template_name='main/home.html')

def brands(request,slug):
    bran= brand.objects.get(name=slug)
    product = Sell.objects.filter(brand=bran)
    return render(request, 'main/brands.html', {'product': product,'name':slug})

def categories(request,slug):
    cate= category.objects.get(name=slug)
    product = Sell.objects.filter(category=cate)
    return render(request, 'main/brands.html', {'product': product,'name':slug})


@csrf_exempt
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error((request, "Invalid username or password."))
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("main:login")


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect("main:profile")  # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'main/profile.html', context)



@login_required
def sell(request):
    if request.method == "POST":
        Sellforms = Sellform(request.POST, request.FILES)
        if Sellforms.is_valid():
            Sell = Sellforms.save(commit=False)
            Sell.owner = request.user
            Sell.save()
            return redirect('main:allproduct')
        # else:
        #     messages.error(request, 'Something went wrong')
        #     return redirect('main:homepage')
    else:
        Sellforms=Sellform()

        template='main/sell.html'
        context = {'Sellform': Sellforms}
        return render(request, template, context)


@login_required
def comment(request,id):
    product = Sell.objects.get(id=id)
    comment = Comment.objects.filter(product=product)
    if request.method == "POST":
        Commentforms = Commentform(request.POST)
        if Commentforms.is_valid():
            comment = Commentforms.save(commit=False)
            comment.owner = request.user
            comment.product=product
            comment.save()
        else:
            messages.error(request, 'Something went wrong')
    else:
        Commentforms=Commentform()
        template='main/detail.html'
    return render(request, 'main/detail.html', {'Commentforms':Commentforms,'sell': product, 'comment': comment, 'name': product.name})

def allproduct(request):
    search_query = request.GET.get('q')
    product = Sell.objects.all()
    if (search_query):
        product= product.filter(Q(name__icontains=search_query) |
                                   Q(description__icontains=search_query) |
                                   Q(condition__icontains=search_query) |
                                   Q(brand__name__icontains=search_query) |
                                   Q(category__name__icontains=search_query))
    return render(request, 'main/allproduct.html', {'product': product})


