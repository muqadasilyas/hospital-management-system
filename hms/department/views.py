from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from department.forms import DepartmentForm
from department.models import Department


# Create your views here.

class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'department/department_list.html'

class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'department/department_detail.html'

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department/department_form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/department_form.html'
    success_url = reverse_lazy('department_list')

class DepartmentDeleteView(DeleteView):
    model = Department
    context_object_name = 'department'
    template_name = 'department/department_delete.html'
    success_url = reverse_lazy('department_list')
