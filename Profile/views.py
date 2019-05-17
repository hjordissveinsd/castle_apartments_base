from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from Profile.models import User, Profile
from Profile.models import Tracker
from Browse.models import Estate, Search

from .forms import ProfileForm, CustomUserCreationForm, CustomUserChangeForm

def profile(request):
    return render(request, 'profile/profile.html')


def create_or_log_in (request):
    return render(request, 'Profile/createOrLogIn.html')


def logged_in (request):
    return render(request, 'Profile/loggedIn.html')


def not_logged_in (request):
    return render(request, 'Profile/notLoggedIn.html')


@login_required
def create_track(request, id):
    track, created = Tracker.objects.get_or_create(user_id=request.user.id, estate_id=id, url=request.get_raw_uri())
    if created == True:
        track.save()

def browsing_history (request):
    info_list = []

    check_list = [request.user.id]
    trackers = list(Tracker.objects.filter(user_id__in=(check_list)))
    estates = []

    for tracker in trackers:
        the_instance = Estate.objects.get(pk=tracker.estate_id)
        estates.append(the_instance)

    context = {'estates': estates}
    return render(request, 'Profile/browsingHistory.html', context)


def search_history(request):
    check_list = [request.user.id]
    searches = list(Search.objects.filter(user_id__in=(check_list)))
    context = {'searches' : searches}
    return render(request, 'Profile/searchHistory.html', context)


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        else:
            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/register.html', context)
    context = {'user_form': CustomUserCreationForm(), 'profile_form': ProfileForm()}
    return render(request, 'profile/register.html', context)


@login_required
def profile(request):
    #print('current user = ', request.user.id)
    #user = get_object_or_404(User, pk=request.user.id)
    #print('current user info = ', user.profile.phone)
    return render(request, 'Profile/profile.html')


def settings(request):
    #print('current user = ', request.user.id)
    user = get_object_or_404(User, pk=request.user.id)
    #print('current user info = ', user.profile.phone)

    # used to overrite current data, instance=   populates
    user_form = CustomUserChangeForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('settings')
        else:
            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/settings.html', context)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'Profile/settings.html', context)