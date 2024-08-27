from django.forms import ModelForm
from .models import CustomerResponse

class CustomerForm(ModelForm):

    class Meta:
        model = CustomerResponse
        fields = '__all__'