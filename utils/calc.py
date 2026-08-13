import datetime
import calendar

def calcular_dias(fecha_inicio: datetime.date) -> int:
    """Calcula los días totales transcurridos desde una fecha especial hasta hoy."""
    hoy = datetime.date.today()
    diferencia = hoy - fecha_inicio
    return diferencia.days

def calcular_tiempo_detallado(fecha_inicio: datetime.date) -> str:
    """Calcula el tiempo transcurrido en formato de años, meses y días."""
    hoy = datetime.date.today()
    
    anios = hoy.year - fecha_inicio.year
    meses = hoy.month - fecha_inicio.month
    dias = hoy.day - fecha_inicio.day

    if dias < 0:
        meses -= 1
        mes_anterior = hoy.month - 1 if hoy.month > 1 else 12
        anio_anterior = hoy.year if hoy.month > 1 else hoy.year - 1
        dias += calendar.monthrange(anio_anterior, mes_anterior)[1]

    if meses < 0:
        anios -= 1
        meses += 12

    partes = []
    if anios > 0:
        partes.append(f"{anios} {'año' if anios == 1 else 'años'}")
    if meses > 0:
        partes.append(f"{meses} {'mes' if meses == 1 else 'meses'}")
    if dias > 0 or not partes:
        partes.append(f"{dias} {'día' if dias == 1 else 'días'}")

    return ", ".join(partes)