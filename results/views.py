import sys
sys.path.append("..")
from sabackend import SABackend
from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from django.http import Http404, HttpResponse, FileResponse
from django.utils.html import escape
# Create your views here.

db = SABackend(host='ceas-e384d-dev1.cs.uwm.edu',dbname='documentorganizer',
                        user='doc_org',password='d3NXWWfyHT',port='5432')


class HomeView(View):
    template_name = 'index.html'
    search_form = SearchForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.search_form, 'resultFiles': []})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_phrase = escape(form.cleaned_data['search_phrase'])
            print("search phrase: " + search_phrase)
            documents = db.get(search_phrase)
            return render(request, self.template_name, {'form': self.search_form, 'resultFiles': documents})
        else:
            print(form.errors)
            raise Http404


class DetailsView(View):
    template_name = 'inspect.html'

    def get(self, request, id):
        document = db.get_doc_by_id(id)
        # file stats
        path = document.get_file_path()
        num_words = document.get_num_words()
        file_size = document.get_file_size()
        date_create = document.get_create_date()
        date_edit = document.get_edit_date()
        # get file dups
        duplicate_docs = db.get_duplicates_of(document)
        print('dups: ' + duplicate_docs)
        # get file tags
        tags = document.get_tags()
        print('tags: ' + tags)
        return render(request, self.template_name, {'path': path, 'num_words': num_words, 'file_size': file_size,
                                                    'date_create': date_create, 'date_edit': date_edit,
                                                    'dups': duplicate_docs, 'tags': tags})

    def post(self, request):
        pass