from peewee import DoesNotExist
from config.database import UserModel


class UserService:
    @staticmethod
    def create_user(user_data: UserModel) -> UserModel:
        if UserModel.select().where(UserModel.username == user_data.username).exists():
            raise ValueError("User already exists")

        new_user = UserModel(
            username=user_data.username,
            name=user_data.name,
            lastname=user_data.lastname,
            email=user_data.email,
            password=user_data.password,
            profile_picture=user_data.profile_picture,
            type_user=user_data.type_user,
        )
        new_user.save()
        return new_user

    @staticmethod
    def get_user_by_id(id_user: int) -> UserModel:
        try:
            return UserModel.get(UserModel.id_user == id_user)
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc

    @staticmethod
    def get_all_users() -> list[UserModel]:
        return list(UserModel.select())

    @staticmethod
    def update_user(user_data: UserModel) -> UserModel:
        try:
            existing_user = UserModel.get(UserModel.id_user == user_data.id_user)
            existing_user.username = user_data.username
            existing_user.name = user_data.name
            existing_user.lastname = user_data.lastname
            existing_user.email = user_data.email
            existing_user.password = user_data.password
            existing_user.profile_picture = user_data.profile_picture
            existing_user.type_user = user_data.type_user
            existing_user.save()
            return existing_user
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc

    @staticmethod
    def delete_user(id_user: int) -> None:
        try:
            user = UserModel.get(UserModel.id_user == id_user)
            user.delete_instance()
            return True
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc
