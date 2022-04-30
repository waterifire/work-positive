from django.shortcuts import render, redirect
from django.utils import timezone

from django.db.models import Q

from .models import Hobby, HobbyList
from .forms import HobbyListForm, HobbyForm

# Create your views here.

def hobby_home(request):
    hobbies_all = HobbyList.objects.all()
    # hobbies = HobbyList.objects.filter()
    hl_form = HobbyListForm()
    h_form = HobbyForm()

    hobbies_list = []
    hobbies_list1 = []
    for i in hobbies_all:
        hobbies_list.append(i.hobbylist_name)
        hobbies_list1.append(i)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    hobbies = HobbyList.objects.filter(
        Q(hobbylist_name__icontains=q)
    )

    if request.method == "POST":
        if 'hobby_add' in request.POST:
            if request.POST['hobbylist_name'].lower() not in hobbies_list:

                # print(f"{request.POST['hobbylist_name']} --- {type(request.POST['hobbylist_name'])}")
                # print(list(hobbies_all))
                # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                # for ho in hobbies_all:
                #     print(f"{ho.hobbylist_name}  --- {type(ho.hobbylist_name)}")
                hl_form = HobbyListForm(request.POST)
                if hl_form.is_valid():
                    form1 = hl_form.save(commit=False)
                    form1.hobbylist_name = form1.hobbylist_name.lower()
                    form1.created_by = request.user
                    form1.save()
                    ls_hobbies_temp = [form1.created_by.id]
                    for i in hobbies:
                        if i.hobbylist_name == form1.hobbylist_name:
                            h_form = HobbyForm({'hobby_user':ls_hobbies_temp, 'hobby_name': i.id, 'updated': timezone.now()})
                            if h_form.is_valid():
                                h_form.save()

                    return redirect(request.path_info)
            else:
                # print("Already there##############################")
                user_hobby_request = request.POST['hobbylist_name'].lower()
                num = 0
                for i in hobbies_list:
                    if user_hobby_request == i:
                        break
                    else:
                        num += 1
                hobby_specific_query = Hobby.objects.filter(hobby_name=hobbies_list1[num].id)  # getting the hobby by id that is entered by user
                for i in hobby_specific_query:
                    instance_made = i  # have the hobby (now its not in a query type)
                h_form = HobbyForm({'hobby_user': instance_made.hobby_user.add(request.user), 'hobby_name': instance_made.id, 'updated': timezone.now()}, instance=instance_made)
                if h_form.is_valid():
                    h_form.save()
                    return redirect(request.path_info)
                # //TODO: Add flash message saying you joined it



    context = {'hobbies': hobbies, 'hl_form': hl_form,}
    response = render(request, 'hobby/hobby_home.html', context)
    return response


def hobby_area(request, pk):
    hobby = HobbyList.objects.get(id=pk)
    hobby_details = Hobby.objects.filter(hobby_name=hobby)
    hobby_specific = Hobby.objects.filter(hobby_name=pk)
    for i in hobby_specific:
        instance_made = i
    h_form = HobbyForm(instance=instance_made)
    if request.method == "POST":
        if 'hobby_join' in request.POST:  # if someone clicked "join"
            # in line below: we just adding this user to the hobby selected
            h_form = HobbyForm({'hobby_user': instance_made.hobby_user.add(request.user.id), 'hobby_name': pk, 'updated': timezone.now()}, instance=instance_made)
            if h_form.is_valid():
                h_form.save()
                return redirect('hobby_home')  # //TODO: make sure this redirect works
        elif 'hobby_leave' in request.POST:
            h_form = HobbyForm({'hobby_user': instance_made.hobby_user.remove(request.user.id), 'hobby_name': pk, 'updated': timezone.now()}, instance=instance_made)
            if h_form.is_valid():
                h_form.save()
                return redirect('hobby_home')
    context = {'instance_made': instance_made,'hobby': hobby, 'hobby_details': hobby_details,}
    response = render(request, 'hobby/hobby_area.html', context)
    return response
