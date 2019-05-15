from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from Profile.models import User, Profile
from Profile.models import Tracker

from .forms import ProfileForm, CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
# bætti við contex = ......
def profile(request):
    #context = {'profiles' : User.objects.all()}
    return render(request, 'profile/profile.html')
#profile/profileMain.html', context)

def messages(request):
    return render(request, 'Profile/messages.html')

def createOrLogIn (request):
    return render(request, 'Profile/createOrLogIn.html')

def loggedIn (request):
    return render(request, 'Profile/loggedIn.html')

def notLoggedIn (request):
    return render(request, 'Profile/notLoggedIn.html')

def browsingHistory (request):

    check_list = [request.user.id]
    #all_instances = Tracker.objects.all()
    #filtered = Tracker.objects.filter(test_id__in=test_ids).filter([some other filtering])
    context = {'trackers': list(Tracker.objects.filter(user_id__in=(check_list)))}
    #context = {'trackers': Tracker.objects..filter(user_id=request.user.id)}
    return render(request, 'Profile/browsingHistory.html', context)

####################raggi######################
def register1(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('invalid')

            return render(request, 'profile/register.html',
                   {'form': form})

    # All other cases that are not a POST.
    return render(request, 'profile/register.html',
                  {'form' : UserCreationForm()})


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            print('VALID')

            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
        else:
            print('invalid')

            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/register.html', context)

    # All other cases that are not a POST (like GET request).
    context = {'user_form': CustomUserCreationForm(), 'profile_form': ProfileForm()}
    return render(request, 'profile/register.html', context)





@login_required
def profile(request):
    print('current user = ', request.user.id)
    user = get_object_or_404(User, pk=request.user.id)
    print('current user info = ', user.profile.phone)

    # used to overrite current data, instance=   populates
    user_form = CustomUserChangeForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)

    print(profile_form.instance.avatar.url)

    return render(request, 'Profile/profile_2.html')


def settings(request):
    print('current user = ', request.user.id)
    user = get_object_or_404(User, pk=request.user.id)
    print('current user info = ', user.profile.phone)

    # used to overrite current data, instance=   populates
    user_form = CustomUserChangeForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)

    print(user_form)
    print(profile_form)
    if request.method == 'POST':
        #user_form = CustomUserChangeForm(request.POST, instance=user)
        #profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('settings')
        else:
            print('invalid')

            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/settings.html', context)

    # All other cases that are not a POST (like GET request).
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'Profile/settings.html', context)

###############################################
#raggi að bæta við#############################

#def settings(request):
#    return render(request, 'profile/profileSettings.html')