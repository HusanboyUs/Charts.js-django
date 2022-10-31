from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club


class ClubChartViev(TemplateView):
    template_name='main/main.html'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['qs']=Club.objects.all()
        return context
        

main_view=ClubChartViev.as_view() 