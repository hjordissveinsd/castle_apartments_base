from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from Profile.models import User, Profile

from .forms import ProfileForm, CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
# bætti við contex = ......
def profile(request):
    #context = {'profiles' : User.objects.all()}
    return render(request, 'Profile/profile.html')
#profile/profileMain.html', context)

def messages(request):
    return render(request, 'Profile/messages.html')

def settings(request):
    return render(request, 'Profile/settings.html')

def createOrLogIn (request):
    return render(request, 'Profile/createOrLogIn.html')

def loggedIn (request):
    return render(request, 'Profile/loggedIn.html')

def notLoggedIn (request):
    return render(request, 'Profile/notLoggedIn.html')

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

            return redirect('profile')
        else:
            print('invalid')

            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'profile/profile_2.html', context)



    # All other cases that are not a POST (like GET request).
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile/profile_2.html', context)


###############################################
#raggi að bæta við#############################

#def settings(request):
#    return render(request, 'profile/profileSettings.html')