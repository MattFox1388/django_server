from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from django.http import Http404
from django.utils.html import escape
from sabackend import SABackend
# Create your views here.


class HomeView(View):
    template_name = 'index.html'
    search_form = SearchForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.search_form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_phrase = escape(form.cleaned_data['search_phrase'])
            print("search phrase: " + search_phrase)
            print("file options: ")
            for item in escape(form.cleaned_data['files']):
                print(item)
            # TODO: add call to database and then update table
            # SABackend.__init__() #Don't have database information saved, need to add that.
            documents = SABackend.get(search_phrase)
        else:
            raise Http404
