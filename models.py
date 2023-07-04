from pydantic import BaseModel


class user(BaseModel):
    user_id: int
    user_name: str
    user_password: str


class login(BaseModel):
    user_id: int
    password: str


class movie(BaseModel):
    movie_id: int
    movie_name: str
    movie_cost: int


class user_booking_movie(BaseModel):
    user_id: int
    user_name: str
    movie_name: str
    movie_cost: int


class user_rating(BaseModel):
    user_id: int
    movie_name: str
    user_rating: int





