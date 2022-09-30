from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.all().prefetch_related('teacher')
    result = students.order_by(ordering)
    context = {'object_list': result}

    return render(request, template, context)