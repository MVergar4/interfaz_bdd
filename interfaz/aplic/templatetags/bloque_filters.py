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

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, [])

@register.filter
def trim(value):
    return value.strip()

@register.filter
def lower(value):
    return value.lower()

@register.filter
def dict_get(dictionary, key):
    return dictionary.get(key, {})

@register.filter
def nested_get(dictionary, keys):
    """
    Permite acceder a dictionary[key1][key2] sin romper si alguno no existe.
    Uso en template: {{ dict|nested_get:"key1,key2" }}
    """
    try:
        key1, key2 = keys.split(',')
        return dictionary.get(key1, {}).get(key2, [])
    except (AttributeError, ValueError):
        return []