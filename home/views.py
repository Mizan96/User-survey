from django.shortcuts import render, redirect
from django.views import View
from .models import *
# Create your views here.

def index(request):
    feedbacks = CustomerFeedback.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'index.html', context)


def customer_feedback(request, id):
    feedback = CustomerFeedback.objects.get(id=id)
    context = {
        'questions': feedback.question.all()
    }
    if request.method == 'POST':
        for question in feedback.question.all():
            response_text = request.POST.get(f'response__{ question.id }')
            selected_options_ids = request.POST.getlist(f'options__{ question.id }')
            response = CustomerResponse.objects.create(
                feedback = feedback,
                question = question,
                response_text = response_text if question.question_type in ["Text", "BigText"] else None
            )
            if selected_options_ids:
                selected_options = Options.objects.filter(id__in = selected_options_ids)
                response.selected_options.set(selected_options)
            print(response_text)
            print(selected_options_ids)

            return redirect("/")
        
    return render(request, 'survey.html', context)

class GraphView(View):
    def get(self, request, *args, **kwargs):
        template_name='graph.html'
        context = {}
        return render(request,template_name=template_name, context=context)
