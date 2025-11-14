from UserRepository import UserRepository
from User import User
from AuthService import AuthService

# короче я думаю можно сделать отдельную папку с зареганными пользователями, чтобы не мучиться с добавлением параметра signed_in
# в файл json надо переделать ещё каррент юзера навреное хз вообще в чём смысл этого метода надо разобраться
# вроде всё

user1 = User(id=1213, name="Name", login="CoolNickname", password="219748137", address="Home")
user2 = User(id=9124, name="OtherName", login="OtherUser", password="0000011111", address="OtherHome")
repo = UserRepository("labs/lab_5/Data")

repo.add(user1)

print(repo.get_all())
user1.login = "VeryCoolNickname"
repo.update(user1)
print(repo.get_all())

authservice = AuthService(repo)

authservice.sign_in(user1)
authservice.current_user(user2)

repo.delete(user1)
print(repo.get_all())
