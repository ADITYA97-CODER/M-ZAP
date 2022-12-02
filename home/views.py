from django.shortcuts import render
from . import k
def home(request):
    name = ['apple','bannana','mixed','orange']
    if request.method == "POST":
        img = request.FILES['image']
        predictions = k.pred(img=img)
        context = {'name':predictions.tag_name,'probability':predictions.probability}

        return render(request,'home.html',context=context)

    return render(request,'home.html')