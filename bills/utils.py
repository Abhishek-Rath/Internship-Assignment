from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
#pisa is a html2pdf converter using the ReportLab Toolkit,
#the HTML5lib and pyPdf.
 
from xhtml2pdf import pisa  
#difine render_to_pdf() function
 
def render_to_pdf(template):
    result = BytesIO()
 
     #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(template.encode('utf-8')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None