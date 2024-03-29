from django.http import JsonResponse
from rest_framework.decorators import api_view
import pickle

@api_view(['POST'])
def calculate(request):
    """
    Calculates the sum of two numbers.
    """
    data = request.data
    num1 = data['num1']
    num2 = data['num2']
    opt = data['opt']

    if opt=='Add':
      result = num1 + num2
    elif opt=="Sub":
       result =num1-num2  
    elif opt=="Mul":
       result =num1*num2
    elif opt=="Div":
       result =num1/num2
    else:
       result="Wrong operation you Enterd"      
       
    return JsonResponse({'result': result})

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
def linear_api(request):
    try:
        with open('E:/Django_apps/simplecalulator/pickle_file/LRmodel.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        return JsonResponse({'error': 'Model file not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    data = request.data
    num1 = int(data.get('Age'))

    result = model.predict([[num1]])
    return JsonResponse({'result': result.tolist()})
