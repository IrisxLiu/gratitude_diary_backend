""" View functions to:
        fetch requested data from Joy model
        handle user authentication
"""
from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Joy
from .forms import JoyForm, UserForm
from .filters import JoyFilter


@login_required(login_url="chill_check:login")
def home(request):
    """ Home page view: create new item
        Parameters:
            request: http request
    """
    if request.method == "POST":
        form = JoyForm(request.POST)
        # Check if all inputs are valid
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            # Display a message if created successfully
            messages.success(request, "Your joy has been captured!")
            # Redirect user back to the home page
            return redirect("chill_check:home")
    else:
        form = JoyForm()
    return render(request, "joylist/home.html", {"form": form})


@login_required(login_url="chill_check:login")
def joy_list(request):
    """ All items page view: list all items, search for items
        Parameters:
            request: http request
    """
    all_joys = Joy.objects.all()  # .all() gets all objects
    search = JoyFilter(request.GET, queryset=all_joys)
    all_joys = search.qs.filter(user=request.user)
    return render(
        request,
        "joylist/joy_list.html",
        {"all_joys": all_joys, "search": search}
    )


@login_required(login_url="chill_check:login")
def joy_detail(request, joy_id):
    """ Item detail view: check detail
        Parameters:
            request: http request
            joy_id: id of requested joy instance
    """
    try:
        detail = Joy.objects.get(pk=joy_id)  # get the object with id
    except Joy.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, "joylist/joy_detail.html", {"detail": detail})


@login_required(login_url="chill_check:login")
def joy_edit(request, joy_id):
    """ View to edit an existing object
        Parameters:
            request: http request
            joy_id: id of requested joy instance
    """
    joy = Joy.objects.get(pk=joy_id)
    form = JoyForm(request.POST or None, instance=joy)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated :D")
        return redirect("chill_check:joys")
    return render(request, "joylist/joy_edit.html", {"joy": joy, "form": form})


@login_required(login_url="chill_check:login")
def joy_delete(request, joy_id):
    """ View to delete an existing object
        Parameters:
            request: http request
            joy_id: id of requested joy instance
    """
    joy = Joy.objects.get(pk=joy_id)
    if request.method == "POST":
        joy.delete()
        messages.success(request, "Deleted Successfully!")
        return redirect("chill_check:joys")
    return render(request, "joylist/joy_delete.html", {"joy": joy})


def user_register(request):
    """ View to register a new account
        Parameters:
            request: http request
    """
    if request.user.is_authenticated:
        messages.info(request, "You have already logged in.")
        return redirect("chill_check:home")
    else:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created!")
                return redirect("chill_check:login")
        else:
            form = UserForm()
        return render(request, 'joylist/register.html', {'form': form})


def user_login(request):
    """ View to login to an existing account
        Parameters:
            request: http request
    """
    if request.user.is_authenticated:
        messages.info(request, "You have already logged in.")
        return redirect("chill_check:home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("chill_check:home")
            else:
                messages.info(request, 'Username or Password is incorrect')
        return render(request, "joylist/login.html", {})


@login_required(login_url="chill_check:login")
def user_logout(request):
    """ View to logout
        Parameters:
            request: http request
    """
    logout(request)
    return redirect("chill_check:login")
