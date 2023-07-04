
from schemas.models import movie, user,user_booking_movie,user_rating
from scripts.utility.mongo_utility import collection_one, collection_two, collection_three,collection_four
from scripts.core.db.mongodb import Mongodb
from scripts.logging.logs.logger import logger


obj = Mongodb()

async def add_user_account(usr: user): #db2 #collection_one
    try:
        collection_one.insert_one(usr.dict())
        logger.debug("user details are added successfully")
        return{"note": "user account created successfully "}
    except Exception as e:
        return {"Error":str(e)}

async def login(user_id: int): #db2 #collection_one
    try:
        if collection_one.find_one({"user_id": user_id}):
            logger.debug("user login successfully")
            return{"msg":"welcome user successfully login"}
        else:
            logger.debug("user details not found in the database")
            return{"sorry,user details are not there in the database ! try again or create account do again to login "}
    except Exception as e:
        logger.error(f"An error occured during login:str(e)")
        return{"message":"An error occured during login.Please try again later"}

async def add_movie(mov: movie): #db3 #collection_two
    try:
        collection_two.insert_one(mov.dict())
        logger.debug("movies details are added successfully")
        return {"note": "movie details are stored successfully"}
    except Exception as e:
        return {"Error":str(e)}


async def get_movie(movie_id: int): #db3 #collection_two
    try:
        find = collection_two.find_one({"movie_id": movie_id})
        if find:
            return{

                "movie_id": find["movie_id"],
                "movie_name": find["movie_name"],
                "movie_cost": find["movie_cost"]

                 }
        else:
            logger.debug("sorry i cant find this movie id")
            return {"we can't able to find this movie!I think this movie name not exist"}
    except Exception as e:
        logger.error(f"An error occured during movie retrive:str(e)")
        return {"message": "An error occured during movie retrive.Please try again later"}


async def update_movie(movie_id: int, mov: movie): #db3 #collection_two
    mov_up = collection_two.find_one({"movie_id": movie_id})
    try:
        if mov_up:
            collection_two.update_one({"movie_id": movie_id}, {"$set": mov.dict()})
            logger.debug("successfully movie details are updated")
            return{"note": "movie details are successfully  updated in the database "}
        else:
            logger.debug("sorry i cant find this movie in the database")
            return{"This movie details are not there in the database "}

    except Exception as e:
        logger.error(f"An error occured during movie update:str(e)")
        return {"message": "An error occured during movie update.Please try again later"}


async def delete_movie(movie_id: int): #db3 #collection_2
    mov_del = collection_two.find_one({"movie_id": movie_id})
    try:
        if mov_del:
            collection_two.delete_one({"movie_id": movie_id})
            logger.debug("movie is removed successfully ")
            return {"note": "movie details are removed successfully"}
        else:
            logger.debug("sorry i cant find this movie ")
            return {"movie details are not found"}
    except Exception as e:
        logger.error(f"An error occured during movie delete:str(e)")
        return {"message": "An error occured during movie delete.Please try again later"}

async def booking(movie_name: str, book: user_booking_movie): #db4 #cllection_three
    find = collection_two.find_one({"movie_name": movie_name})
    try:
        if find:
            collection_three.insert_one(book.dict())
            logger.debug("user booked movie successfullly")
            return {"welcome to movie": " user successfully booked movie"}
        else:
            logger.debug("sorry you  cant book this movie ")
            return {"movie details are not found"}
    except Exception as e:
        logger.error("error occured during booking:str(e)")
        return {"message": "An error occured during movie booking.Please try again later"}


async def rating(movie_name: str, rate: user_rating): # db5 #cllection_four
    find = collection_two.find_one({"movie_name": movie_name})
    try:
        if find:
            collection_four.insert_one(rate.dict())
            logger.debug("user successfully gives rating for that movie ")
            return {"note": "successfully user gives rating for that movie"}
        else:
            logger.debug("sorry you cant able to give rating to this movie ")
            return {"movie details are not found"}
    except Exception as e:
        logger.error("error occured during rating:str(e)")
        return {"message": "An error occured during movie giving rating to the movie.Please try again later"}


async def specfic_rating(user_id: int):
    spv_mov = collection_four.find_one({"user_id": user_id })
    try:
        if spv_mov:
            return {"user_id": spv_mov["user_id"],
                    "movie_name": spv_mov["movie_name"],
                    "user_rating": spv_mov["user_rating"]
                    }
            logger.debug("we are  successfully find the rating for this movie")

        else:
            logger.debug("sorry i cant find this movie ")
            return {"movie details are not found"}
    except Exception as e:
        logger.error("error occured during finding specfic movie:str(e)")
        return {"message": "An error occured during finding specific movie.Please try again later"}

async def search_movie(movie_name: str):
    src_mov = collection_two.find_one({"movie_name": movie_name})
    try:
        if src_mov:
            return{"movie_id": src_mov["movie_id"],
                   "movie_name": src_mov["movie_name"],
                   "movie_cost": src_mov["movie_cost"]

            }
            logger.debug("movie name searched successfully")
        else:
            logger.debug("sorry i cant find this movie ")
            return {"movie details are not found"}
    except Exception as e:
        logger.error("error occured during searching:str(e)")
        return {"message": "An error occured during searching the movie.Please try again later"}



