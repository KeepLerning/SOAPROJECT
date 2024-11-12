from django import template

register = template.Library()

@register.filter
def rupiah_format(value):
    try:
        value = int(value)  # Pastikan nilainya berupa integer
        return f"Rp {value:,.0f}".replace(",", ".")
    except (ValueError, TypeError):
        return value  # Jika nilai tidak valid, kembalikan seperti aslinya
