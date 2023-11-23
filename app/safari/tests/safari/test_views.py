from django.test import RequestFactory
from django.template.response import TemplateResponse
from django.urls import reverse
from safari.views import index

def test_index_view():
    factory = RequestFactory()
    index_url = reverse('index')
    request = factory.get(index_url)
    response = index(request)
    
    assert response.status_code == 200