import sys
import json
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
            # set initial search phrase for form to what was searched
            form.fields['search_phrase'].initial = search_phrase
            print('Search Op: ' + form.cleaned_data['search_by'])
            documents = db.get(search_phrase)
            return render(request, self.template_name, {'form': form, 'resultFiles': documents})
        else:
            print(form.errors)
            raise Http404


class DetailsView(View):
    template_name = 'inspect.html'

    def get(self, request, id):
        document = db.get_doc_by_id(id)
        print(document)
        # file stats
        path = document.get_file_path()
        num_words = document.get_num_words()
        file_size = document.get_file_size()
        date_create = document.get_create_date()
        date_edit = document.get_edit_date()
        # get file dups
        duplicate_docs = db.get_duplicates_of(document)
        # get file tags
        tags = document.get_tags()
        tagStr = ""
        for tag in tags:
            tagStr += tag + ','
        print(tagStr)
        return render(request, self.template_name, {'path': path, 'num_words': num_words, 'file_size': file_size,
                                                    'date_create': date_create, 'date_edit': date_edit,
                                                    'dups': duplicate_docs, 'tags': tagStr})

    def post(self, request, id):
        # add tag
        document = db.get_doc_by_id(id)
        curTags = db.get_tags(document)
        tagInput = request.POST["tagInput"]
        print("Here 1")
        print(tagInput)
        tagInput = tagInput.split(',')
        for tag in tagInput:
            if tag not in curTags:
                db.add_tag(id, tag)
                print("Tag added to document: " + tag)
        for tag in curTags:
            if tag not in tagInput:
                db.remove_tag(document, tag)
                print("Tag removed from document: " + tag)
        # reload page
        document = db.get_doc_by_id(id)
        # file stats
        path = document.get_file_path()
        num_words = document.get_num_words()
        file_size = document.get_file_size()
        date_create = document.get_create_date()
        date_edit = document.get_edit_date()
        # get file dups
        duplicate_docs = db.get_duplicates_of(document)
        # get file tags
        tags = db.get_tags(document)
        print("Tags: ")
        print(tags)
        tagStr = ""
        for tag in tags:
            tagStr += tag + ','
        print(tagStr)
        return render(request, self.template_name, {'path': path, 'num_words': num_words, 'file_size': file_size,
                                                    'date_create': date_create, 'date_edit': date_edit,
                                                    'dups': duplicate_docs, 'tags': tagStr})
