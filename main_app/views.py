from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Cage
from .forms import FeedingForm



# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request,'finches/index.html',{
        'finches': finches
    })
    
def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    id_list = finch.cages.all().values_list('id')
    cages_that_dont_have = Cage.objects.exclude(id__in=id_list)

    feeding_form = FeedingForm()
    return render(request,'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form,
        'cages': cages_that_dont_have
    })

def assoc_cage(request, finch_id, cage_id):
    Finch.objects.get(id=finch_id).cages.add(cage_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_cage(request, finch_id, cage_id):
    Finch.objects.get(id=finch_id).cages.remove(cage_id)
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ('count','name')

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request,finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class CageList(ListView):
  model = Cage

class CageDetail(DetailView):
    model = Cage
    

class CageCreate(CreateView):
  model = Cage
  fields = '__all__'

class CageUpdate(UpdateView):
  model = Cage
  fields = ['name', 'color','material', 'size']

class CageDelete(DeleteView):
  model = Cage
  success_url = '/cages'