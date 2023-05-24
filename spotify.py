from flask import Flask, request, jsonify
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
CORS(app)

SPOTIPY_CLIENT_ID = 'f79bd87d0a9143369035ad4ee79b1461'
SPOTIPY_CLIENT_SECRET = '2d18e255211e4dcf8f65dc10a70f72e9'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/api/search', methods=['GET'])

def search():
    query = request.args.get('q', '')
    results = sp.search(q=query, type='track', limit=10)
    
    tracks = []
    for item in results['tracks']['items']:
        track = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],  # get the first artist
            'album': item['album']['name'],
            'preview_url': item['preview_url']
        }
        tracks.append(track)
    
    return jsonify({'tracks': tracks})

if __name__ == '__main__':
    app.run(port=5000)  # runs the app on localhost port 5000
