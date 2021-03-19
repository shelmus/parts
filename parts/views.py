from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from .models import Part
from .forms import AddPart

# Create your views here.

def search_parts(request):
    parts = Part.objects.all().order_by('create_date')
    return render(request, 'parts/search_parts.html', {'parts': parts})

def new_parts(request):
    if request.method == "POST":
        form = AddPart(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.author = request.user
            part.create_date = timezone.now()
            part.save()
            messages.success(request, 'Part added succesfully')
    else:
        form = AddPart()
    return render(request, 'parts/new_parts.html', {'form': form})

def part_detail(request, part_id):
    part_obj = get_object_or_404(Part, serial=part_id)
    return render(request, 'parts/part_detail.html', {'part': part_obj})

def remove_part(request, part_id):
    if request.method == "POST":
        form = AddPart()
        parts_list = Part.objects.all()
        part_id = int(request.POST.get('part_id'))
        part = Part.objects.get(id=part_id)
        part.delete()
        messages.success(request, 'Part deleted succesfully')
