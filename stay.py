
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import sys
from requests.exceptions import ReadTimeout

def main():
     #APIを入力
     client_id = '34b8b8cec397402697f5628cb38f0240'
     client_secret = 'b94199c727d94e29a8fabdd6d089a488'

     client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
     sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                          requests_timeout=10, retries=10)

     #データ読み込み
     result = sp.audio_features('5HCyWlXZPP0y6Gqq8TgA20')

     df = pd.DataFrame(result, columns = ['acousticness', 'danceability', 'energy',
                                          'instrumentalness', 'key', 'liveness','loudness',
                                          'mode', 'speechiness', 'tempo','time_signature',
                                          'valence'])

     #csvに書き込み
     df.to_csv('spotify_stay_data.csv', sep = ',')


#実行
if __name__ == "__main__":
     main()
     print('Finished')
