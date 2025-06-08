from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', 'o valor mínimo deve ser de €20.000,00')
        return price

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error(
                'factory_year', 'não é permitido cadastrar carros fabricados antes de 1975')
        return factory_year

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     price = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self):
#         car = Car(
#             model=self.cleaned_data['model'],
#             brand=self.cleaned_data['brand'],
#             factory_year=self.cleaned_data['factory_year'],
#             model_year=self.cleaned_data['model_year'],
#             plate=self.cleaned_data['plate'],
#             price=self.cleaned_data['price'],
#             photo=self.cleaned_data['photo'],
#         )
#         car.save()
#         return car
