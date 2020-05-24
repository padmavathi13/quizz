from django.shortcuts import render
from quizz.forms import SignupForm
def home_page_view(request):
    return render(request,'quizz/home.html')
@login_required
def Science_quizz_view(request):
    return render(request,'quizz/sciencequizz.html')
def logout_view(request):
    return render(request,'quizz/logout.html)'
def signup_view(request):
    form=forms.SignupForm()
    my_dict={'form':form}
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse Redirect('/accounts/login')
        return render(request,'quizz/signup.html',context=my_dict)
