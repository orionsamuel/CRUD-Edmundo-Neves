from django.forms import ModelForm
from app.models import Carros

# Creat the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']