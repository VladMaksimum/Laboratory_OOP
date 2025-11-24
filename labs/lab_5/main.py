from UserRepository import UserRepository
from User import User
from AuthService import AuthService

user1 = User(id=12345, name="Name", login="OriginalLogin", password="0000")
repo_in = UserRepository("labs/lab_5/users_active")
repo_out = UserRepository("labs/lab_5/users_inactive")

auth_service = AuthService(repo_in, repo_out)

#auth_service.sign_in(user1)
#auth_service.sign_out(user1)

if auth_service.is_authorized(user1):
    print("Hello again")
