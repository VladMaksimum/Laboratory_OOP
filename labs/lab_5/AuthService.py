from IAuthService import IAuthService
from User import User
from UserRepository import UserRepository


class AuthService(IAuthService):
    def __init__(self, signed_repository: UserRepository, unsigned_repository: UserRepository) -> None:
        self._signed = signed_repository
        self._unsigned = unsigned_repository

        self._current: User | None = None

    def sign_in(self, user: User) -> None:
        self._unsigned.delete(user)
        self._signed.add(user)

        self._current = user

    def sign_out(self, user: User) -> None:
        self._signed.delete(user)
        self._unsigned.add(user)

        self._current = None
    
    def is_authorized(self, user: User) -> bool:
        return self._signed.get_by_id(user.id) != None

    def current_user(self, user: User) -> None:
        self._current = user
