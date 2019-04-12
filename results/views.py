from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from django.http import Http404
from django.utils.html import escape
import sys
sys.path.append("..")
from sabackend import SABackend
# Create your views here.

db = SABackend(host='ceas-e384d-dev1.cs.uwm.edu',dbname='documentorganizer',
                        user='doc_org',password='d3NXWWfyHT',port='5432')


class HomeView(View):
    template_name = 'index.html'
    search_form = SearchForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.search_form})

    def post(self, request):
        print('here')
        form = SearchForm(request.POST)
        if form.is_valid():
            search_phrase = escape(form.cleaned_data['search_phrase'])
            print("search phrase: " + search_phrase)
            print("file options: ")
            print(escape(form.cleaned_data['files']))
            # TODO: add call to database and then update table
            documents = db.get(search_phrase)
            for doc in documents:
                print(doc.get_file_path())
                print(doc.get_file_size())
        else:
            print(form.errors)
            raise Http404
