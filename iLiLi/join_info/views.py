from django.shortcuts import render


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
    return render(request, "join_info/join_form.html", context)