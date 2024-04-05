from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import CatFact
from .tasks import fetch_cat_fact

@api_view(['GET'])
def health_check(request):
    return JsonResponse({'status': 'healthy'}, status=200)

@api_view(['POST'])
def fetch_fact(request):
    fetch_cat_fact.send()
    return JsonResponse({'success': True})

@api_view(['GET'])
def get_fact(request):
    try:
        fact = CatFact.objects.latest('id')
        return JsonResponse({'fact': fact.fact})
    except CatFact.DoesNotExist:
        return JsonResponse({'error': 'no_task_has_been_queued'}, status=404)
