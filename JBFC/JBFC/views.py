from django.http import HttpResponse
from django.shortcuts import render

# Request: Cuando requiero parametros en la vista desde la plantilla (Forms)
#           implementa por defecto los token CSRF - Cross Site Scripting
# Response: Cuando enviamos datos de la vista a la plantilla

def formulario(request):
    return render(request,"formulario_registro")
