import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
from requests.exceptions import ReadTimeout

def main():
    #APIを入力
    client_id = '34b8b8cec397402697f5628cb38f0240'
    client_secret = 'b94199c727d94e29a8fabdd6d089a488'

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager,  
                         requests_timeout = 10, retries = 10)

    #楽曲idを書き込んだcsvを開く_ドライブソング
    import csv

    with open('spotify_drivesong_id.csv', 'r') as f:
      reader = csv.reader(f)
      line = [row for row in reader]

    line_T_1 = [list(x) for x in zip(*line)]
    track_ids1 = line_T_1[1]
    track_ids1.pop(0)

    #楽曲idを書き込んだcsvを開く_懐メロ
    import csv

    with open('spotify_natsumelo_id.csv', 'r') as f:
        reader = csv.reader(f)
        line = [row for row in reader]

    line_T_2 = [list(x) for x in zip(*line)]
    track_ids2 = line_T_2[1]
    track_ids2.pop(0)

    #楽曲の変数を取得
    def getTrackFeatures(id):
      meta = sp.track(id)
      features = sp.audio_features(id)

      name = meta['name']
      artist = meta['album']['artists'][0]['name']
        
      acousticness = features[0]['acousticness']
      danceability = features[0]['danceability']
      energy = features[0]['energy']
      instrumentalness = features[0]['instrumentalness']
      key = features[0]['key']
      liveness = features[0]['liveness']
      loudness = features[0]['loudness']
      mode = features[0]['mode']
      speechiness = features[0]['speechiness']
      tempo = features[0]['tempo']
      time_signature = features[0]['time_signature']
      valence = features[0]['valence']
      id = features[0]['id']

      track = [name, artist, acousticness, danceability, energy, instrumentalness, key, 
               liveness, loudness, mode, speechiness, tempo, time_signature, valence, id]
      return track

    #楽曲のidと変数を結びつける_ドライブソング
    try:
      
     tracks1 = []
     for i in range(len(track_ids1)):
        track1 = getTrackFeatures(track_ids1[i])
        tracks1.append(track1)

    except ReadTimeout:

      print('Spotify timed out... trying again...')
      tracks1 = []
      for i in range(len(track_ids1)):
        track1 = getTrackFeatures(track_ids1[i])
        tracks1.append(track1)

    df1 = pd.DataFrame(tracks1, columns = ['name', 'artist', 'acousticness', 'danceability', 
      'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 
      'tempo', 'time_signature', 'valence', 'id'])

    #重複楽曲数の確認、重複を除いて3000超取得
    duplicated_df1 = df1[df1.duplicated(subset=['name', 'artist'])]
    print(len(duplicated_df1))

    #変数をcsvに書き込み
    df1.to_csv('spotify_drivesong_data.csv', sep = ',')

    #楽曲のidと変数を結びつける_懐メロ
    try:
      
     tracks2 = []
     for i in range(len(track_ids2)):
        track2 = getTrackFeatures(track_ids2[i])
        tracks2.append(track2)

    except ReadTimeout:

      print('Spotify timed out... trying again...')
      tracks2 = []
      for i in range(len(track_ids2)):
        track2 = getTrackFeatures(track_ids2[i])
        tracks2.append(track2)

    df2 = pd.DataFrame(tracks2, columns = ['name', 'artist', 'acousticness', 'danceability', 
      'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 
      'tempo', 'time_signature', 'valence', 'id'])

    #重複楽曲数の確認、重複を除いて3000超取得
    duplicated_df2 = df2[df2.duplicated(subset=['name', 'artist'])]
    print(len(duplicated_df2))

    #変数をcsvに書き込み
    df2.to_csv("spotify_natsumelo_data.csv", sep = ',')

#実行
if __name__ == "__main__":
     main()
     print('Finished')
