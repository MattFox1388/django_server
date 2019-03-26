from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from django.http import Http404
from django.utils.html import escape
# Create your views here.


class HomeView(View):
    template_name = 'index.html'
    search_form = SearchForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.search_form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            print("search phrase: " + escape(form.cleaned_data['search_phrase']))
            print("file options: ")
            for item in escape(form.cleaned_data['files']):
                print(item)
            # TODO: add call to database and then update table

        else:
            raise Http404
