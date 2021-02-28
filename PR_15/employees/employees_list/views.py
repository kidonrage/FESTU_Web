from django.shortcuts import render
from employees_list.models import Employee

# Create your views here.
def home_view(req):
  employees = Employee.objects.all()
  return render(req, "home.html", {'items': employees})

def search_view(req):
  query = req.GET['second_name']
  employees = Employee.objects.filter(second_name=query)
  return render(req, "search.html", {'items': employees, 'search_query': query})