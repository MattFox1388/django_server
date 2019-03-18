from django.shortcuts import render
from django.views import View
from .forms import SearchForm
# Create your views here.


class HomeView(View):
    template_name = 'index.html'
    search_form = SearchForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.search_form})

    def post(self, request):
        pass
