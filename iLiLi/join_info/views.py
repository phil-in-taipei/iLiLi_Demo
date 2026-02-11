from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentQuestionnaireForm

def join_form(request, *args, **kwargs):
    #form = UserLoginForm(request.POST or None)
    #if form.is_valid():
    #    username_ = form.cleaned_data.get('username')
    #    user_obj = User.objects.get(username__iexact=username_)
    #    login(request, user_obj) # landing-page/welcome-page/
    #    user_profile = UserProfile.objects.filter(user=user_obj).first()
    #    if user_profile:
    #        return HttpResponseRedirect("/landing/welcome") # redirect to a landing page
    #    else:
    #        return HttpResponseRedirect("/user-profiles/create-profile") # redirect to a landing page
    context = {} #{"form": form}
    return render(request, "join_info/join_page.html", context)


def questionnaire_form(request):
    if request.method == 'POST':
        form = StudentQuestionnaireForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('join_info:success'))
    else:
        form = StudentQuestionnaireForm()

    context = {
        "form": form,
    }
    template = "join_info/join_form.html"
    return render(request, template, context)


def questionnaire_success(request):
    template = "join_info/join_success.html"
    return render(request, template)
