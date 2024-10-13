from peewee import Model, MySQLDatabase, AutoField, CharField  # type: ignore
from config.settings import DATABASE

print(DATABASE)

# Configure the MySQL database connection
database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=int(DATABASE["port"]),
)


# pylint: disable=too-few-public-methods
class UserModel(Model):
    id_user = AutoField(primary_key=True)
    username = CharField(max_length=50, unique=True)
    name = CharField(max_length=80)
    lastname = CharField(max_length=80)
    email = CharField(max_length=255)
    password = CharField(max_length=50)
    profile_picture = CharField(max_length=255, null=True)
    type_user = CharField(max_length=80)

    class Meta:
        database = database
        table_name = "user"


class rol(Model):
    id_rol = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "rol"
