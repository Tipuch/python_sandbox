from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import get_language
from django.http import HttpResponse


class TestLanguageView(View):
    def get(self, request):
        print(get_language())
        return HttpResponse(status=200)
