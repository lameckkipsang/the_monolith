from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artwork, CategoryTag, CuratorProfile
from .forms import CuratorRegistrationForm, EditAccountForm, EditProfileForm

# Create your views here.

def exhibition_home(request):
    """Displays all artworks, with an optional category filter."""
    selected_tag = request.GET.get('tag')
    
    if selected_tag:
        tag_object = get_object_or_404(CategoryTag, name__iexact=selected_tag)
        artworks = tag_object.artworks.all()
    else:
        artworks = Artwork.objects.all()
        
    tags = CategoryTag.objects.all()
    
    context = {
        "artworks": artworks,
        "tags": tags,
        "selected_tag": selected_tag,
    }
    return render(request, 'homepage.html', context)

def artwork_detail(request, artwork_id):
    """Displays a single artwork's details."""
    artwork = get_object_or_404(Artwork, id=artwork_id)
    return render(request, 'artwork_detail.html', {"artwork": artwork})

def register_curator(request):
    """Handles new user signups and logs them in immediately."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CuratorRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            CuratorProfile.objects.get_or_create(user_account=new_user)
            
            login(request, new_user)
            messages.success(request, f"Welcome to The Monolith, Curator {new_user.username}!")
            return redirect('home')
        else:
            messages.error(request, "There was a problem with your registration.")
    else:
        form = CuratorRegistrationForm()

    return render(request, 'signup.html', {"form": form})
    

@login_required
def curator_profile(request):
    """Allows a logged-in user to view and update their profile and avatar."""
    profile, created = CuratorProfile.objects.get_or_create(user_account=request.user)

    if request.method == "POST":
        account_form = EditAccountForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if account_form.is_valid() and profile_form.is_valid():
            account_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        account_form = EditAccountForm(instance=request.user)
        profile_form = EditProfileForm(instance=profile)

    context = {
        "profile": profile,
        "account_form": account_form,
        "profile_form": profile_form,
    }
    return render(request, 'profile.html', context)

@login_required
def toggle_like(request, artwork_id):
    """Toggles a like on an artwork for the logged-in user."""
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.user in artwork.likes.all():
        artwork.likes.remove(request.user)
    else:
        artwork.likes.add(request.user)
    return redirect('artwork_detail', artwork_id=artwork.id)

@login_required
def profile_view(request):
    profile, created = CuratorProfile.objects.get_or_create(user_account=request.user)
    return render(request, 'profile.html', {'profile': profile})