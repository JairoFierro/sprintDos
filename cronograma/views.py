from django.shortcuts import render
from .models import Cronograma
from pago.models import Pago

def cronograma_index(request):
    cronogramas = Cronograma.objects.all() 
    return render(request, 'cronograma_index.html', {'cronogramas': cronogramas})

def listado_cronogramas(request):
    cronogramas = Cronograma.objects.all()
    pagos = Pago.objects.all()

    # Construir un diccionario de pagos asociados a cada cronograma
    pagos_dict = {}
    for pago in pagos:
        if pago.cronograma_id not in pagos_dict:
            pagos_dict[pago.cronograma_id] = []
        pagos_dict[pago.cronograma_id].append(pago)

    # Pasar el diccionario a la plantilla
    return render(request, 'listado_cronogramas.html', {'cronogramas': cronogramas, 'pagos': pagos_dict})