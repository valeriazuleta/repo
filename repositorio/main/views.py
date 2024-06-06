from django.shortcuts import render


def main(request):
    return render(request, 'main.html')

def portfolio(request):

    return render(request, 'portafolio.html')

def contacto(request):

    return render(request, 'contacto.html')



def main_Ingles(request):
    return render(request, 'mainIngles.html')

def portfolio_Ingles(request):

    return render(request, 'portafolioIngles.html')

def contacto_Ingles(request):

    return render(request, 'contactoIngles.html')
