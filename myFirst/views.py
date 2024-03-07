from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello!, Welcome to Index Page")

def contact(request):
    msg = "<h3> Email: CSIPT101BARTIANA@gmail.com </br> \
                Telephone: 09211436970 \
            </h3>"
    return HttpResponse(msg)

def about(request):
    pangalan = "Fritz"
    apelyido = "Bartiana"
    edad = "22"

    return render(request, "about.html",{'fname': pangalan, 'lname': apelyido, 'age': edad})

def aboutContext(request):
    context = {
        'pangalan': "Fritz",
        'quiz1': 100,
        'quiz2': 50,
    }
    return render(request, 'aboutContext.html', context)

def aboutFilters(request):
    context = {
        'pangalan': "Fritz",
        'motto': "To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries."
    }
    return render(request, 'aboutFilters.html', context)

def aboutIf(request):
    context = {
        'pangalan': "Fritz",
        'quiz1': 100,
        'quiz2': 50,
    }
    return render(request, "aboutIfElifElse.html", context)

def installation(request):
    context = {
        'title': "Installation",
        'skills': ["Interest in setting up a smart home"],
        'tools': ["Ethernet connection"],
    }
    return render(request, 'installation.html', context)

def configuration(request):
    context = {
        'title': "Configuration",
    }
    return render(request, 'configuration.html', context)

def automation(request):
    context = {
        'title': "Configuration",
        'skills': ["If you have got the hang of blueprints and would like to explore more, it’s time for the next step. But before you start creating automations, you will need to learn about the automation basics."]
    }
    return render(request, 'configuration.html', context)