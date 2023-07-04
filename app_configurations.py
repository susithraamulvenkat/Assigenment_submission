# CONFIG PARSER
import configparser
import logging

# Configure the logger
logger = logging.getLogger(__name__)

parser = configparser.ConfigParser()
parser.read(r'C:\Users\susithra.v\PycharmProjects\movie_rating_system\configuration\application.conf')
mongodb = parser.get('Mongodb', 'mongo_uri')
db = parser.get('Mongodb', 'db')

