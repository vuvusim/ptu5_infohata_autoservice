from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic

def index(request):
    return render(request, 'autoservice/index.html', {
        'cars_count': models.Car.objects.count(),
        'services_count': models.Service.objects.count(),
        'orders_count': models.Order.objects.count(),
    })    

def car_list_view(request):
    return render(request, 'autoservice/car_list.html', {'car_list': models.Car.objects.all()})

def car_detail_view(request, pk):
    return render(request, 'autoservice/car_detail.html', {'object': get_object_or_404(models.Car, pk=pk)})

class OrderListView(generic.ListView):
    model = models.Order
    template_name = 'autoservice/order_list.html'


class OrderDetailView(generic.DetailView):
    model = models.Order
    template_name = 'autoservice/order_detail.html'