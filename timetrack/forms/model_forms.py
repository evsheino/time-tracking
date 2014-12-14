from django.forms import ModelForm, DateInput
from timetrack.models import WorkEntry

class WorkEntryForm(ModelForm):
    class Meta:
        model = WorkEntry
        fields = ('date', 'hours', 'comment')
        error_css_class = 'error'
        widgets = {
            'date': DateInput(attrs={
                'class': 'fdatepicker',
                'data-date-format': 'dd.mm.yyyy'
            })
        }
