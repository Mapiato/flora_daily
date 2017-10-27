from django.shortcuts import render

# Create your views here.
def flora_daily(request):
    return render(request, 'flora_daily/lookup.html', {})
