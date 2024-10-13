from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from app.config.settings import DATABASE 

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    name = Column(String(80))
    lastname = Column(String(80))
    email = Column(String(255))
    password = Column(String(50))
    profile_picture = Column(String(255))
    type_user = Column(String(80))

    # Relationships
    favorites = relationship("Favorities", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    recipes = relationship("Recipe", back_populates="user")
    pantry_items = relationship("Pantry", back_populates="user")
    shopping_lists = relationship("ShoppingList", back_populates="user")
    user_groups = relationship("UserGroup", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(String(50))
    id_user = Column(Integer, ForeignKey("users.id_user"))


class Rol(Base):
    __tablename__ = "rol"
    id_rol = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)


class Category(Base):
    __tablename__ = "category"
    id_category = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)


class RecipeCategory(Base):
    __tablename__ = "recipe_category"
    id_recipe = Column(Integer, ForeignKey("recipe.id_recipe"), primary_key=True)
    id_category = Column(Integer, ForeignKey("category.id_category"), primary_key=True)


class Favorities(Base):
    __tablename__ = "favorities"
    id_favorities = Column(Integer, primary_key=True, index=True)
    id_recipe = Column(Integer, ForeignKey("recipe.id_recipe"))
    id_user = Column(Integer, ForeignKey("users.id_user"))

    # Relationships
    recipe = relationship("Recipe", back_populates="favorites")
    user = relationship("User", back_populates="favorites")


class Group(Base):
    __tablename__ = "group"
    id_group = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)


class Ingredient(Base):
    __tablename__ = "ingredient"
    id_ingredient = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    expiration_date = Column(String(50))
    id_nutrition_info = Column(Integer, ForeignKey("nutrition_info.id_nutrition_info"))


class Menu(Base):
    __tablename__ = "menu"
    id_menu = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    id_typeMenu = Column(Integer, ForeignKey("type_menu.id_typeMenu"))


class TypeMenu(Base):
    __tablename__ = "type_menu"
    id_typeMenu = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    type = Column(String(50))


class Notification(Base):
    __tablename__ = "notification"
    id_notification = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(String(50))
    id_user = Column(Integer, ForeignKey("users.id_user"))

    # Relationships
    user = relationship("User", back_populates="notifications")


class NutritionInfo(Base):
    __tablename__ = "nutrition_info"
    id_nutrition_info = Column(Integer, primary_key=True, index=True)
    kcal = Column(String(50))
    protein = Column(String(50))
    fat = Column(String(50))
    carbs = Column(String(50))


class Pantry(Base):
    __tablename__ = "pantry"
    id_pantry = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    id_ingredient = Column(Integer, ForeignKey("ingredient.id_ingredient"))
    id_user = Column(Integer, ForeignKey("users.id_user"))
    id_quantity = Column(Integer, ForeignKey("quantity.id_quantity"))
    expiration_date = Column(String(50))

    # Relationships
    ingredient = relationship("Ingredient")
    user = relationship("User", back_populates="pantry_items")
    quantity = relationship("Quantity")


class Quantity(Base):
    __tablename__ = "quantity"
    id_quantity = Column(Integer, primary_key=True, index=True)
    grammes = Column(String(50))
    liters = Column(String(50))


class RecipeMenu(Base):
    __tablename__ = "recipe_menu"
    id_recipe = Column(Integer, ForeignKey("recipe.id_recipe"), primary_key=True)
    id_menu = Column(Integer, ForeignKey("menu.id_menu"), primary_key=True)


class Recipe(Base):
    __tablename__ = "recipe"
    id_recipe = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(50))
    instructions = Column(String(50))
    preparation_time = Column(String(50))
    status = Column(String(50))
    difficulty = Column(String(50))
    id_user = Column(Integer, ForeignKey("users.id_user"))
    id_quantity = Column(Integer, ForeignKey("quantity.id_quantity"))

    # Relationships
    user = relationship("User", back_populates="recipes")
    favorites = relationship("Favorities", back_populates="recipe")
    recipe_categories = relationship("RecipeCategory", back_populates="recipe")
    recipe_menus = relationship("RecipeMenu", back_populates="recipe")


class ShoppingList(Base):
    __tablename__ = "shopping_list"
    id_shopping_list = Column(Integer, primary_key=True, index=True)
    status = Column(String(50))
    total_items = Column(String(50))
    creation_date = Column(String(50))
    id_user = Column(Integer, ForeignKey("users.id_user"))
    id_quantity = Column(Integer, ForeignKey("quantity.id_quantity"))

    # Relationships
    user = relationship("User", back_populates="shopping_lists")
    quantity = relationship("Quantity")
    ingredient = relationship("Ingredient")

DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)