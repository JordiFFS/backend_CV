from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.
# 404
def not_found_view(request, exception=None):
    if not request.path.endswith('/'):
        return HttpResponsePermanentRedirect(request.path + '/')
    return render(request, '404.html',context={'backend':'https://fastcv.myvnc.com/'}, status=404)
