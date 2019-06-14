from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class CroquisListadoView(TemplateView):
    template_name = 'croquis_listado/monitoreo.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=403)

