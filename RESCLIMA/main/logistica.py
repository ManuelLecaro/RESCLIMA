# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.conf import settings

from main.forms import *
from main.models import *
from main.utils import copy_csv_logistica

@login_required(login_url='noAccess')
def LogisticaCreate(request):
	if request.method == 'POST' and request.FILES['file']:
		file = request.FILES['file']
		copy_csv_logistica(file, request.user)
		return HttpResponseRedirect('/data/')
	return render(request, 'main/logistica/form.html')


class LogisticaList(TemplateView):
    template_name = 'main/logistica/list.html'

    def get_context_data(self, **kwargs):
        context = super(LogisticaList, self).get_context_data(**kwargs)
        try:
            context['object_list'] = Logistica.objects.filter(user=self.request.user).order_by('id')
        except Logistica.DoesNotExist:
            context['object_list'] = None
        return context

# No se esta usando por el momento
class LogisticaUpdate(UpdateView):
	model = Logistica
	form_class = LogisticaForm
	template_name = 'main/logistica/form.html'
	success_url = reverse_lazy('logistica_list')

	def form_valid(self, form):
		form.instance.user =  self.request.user.id
		return super(LogisticaUpdate, self).form_valid(form)

# No se esta usando por el momento
class LogisticaDelete(DeleteView):
	model = Logistica
	template_name = 'main/logistica/delete.html'
	success_url = reverse_lazy('logistica_list')

# No se esta usando por el momento
class LogisticaShow(DetailView):
	model = Logistica
	template_name = 'main/logistica/show.html'
