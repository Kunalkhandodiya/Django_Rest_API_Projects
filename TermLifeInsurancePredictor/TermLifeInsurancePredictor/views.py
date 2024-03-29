from django.shortcuts import render
import pickle


def linear(request):
    result=0
    try:

        a=int(request.GET.get('n1'))

        with open('E:/Django_apps/simplecalulator/pickle_file/LRmodel.pkl','rb') as f:
            model=pickle.load(f)

            result=model.predict([[a]])

    except (ValueError, TypeError, ZeroDivisionError):
        pass        

    return render(request, "templates/index.html", {'result': result})
    