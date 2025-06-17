from django.shortcuts import HttpResponse


def test_view(request):
    return HttpResponse(
        {
            'test': 'testando teste do teste'
        }
        )
