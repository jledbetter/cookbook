from django.views.generic.simple import direct_to_template

def homepage(request):
    # Return an http response that serves the index.html template
    return direct_to_template(request, 'homepage/index.html')