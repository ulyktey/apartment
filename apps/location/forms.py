from django import forms
from models import Region, City, District, Street


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ('name','district')

    def custom_district_choice():
        city_objs = City.objects.all()
        choice = []
        for obj in city_objs:
            tmp_list = []
            obj_districts = District.objects.filter(city = obj.id)
            if obj_districts:
                tmp_list.append(obj)
                tmp_list.append(([(x.id, '--- %s' % x) for x in obj_districts]))
                choice.append(tmp_list)
        return choice
    district = forms.ChoiceField(choices=custom_district_choice())
    name = forms.CharField(max_length = 255, required = True)

    def clean(self):
        self.cleaned_data['district'] = District.objects.get(id = self.cleaned_data['district'])
        return self.cleaned_data
