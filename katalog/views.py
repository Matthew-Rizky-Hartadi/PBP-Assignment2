from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_katalog(request):
    katalog_item = CatalogItem.objects.all()
    context = {
        'name': 'Matthew Rizky Hartadi',
        'student_id': 2106720941,
        'katalog_list': katalog_item 
    } 

    return render(request, 'katalog.html', context)
