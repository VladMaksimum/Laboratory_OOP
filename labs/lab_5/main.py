from UserRepository import UserRepository
from DataRepository import DataRepository
from User import User
from AuthService import AuthService


user1 = User(id=1213, name="Name", login="CoolNickname", password="219748137", address="Home")
user2 = User(id=9124, name="OtherName", login="OtherUser", password="0000011111", address="OtherHome")
repo_sgn = UserRepository("labs/lab_5/signed")
repo_unsgn = UserRepository("labs/lab_5/unsigned")

repo_unsgn.add(user1)

print(repo_unsgn.get_all()[0].login)
user1.login = "VeryCoolNickname"
repo_unsgn.update(user1)
print(repo_unsgn.get_all()[0].login)

authservice = AuthService(repo_sgn, repo_unsgn)

# authservice.sign_in(user1)
authservice.current_user(user2)

if authservice.is_authorized(user1):
    print("Hello again")


