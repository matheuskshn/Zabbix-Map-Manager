from django import forms
from .models import CreateMap

class CreateMapForm(forms.ModelForm):
    class Meta:
        model = CreateMap
        fields = ['map_name', 'map_groups', 'map_hosts', 'map_ips', 'map_hosts_filter', 'create_link', 'add_trigger', 'unavailable_by_icmp', 'snmp_not_responding']

        widgets = {
            'map_name': forms.TextInput(attrs={'placeholder': 'Exemplo: CPD-DATACENTER'}),
            'map_groups': forms.Textarea(attrs={'placeholder': 'Exemplo: DATACENTER1, DATACENTER2', 'style': 'resize: vertical;'}),
            'map_hosts': forms.Textarea(attrs={'placeholder': 'Exemplo: SW009, SW019', 'style': 'resize: vertical;'}),
            'map_ips': forms.Textarea(attrs={'placeholder': 'Exemplo: 192.168.99.227, 192.168.99.227', 'style': 'resize: vertical;'}),
            'map_hosts_filter': forms.Textarea(attrs={'placeholder': 'Exemplo: DATASW0, DATASW2','style': 'resize: vertical;'}),
            'create_link': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'add_trigger': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'unavailable_by_icmp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'snmp_not_responding': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateMapForm, self).__init__(*args, **kwargs)
        self.fields['map_groups'].required = False
        self.fields['map_hosts'].required = False
        self.fields['map_ips'].required = False
