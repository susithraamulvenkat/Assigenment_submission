from fastapi import APIRouter
from scripts.core.handlers import movie_handlers
from scripts.core.handlers.movie_handlers import add_user_account,login,add_movie,get_movie,update_movie,delete_movie,booking,rating,specfic_rating,search_movie
from schemas.models import movie, user, user_booking_movie, user_rating

movie_router = APIRouter()

@movie_router.post("/create_user_account")
async def create_user_account(usr: user):
    try:
        return await add_user_account(usr)
    except Exception as e:
        return {"Error": str(e)}

@movie_router.post("/user_login")
async def user_login(user_id: int):
    try:
        return await login(user_id)
    except Exception as e:
        return {"Error":str(e)}


@movie_router.post("/adding_movie")
async def adding_movie(mov: movie):
    try:
        return await add_movie(mov)
    except Exception as e:
        return {"Error":str(e)}


@movie_router.get("/retrieve_movie")
async def retrieve_movie(movie_id: int):
    try:
        return await get_movie(movie_id)
    except Exception as e:
        return {"Error": str(e)}



@movie_router.put("/updating_movie")
async def updating_movie(movie_id: int,mov: movie):
    try:
        return await update_movie(movie_id,mov)
    except Exception as e:
        return {"Error": str(e)}


@movie_router.delete("/deleting_movie")
async def deleting_movie(movie_id: int):
    try:
        return await delete_movie(movie_id)
    except Exception as e:
        return {"Error": str(e)}

@movie_router.post("/user_booking")
async def user_booking(movie_name: str, book: user_booking_movie):
    try:
        return await booking(movie_name, book)
    except Exception as e:
        return {"Error": str(e)}

@movie_router.post("/user_rating")
async def user_rating(movie_name: str, rate: user_rating):
    try:
        return await rating(movie_name, rate)
    except Exception as e:
        return {"Error": str(e)}

@movie_router.get("/get_specfic_movie")
async def get_specfic_movie(user_id: int):
    try:
        return await specfic_rating(user_id)
    except Exception as e:
        return {"Error": str(e)}

@movie_router.get("/movie_searching")
async def movie_searching(movie_name:str):
    try:
        return await search_movie(movie_name)
    except Exception as e:
        return {"Error": str(e)}

