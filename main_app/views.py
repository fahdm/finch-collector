from django.shortcuts import render

# TODO Temporrary Database - Remove This After Adding Finch Model

finches = [
    { 'species': 'finches and buntings', 'breed': 'Hawfinch', 'description': 'rusty, orange-brown', 'count': 40},
    {'species': 'finches and buntings', 'breed': 'Greenfinch', 'description': ' olive-green, but with a yellow patch on the wings and tail', 'count': 50},
    {'species': 'finches and buntings', 'breed': 'Chaffinch', 'description': 'colourful finch that is gingery-brown', 'count': 2},
    {'species': 'finches and buntings', 'breed': 'goldfinch', 'description': ' blue-grey crown, brown back and pink breast ', 'count': 200},
]

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    return render(request,'finches/index.html',{

        'finches': finches

    })
    
