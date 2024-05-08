from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings

from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import os
from imageGeneration.models import Prompt, Image, UserImage


from django.shortcuts import render, get_object_or_404


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

# Addition of imageForge Views

def generation(request):
    """Show generation page."""
    return render(request, 'learning_logs/generation.html')

def gallery(request):
    """Show gallery page."""
    return render(request, 'learning_logs/gallery.html')

def user_history(request):
    """Show user history page."""
    return render(request, 'learning_logs/user_history.html')

def about(request):
    """Show the about page."""
    return render(request, 'learning_logs/about.html')

def prompt(request):
    most_recent_prompt = Prompt.objects.latest('date_added')
    context = {'prompt': most_recent_prompt}
    return render(request, 'learning_logs/prompt.html', context)


# Script execution on button click

def run_prompt_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'grammar.py')
    subprocess.run(["python", script_path], cwd=settings.BASE_DIR)
    return redirect('learning_logs:prompt')

def run_image_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'newImageInstance.py')
    subprocess.run(["python", script_path], cwd=settings.BASE_DIR)
    return render(request, 'learning_logs/user_image.html')



def user_image(request):
    # Get the most recent image from the Image model
    most_recent_image = Image.objects.latest('datetime_field')

    if request.user.is_authenticated:
        # Check if this image is already associated with the user
        user_image_instance = UserImage.objects.filter(
            image_field=most_recent_image.image_field, 
            owner=request.user
        ).first()

        # If not associated, create a new UserImage instance linked to the user
        if not user_image_instance:
            user_image_instance = UserImage(
                text_field=most_recent_image.text_field,
                datetime_field=most_recent_image.datetime_field,
                image_field=most_recent_image.image_field,
                local_url=most_recent_image.local_url,
                owner=request.user,
            )
            user_image_instance.save()
            print('New UserImage instance created with ID:', user_image_instance.id)

    # Pass the most recent image instance to the template
    context = {
        'image': most_recent_image,
    }

    return render(request, 'learning_logs/user_image.html', context)