from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import registration
from enroll.models import user
# Create your views here.


# This function will add and show data
def add_show(request):
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            ps = form.cleaned_data['password']
            reg = user(name=nm, email=em, password=ps)
            reg.save()
            form = registration()
    else:
        form = registration()
        
    stud = user.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':form, 'stud':stud})


# This function will delete data
def delete_data(request, id):
    if request.method == "POST":
        user_id = user.objects.get(pk=id)
        user_id.delete()
        return HttpResponseRedirect('/enroll/show/')
    
    
# This function will edit the data
def update_data(request, id):
    if request.method == 'POST':
        user_id = user.objects.get(pk=id)
        form = registration(request.POST, instance=user_id)
        if form.is_valid():
            form.save()
    else:
        user_id = user.objects.get(pk=id)
        form = registration(instance=user_id)
    return render(request, 'enroll/update.html', {"form": form})