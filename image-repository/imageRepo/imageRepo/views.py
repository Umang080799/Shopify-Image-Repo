from django.shortcuts import render
from imageRepo.models import imageRepo

# Used to dispaly the images in a gallery format
def displayImg(request):
    display = imageRepo.objects.all()
    return render(request, 'index.html', {'imageRepo': display})
