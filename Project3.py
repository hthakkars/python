#            Project3.py

'''  
 This program is to help the artist determine how much they will earn by
 realeasing their songs on one of the popular music streaming platform:
 TIDL, Amazon, Apple Music, Spotify, YouTube. 
'''

import random

# Which streaming service will you use to upload your song?
STREAM_SERV_TIDAL = 1
STREAM_SERV_AMAZON = 2
STREAM_SERV_APPLE_MUSIC = 3
STREAM_SERV_SPOTIFY = 4
STREAM_SERV_YOUTUBE = 5

# Pay per streaming for each Streaming service in $.
STREAM_SERV_TIDAL_COST = 0.01250
STREAM_SERV_AMAZON_COST= 0.00402
STREAM_SERV_APPLE_MUSIC_COST = 0.00735
STREAM_SERV_SPOTIFY_COST = 0.00437
STREAM_SERV_YOUTUBE_COST = 0.00069

# Distribution Charge % 
DIST_MAJOR_CHARGE = 60
DIST_IND_CHARGE = 30

#Defining variable stream choice prompt
streamChoiceStr = ''
artistName = ''
songName = ''
streams = -1
userInput = 0
streamChoice = 0

distributionType = 0
noOfSongs = -1
noOfStreams = 0
totalStreams = 0

#The main function.
def main():
    global streamChoiceStr
    global artistName
    global songName
    global streams
    global userInput
    global streamChoice
    global distributionType
    global noOfSongs
    global noOfStreams
    global totalStreams
    
    # Defining variable for earning
    earning = 0.00
    
    #Defining variable streang choice prompt
    streamChoiceStr = ''
    artistName = ''
    songName = ''
    streams = -1
    userInput = 0
    streamChoice = 0
    
    distributionType = 0
    noOfSongs = -1
    noOfStreams = 0
    totalStreams = 0
    
    mainMenu()
    if(userInput==1):
        executeSingleSongMenuOption()
    elif(userInput==2):
        executeMultiSongsMenuOption()
    else:
        print('Thank you for using the program!')
        exit()
    
# Execute single song menu options
def executeSingleSongMenuOption():
    global streamChoice
    global songName
    global artistName
    global streamChoiceStr
    global streams
    
    streamingSerivceMenu()
    getSingleSongOptions()
    totalEarnings = calculateEarnings(streamChoice, streams)
    displaySingleEarning(songName, artistName, streamChoiceStr, streams, totalEarnings)
    
# Execute multiple song menu options    
def executeMultiSongsMenuOption():
    global streamChoiceStr
    global streamChoice
    global distributionType
    
    streamingSerivceMenu()
    getNumberOfSongs()
    distributionLabelMenu()
    totalStreams = generateStreams(distributionType)
    totalEarnings = calculateEarnings(streamChoice, totalStreams)
    labelEarnings = calculateLabelEarnings(distributionType, totalEarnings)
    artistEarnings = totalEarnings-labelEarnings
    displayEarnings(streamChoiceStr, distributionType, totalStreams, totalEarnings, labelEarnings, artistEarnings)

# User input options
def mainMenu():
    global userInput
    while (userInput < 1 or userInput > 3):
        print('Choose from of the following menu option:')
        print('\t1: Upload a single song to a streaming service')
        print('\t2: Upload a multiple songs to a streaming service')
        print('\t3: Exit the program')
        userInput = int(input("Enter your choice(1,2,or 3): "))
        if (userInput < 1 or userInput > 3):
            print('ERROR - NOT A VALID MENU CHOICE. PLEASE TRY AGAIN')

# User input stream options
def streamingSerivceMenu():
    global streamChoice
    while (streamChoice < 1 or streamChoice > 5):
        print('Which Streaming Service will you use to upload your song(s)?')
        print('\t 1: TIDAL')
        print('\t 2: Amazon')
        print('\t 3: Apple music')
        print('\t 4: Spotify')
        print('\t 5: YouTube')
        
        # Get user's streaming choice.
        streamChoice = int(input('Enter your choice (1-5): ')) 
        
        if (streamChoice < 1 or streamChoice > 5):
            print('ERROR - NOT A VALID STREAMING SERVICE. Please choose from the services listed.')
            
# This accepts a list as an argument returns the stream choice for single song.
def getSingleSongOptions():
    global streamChoice
    global streamChoiceStr
    global artistName
    global songName
    global streams
    
    if streamChoice == STREAM_SERV_TIDAL:
       streamChoiceStr = 'TIDAL'
    elif streamChoice == STREAM_SERV_AMAZON:
       streamChoiceStr = 'Amazon'
    elif streamChoice == STREAM_SERV_APPLE_MUSIC:
       streamChoiceStr= 'Apple music'
    elif streamChoice == STREAM_SERV_SPOTIFY:
       streamChoiceStr = 'Spotify'
    elif streamChoice == STREAM_SERV_YOUTUBE:
       streamChoiceStr = 'YouTube'
       
    # Get the artist name, song name and streams from user.
    artistName= input('What is the artist\'s name?: ')
    songName = input('What is the name of the song?: ')
    
   #Simulate the input of streams 
    while (streams < 0):
        streams = int(input('How many streams does '+songName+' have on '+ streamChoiceStr+ '?: '))
        
        # Determine weather the streams qualifies.
        if streams < 0:
            print('ERROR - NUMBER OF STREAMS CANNOT BE NEGATIVE.') 

