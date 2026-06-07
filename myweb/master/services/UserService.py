from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from master.Entity.UserProfile import UserProfile
from master.Repository.UserRepo import UserRepo


class UserService:

    repo = UserRepo()

    def signup(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        contact = request.POST['contact']
        question = request.POST['question']
        answer = request.POST['answer']

        if User.objects.filter(username=username).exists():
            return "Username already exists"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        profile = UserProfile()

        profile.user_id = user.id
        profile.contact = contact
        profile.security_question = question
        profile.security_answer = answer

        self.repo.saveProfile(profile)

        return "Account created successfully"
    
    def signin(self, request):

        username = request.POST['username']
        password = request.POST['password']

        print("USERNAME =", username)
        print("PASSWORD =", password)

        user = authenticate(
            username=username,
            password=password
        )

        print("USER =", user)

        return user
