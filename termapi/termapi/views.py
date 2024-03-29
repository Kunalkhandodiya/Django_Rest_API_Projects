from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this decorator if you're not using CSRF token in your API

import pickle

@csrf_exempt  # Use this decorator if you're not using CSRF token in your API
def linear_api(request):
    if request.method == 'POST':
        result = 0
        try:
            data = request.POST  # Assuming data is sent in form-data format
            a = int(data.get('n1'))

            with open('E:/Django_apps/simplecalulator/pickle_file/LRmodel.pkl', 'rb') as f:
                model = pickle.load(f)
                result = model.predict([[a]])

        except (ValueError, TypeError, ZeroDivisionError):
            pass

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)