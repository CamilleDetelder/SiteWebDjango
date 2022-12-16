from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

User = get_user_model()


# Create your views here.
# récupérer les données  utilisateurs depuis page sign up :
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # créer utilisateur :
        user = User.objects.create_user(username=username, password=password)
        # connecter utilisateur et redirige vers page d'accueil:
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html')
