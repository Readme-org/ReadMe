from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Testing',
        'class': 'Test'
    }

    return render(request, "main.html", context)