from django.shortcuts import render, redirect
from django.views import View
from .froms import CustomerForm
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name='index.html'
        form = CustomerForm()
        context = {
            'form': form
        }
        return render(request,template_name=template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        template_name='index.html'
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        context = {
            'form': form
        }
        return render(request,template_name=template_name, context=context)
    

class GraphView(View):
    def get(self, request, *args, **kwargs):
        template_name='graph.html'
        context = {}
        return render(request,template_name=template_name, context=context)
