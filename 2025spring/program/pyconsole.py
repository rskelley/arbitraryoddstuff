import json
""" 

Problem statement 

Collect and save a list of media items from users 
Collect the name, year, artist and genre and type 
If the item is a book, ask whether it’s paperback, hardback of ebook 
If the item is a movie, ask if it’s streaming, 4K or BluRay and who the director is 
If the item is music, ask if it’s Apple Music, YouTube Music, Amazon Music or a CD 

""" 

# variable declarations 
data = {} # This is a special variable to store the pieces for the storage record 
"""string itemType 
string itemName 
int itemYear 
string itemGenre 
string mediaType 
string itemArtist 
float itemLength
string hasInput 
string inputTemporary
"""
# See if user has input 
hasInput = input("Do you have items to enter (y/n)?")
hasInput = hasInput.upper()
while hasInput == "Y":
    # get the initial baisc items
    itemName = input("Please enter the item name: ")
    inputTemporary = input( "Please enter the item year: ")
    itemYear = int(inputTemporary)
    itemGenre = input("Please enter the item genre: ")
    itemType = input("Please enter the item type (book, music, movie): ")
    if itemType == "book":
        mediaType = input("Please identify if this is an ebook, hardback or paperback book: ")
        itemArtist = input("Please enter the name of the author: ")
        inputTemporary = input("Please enter the number of pages in the book")
        itemLength = float(inputTemporary)
    elif itemType == "music":
        mediaType = input("Please identify if this is a CD or on YouTube Music, Apple Music or Amazon Music: ")
        itemArtist = input("Please enter the name of the artist: ")
        inputTemporary = input("Please enter the length in minutes of the music: " )
        itemLength = float(inputTemporary)
    elif itemType == "movie":
        mediaType = input("Please identify if this is a 4k, BluRay or streaming: ")
        itemArtist = input("Please enter the name of the director: ")
        inputTemporary = input( "Please enter the length in minutes of the movie: " )
        itemLength = float(inputTemporary)
    # store everything into the data object
    data["name"] = itemName
    data["type"] = itemType
    data["media"] = mediaType
    data["artist"] = itemArtist
    data["length"] = itemLength
    data["genre"] = itemGenre
    data["name"] = itemName
    # save the item
    with open("datafile.json","a") as f:
        f.writelines(json.dumps(data)+"\n")
    # Tell the user we"re all good
    print("We have saved the ",itemType," named ",itemName)
    # see if the user has more input
    hasInput = input("Do you have more items to enter (y/n)? ")
    hasInput = hasInput.upper()        
# End of program