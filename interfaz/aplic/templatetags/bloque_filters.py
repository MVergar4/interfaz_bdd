from django import template
import re

register = template.Library()

@register.filter
def extraer_fecha(bloque):
    """Extrae la segunda cadena entre corchetes (la fecha)."""
    partes = re.findall(r'\[(.*?)\]', bloque or '')
    if len(partes) >= 2:
        return partes[1]
    return ''

@register.filter
def extraer_hora(bloque):
    """Extrae la primera cadena entre corchetes (la hora)."""
    partes = re.findall(r'\[(.*?)\]', bloque or '')
    if len(partes) >= 1:
        return partes[0]
    return ''