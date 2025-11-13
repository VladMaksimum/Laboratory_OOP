from IDataRepository import IDataRepository

class IUserRepository(IDataRepository[User]):
    def get_by_login(self, login: str) -> User | None:
        ...