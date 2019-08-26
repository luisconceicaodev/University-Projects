import spotipy
import spotipy.oauth2 as oauth2
import sys

credentials = oauth2.SpotifyClientCredentials(
        client_id= 'fefea9c5ccac4284bea0f9b06e326721',
        client_secret= '8a47ab7f8ca74a2db130ee01e31c801c')

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

#------------------------ Só aceita nomes sem espaços ! ----------------


def search_artist(artist):
    lista = []
    results = spotify.search(q='artist:' + artist, type='artist')
    artist_results = results['artists']['items']
    if len(artist_results) > 0:
        artist = (artist_results[0])
    lista.append('Nome: ' + artist['name'] + "\n")
    lista.append("ID: " + artist['id']+ "\n")
    lista.append("Cover: " + artist['images'][0]['url']+ "\n")
    lista.append("Main genre: "+ artist['genres'][0]+ "\n")
    lista.append("Followers: "+ str(artist['followers']['total']))
    return lista

def search_album(album):
    lista = []
    results = spotify.search(q='album:' + album, type='album')
    album_results = results['albums']['items']
    if len(album_results) > 0:
        album = (album_results[0])
    lista.append('Nome: ' + album['name'] + "\n")
    lista.append("ID: " + album['id']+ "\n")
    lista.append("Cover: " + album['images'][0]['url']+ "\n")
    lista.append("Release Date: " + album['release_date']+ "\n")
    lista.append("Number of tracks: "+str(album['total_tracks']))
    return lista

##print (album['name'], ":")
##print ("ID:", album['id'])
##print ("Cover: ",album['images'][0]['url'])
##print ("Release Date: ",album['release_date'])
##print ("Number of tracks: ",album['total_tracks'])

##print (artist['name'],":")
##print ("ID:", artist['id'])
##print ("Cover: ",artist['images'][0]['url'])
##print ("Main genre:", artist['genres'][0])
##print ("Followers:", artist['followers']['total'])
##
##print ("***")
##
##print (album['name'], ":")
##print ("ID:", album['id'])
##print ("Cover: ",album['images'][0]['url'])
##print ("Release Date: ",album['release_date'])
##print ("Number of tracks: ",album['total_tracks'])
##        
####if len(sys.argv) == 3:
####    artist = sys.argv[1]
####    album = sys.argv[2]
####else:
####    print ("Erro: argumentos incorretos.")
##
##results = spotify.search(q='artist:' + artist, type='artist')
##artist_results = results['artists']['items']
##if len(artist_results) > 0:
##    artist = artist_results[0]
##    
##results = spotify.search(q='album:' + album, type='album')
##album_results = results['albums']['items']
##if len(album_results) > 0:
##    album = album_results[0]
##
##print (artist['name'],":")
##print ("ID:", artist['id'])
##print ("Cover: ",artist['images'][0]['url'])
##print ("Main genre:", artist['genres'][0])
##print ("Followers:", artist['followers']['total'])
##
##print ("***")
##
##print (album['name'], ":")
##print ("ID:", album['id'])
##print ("Cover: ",album['images'][0]['url'])
##print ("Release Date: ",album['release_date'])
##print ("Number of tracks: ",album['total_tracks'])

    
