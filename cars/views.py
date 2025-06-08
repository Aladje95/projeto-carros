from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self) -> QuerySet[Any]:
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)

        return cars

# Compare this snippet from cars/views.py:


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

# esta view é responsável por renderizar o formulário de cadastro de carros


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    # def get(self, request, pk):
    #     car = self.model.objects.get(pk=pk)
    #     form = self.form_class(instance=car)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, pk):
    #     car = self.model.objects.get(pk=pk)
    #     form = self.form_class(request.POST, request.FILES, instance=car)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('cars_list')
    #     return render(request, self.template_name, {'form': form})


# from cars.forms import CarForm
# from django.http import HttpResponse

# esta função é uma view que renderiza a página de carros
# e foi substituída pela classe CarsView que herda de View de Django.


# def cars_view(request):
#     search = request.GET.get('search')
#     cars = Car.objects.filter(
#         model__icontains=search) if search else Car.objects.all().order_by('model')
#     # cars = Car.objects.filter(model__contains='Chevette')  # aqui conseguimos
#     # filtrar os carros que possuem 'Chevette' no modelo, ou seja,
#     # todos os carros que possuem 'Chevette' ou se colocarmos um
#     # caracter que está no nosso obejecto no modelo serão retornados aquele obejecto.

#     return render(request, 'cars.html', {'cars': cars})


# class CarsView(View):
#     def get(self, request):
#         search = request.GET.get('search')
#         cars = Car.objects.filter(
#             model__icontains=search) if search else Car.objects.all().order_by('model')
#         return render(request, 'cars.html', {'cars': cars})


# class NewCarView(View):
#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})


# esta view é responsável por renderizar o formulário de cadastro de carros
# e salvar os dados no banco de dados quando o formulário é enviado.
# ela foi substituída pela função NewCarView que renderiza o formulário
# e salva os dados no banco de dados quando o formulário é enviado.

# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()

#     return render(request, 'new_car.html', {'new_car_form': new_car_form})
