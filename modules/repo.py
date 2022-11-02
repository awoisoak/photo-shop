import os, mysql.connector, modules.utils as utils
from queue import Empty
from mysql.connector import errorcode
from pathlib import Path


#Allow to set the database url as environment variable.
database_url = os.environ.get('DATABASE_URL', 'localhost')
print ("Database URL: ", database_url)

# Attempt to get the list of images from the Database, 
# if it can't connect it will grab them from local directory
# return a list with list[boolean, string..] where:
#   boolean: true if images were retrived from db, false otherwise
#   string..: images names
def getImages():
    response = []
    images = __getDbImages()
    if images:
        utils.printSuccess ("images retrieved from DB")
        response.insert(0, True)
        response.insert(1, images)
        return response
    else:
        utils.printWarning ("images retrieved locally")
        images = __getLocalImages()
        response.insert(0, False)
        response.insert(1, images)
        return response


# Get the list of images from the database (which runs in another container)
def __getDbImages():
    imageUrls = []
    try:
        # Database information (including hostname and name) is defined in docker-compose file
        cnx = mysql.connector.connect(user='user', password='password',
                                    host= database_url,
                                    database='photosdb')

        cursor = cnx.cursor()
        query = ("SELECT image_url from photos")
        cursor.execute(query)

        imageUrls = [row[0] for row in cursor.fetchall()]

        cursor.close()
    except mysql.connector.Error as err:
        utils.printError("Error connecting to the db :(")
        utils.printError(err.msg)
    else:
        utils.printSuccess("Connection success! :)")
        cnx.close()
    print(imageUrls)
    return imageUrls    

# Get the list of images directly from the local directory
def __getLocalImages():
    return utils.filterImages(os.listdir('./images'))     