# This display single song earning.           
def displaySingleEarning(songName, artistName, streamChoiceStr, totalStreams, totalEarnings):

    # Display the earning for each streaming service.
    print('Song Name:\t\t',songName)
    print('Artist Name:\t\t',artistName)
    print('Streaming Service:\t',streamChoiceStr)
    print('Streams:\t\t',totalStreams)
    print('Earnings:\t\t',' $', format(totalEarnings, '.2f'), sep='')    

# User number of songs input for multiple songs menu.
def getNumberOfSongs():
    global streamChoice
    global streamChoiceStr
    global noOfSongs
    
    if streamChoice == STREAM_SERV_TIDAL:
       streamChoiceStr = 'TIDAL'
    elif streamChoice == STREAM_SERV_AMAZON:
       streamChoiceStr = 'Amazon'
    elif streamChoice == STREAM_SERV_APPLE_MUSIC:
       streamChoiceStr= 'Apple music'
    elif streamChoice == STREAM_SERV_SPOTIFY:
       streamChoiceStr = 'Spotify'
    elif streamChoice == STREAM_SERV_YOUTUBE:
       streamChoiceStr = 'YouTube'
       
 # Simulate the input of number of songs. 
    while (noOfSongs <0):  
        noOfSongs = int(input('How many songs will be uploaded on '+ streamChoiceStr +' ? '))
        
     # Determin weather the number of songs qualifies.  
        if (noOfSongs <0):
            print('ERROR - NUMBER OF SONGS CANNOT BE NEGATIVE.')
            
    
# User input for distribution type selection
def distributionLabelMenu():
    global distributionType
    
    while (distributionType <1 or distributionType >2):
        print('Which type of distribution will you use to distribute your song(s)?')
        print('\t 1: MAJOR LABEL')
        print('\t 2: INDEPENDENT LABEL') 
        
        distributionType = int(input('Enter your choice (1 or 2): '))
        
        if (distributionType <1 or distributionType >2):
            print('ERROR - INDIVIDUAL DISTRIBUTION CHOSEN. Please choose from one of the option listed.')

# This prints songs list with random number streams
def generateStreams(distributionType):
    global noOfSongs 
    global noOfStreams 
    global totalStreams 
    
    for index in range(1,noOfSongs+1,1):
        if (distributionType == 1):
            noOfStreams = random.randint(100000,50000000)
        else:
            noOfStreams = random.randint(10000,1000000)
            
        totalStreams = totalStreams + noOfStreams
        print('Song #',index,':\t',noOfStreams,' streams', sep='')

    return totalStreams
    
# This calculate earnings based on stream type and total streams
def calculateEarnings(streamChoice, totalStreams):       
        
    # Calculate earning for each streaming service.
    if streamChoice == STREAM_SERV_TIDAL:
       totalEarnings = totalStreams * STREAM_SERV_TIDAL_COST
    elif streamChoice == STREAM_SERV_AMAZON:
       totalEarnings = totalStreams * STREAM_SERV_AMAZON_COST
    elif streamChoice == STREAM_SERV_APPLE_MUSIC:
       totalEarnings = totalStreams * STREAM_SERV_APPLE_MUSIC_COST
    elif streamChoice == STREAM_SERV_SPOTIFY:
       totalEarnings = totalStreams * STREAM_SERV_SPOTIFY_COST
    elif streamChoice == STREAM_SERV_YOUTUBE:
       totalEarnings = totalStreams * STREAM_SERV_YOUTUBE_COST
       
    return totalEarnings

# This calculate label earning based on distribution type and total earning 
def calculateLabelEarnings(distributionType, totalEarnings):
    labelEarnings = 0
    
    if (distributionType == 1):
        labelEarnings = (totalEarnings * DIST_MAJOR_CHARGE) / 100
    elif (distributionType == 2):
        labelEarnings = (totalEarnings * DIST_IND_CHARGE) / 100

    return labelEarnings
    
#This displays earning for multiple song menu selection
def displayEarnings(streamChoiceStr, distributionType, totalStreams, totalEarnings, labelEarnings, artistEarnings):
    
    # Display the earning for each streaming service.
    print('Streaming Service:\t',streamChoiceStr)
    print('Streams:\t\t',totalStreams)
    print('Earnings:\t\t',' $', format(totalEarnings, '.2f'), sep='')
    print('Artist Earnings:\t',' $', format(artistEarnings, '.2f'), sep='')
    print('Label Earnings:\t\t',' $', format(labelEarnings, '.2f'), sep='')    
    

#call the main function.    
while (userInput!=3):
    main()