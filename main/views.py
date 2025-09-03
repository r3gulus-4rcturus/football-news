from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406362860',
        'name': 'Muhammad Lanang',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)


