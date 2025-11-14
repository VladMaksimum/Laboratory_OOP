from IAuthService import IAuthService
from User import User
from UserRepository import UserRepository


class AuthService(IAuthService):
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository
        self._current: User | None = None

    def sign_in(self, user: User) -> None:
        self._repository.add(user)
        self._current = user

    def sign_out(self, user: User) -> None:
        self._repository.delete(user)
        self._current = None
    
    def is_authorized(self, user: User) -> bool:
        return self._current == user

    def current_user(self) -> User | None:
        return self._current
