from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
import random
import string

def get_random_string():
    letters = string.ascii_lowercase+string.digits
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str.upper()

def generate_pdf(data):
    template = get_template('pdf/recepisse.html')
    html = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    print(pdf.err)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None