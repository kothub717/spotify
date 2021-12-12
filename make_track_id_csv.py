import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests.exceptions import ReadTimeout

def main():
     #APIを入力
     client_id = '34b8b8cec397402697f5628cb38f0240'
     client_secret = 'b94199c727d94e29a8fabdd6d089a488'

     client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
     sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                          requests_timeout=10, retries=10)

     #プレイリストidを入力_ドライブソング
     def getTrackIDs(playlist_ids):
  
       track_ids = []

       for playlist_id in playlist_ids:
         playlist = sp.playlist(playlist_id)

         while playlist['tracks']['next']:
           for item in playlist['tracks']['items']:
             track = item['track']
             track_ids.append(track['id'])
           playlist['tracks'] = sp.next(playlist['tracks'])

         else:
           for item in playlist['tracks']['items']:
             track = item['track']
             track_ids.append(track['id'])

       return track_ids

     playlist_ids1 = ['1DLrsHeKu1z1aS2LoCJr1t', '7yWmQI0XeYYCqrZTWqD4HO',
                      '3V1KhNBg8gC9xpxrKDDr7i', '0IflXYMtsGsd1RW4ORpKy7',
                      '5P6hnZzIP5bxXcMcs8lFLd', '2qL88SeigZKyBnFjH5Qe2w', 
                      '2rbncbHFealDKON8mVrxyR', '2W6Qe8aWWIDm5iKVbwwQE1',
                      '5mI13w9UasNCm2VsId1DtT', '2cu07vq3uDI5QsgGT1zdxO',
                      '3cNU8rEAchW5r1cVXzzrs8', '4TFGR6rgVOOca49qCXSj5W', 
                      '0iW31srilXqCAnyHPIXRR5', '6zefcAD3lLGzmKOk15GhEx',
                      '1SjDinK3JTgb6gWpDGUy7Y', '3wZjctyrtCAhp3QBV5byEu',
                      '73q1OjVojMYW2TRddISSiG', '132U72x1rlJaVWlXRyVjUW', 
                      '61YnsFsvWvSccodjeGtpbo', '0ADZuqAODLglcy5TccnLuQ',
                      '37i9dQZF1DWSAJ2OGLglOP', '2vmZnCGxxrq0houM6zrGmW',
                      '52IhxLmUCtg1vbU9ZQfIWr', '59XJcYsE3BsavlvIFSS30q', 
                      '2vHnD14FblnFd3nnPbtyZf', '6dawFJMUimqH31ahukZs29',
                      '3hoJaXzeYe1RJzo9iFDi7B', '6XLIilnkgM5pu5QL7V36uW']  

     track_ids1 = getTrackIDs(playlist_ids1)

     #検収条件の確認
     def get_pl_length(sp: spotipy.client.Spotify, playlist_ids: str) -> int:
         return sp.playlist_tracks(
             playlist_ids,
             offset=0,
             fields="total"
         )["total"]

     pl_length1 = print(get_pl_length(sp, '1DLrsHeKu1z1aS2LoCJr1t') + 
                          get_pl_length(sp, '7yWmQI0XeYYCqrZTWqD4HO') +
                          get_pl_length(sp, '3V1KhNBg8gC9xpxrKDDr7i') +
                          get_pl_length(sp, '0IflXYMtsGsd1RW4ORpKy7') +
                          get_pl_length(sp, '5P6hnZzIP5bxXcMcs8lFLd') +
                          get_pl_length(sp, '2qL88SeigZKyBnFjH5Qe2w') +
                          get_pl_length(sp, '2rbncbHFealDKON8mVrxyR') +
                          get_pl_length(sp, '2W6Qe8aWWIDm5iKVbwwQE1') +
                          get_pl_length(sp, '5mI13w9UasNCm2VsId1DtT') +
                          get_pl_length(sp, '2cu07vq3uDI5QsgGT1zdxO') +
                          get_pl_length(sp, '3cNU8rEAchW5r1cVXzzrs8') +
                          get_pl_length(sp, '4TFGR6rgVOOca49qCXSj5W') +
                          get_pl_length(sp, '0iW31srilXqCAnyHPIXRR5') +
                          get_pl_length(sp, '6zefcAD3lLGzmKOk15GhEx') +
                          get_pl_length(sp, '1SjDinK3JTgb6gWpDGUy7Y') +
                          get_pl_length(sp, '3wZjctyrtCAhp3QBV5byEu') +
                          get_pl_length(sp, '73q1OjVojMYW2TRddISSiG') +
                          get_pl_length(sp, '132U72x1rlJaVWlXRyVjUW') +
                          get_pl_length(sp, '61YnsFsvWvSccodjeGtpbo') +
                          get_pl_length(sp, '0ADZuqAODLglcy5TccnLuQ') + 
                          get_pl_length(sp, '37i9dQZF1DWSAJ2OGLglOP') +
                          get_pl_length(sp, '2vmZnCGxxrq0houM6zrGmW') +
                          get_pl_length(sp, '52IhxLmUCtg1vbU9ZQfIWr') +
                          get_pl_length(sp, '59XJcYsE3BsavlvIFSS30q') +
                          get_pl_length(sp, '2vHnD14FblnFd3nnPbtyZf') +
                          get_pl_length(sp, '6dawFJMUimqH31ahukZs29') +
                          get_pl_length(sp, '3hoJaXzeYe1RJzo9iFDi7B') +
                          get_pl_length(sp, '6XLIilnkgM5pu5QL7V36uW'))
 
     if print(len(track_ids1)) == pl_length1:
         print("検収条件達成")
     else:
         print("検収条件未達成")


     #楽曲idをcsvに書き込み
     track_ids1_df = pd.DataFrame(track_ids1)
     track_ids1_df.to_csv('spotify_drivesong_id.csv', sep = ',')

     #プレイリストidを入力_懐メロ
     playlist_ids2 = ['0ECChQuh17jvprg5R3iXzT', '7vgHNyZLYQrZa8rwt5kaiV',
                      '0zQyxyuRIqj2YEenFM7z4z', '1HGn5JlHoUse3roXozm7Oo',
                      '7y5I8V6H7HfRHRQi1V0lD9', '0FVJtzVj1ihfBH9rC3CRPQ', 
                      '0zeUqZZI8xX0jtN5vr691H', '2TajSMPFMby1HcclouN0Oj',
                      '7qSxZG8uX2mmqHRQZCjKmK', '32xm47VLpBheTfapOl4bnl',
                      '5JUYroPwqRYACOZ1H7o3o1', '30dOk9TiUMEAFhrc6qEfol', 
                      '5M1zcJqgBbOkKHK3uBbC9K', '6vP1kXTwSqFsNLsQ4WZc56',
                      '22iz3QqsGx8kaYThdjWCBG', '5EDv7LePYBedd1zdZryAuD',
                      '61j044WNbE33xZG79HQr4n', '4RYUSOrn1CcjhYv70ixoPo', 
                      '76cm1EjlOYGBsAOlIUQFje', '6KFxLJY3ppzw93zY90zpVL',
                      '1jYNhRXcktnJy012aOAy70', '0Do5TRQTJCx79XcPeDWfrD',
                      '5pGxPUXOyjaaiGiHubJXvJ', '2HBnkpcsrXpAO5RtNuMZYZ', 
                      '7Gb08zCy1eP2TStAuCMR4Y', '3mX4EZtzeGpADDJpmLaGEL',
                      '0UeoTuac1wzCXK5iZDQ9vk', '7hK4QfjEt4TpJUXySzwwmI',
                      '4H9d6nYmeNkrxqUg8bJqU1', '5M9fd97TItOTU1VLvy19d1', 
                      '7skMngKUlem958O4NUtP6U', '4wkH1p6BIq5y5Hw1xrp5YQ',
                      '6Uxe9hahGISHJMvHL2SDTV', '5iNBw3BjBFoDIsi487zE2R',
                      '2Ex5aRThAk9gO0QjuQtG0F'] 

     track_ids2 = getTrackIDs(playlist_ids2)

     #検収条件の確認
     pl_length2 = print(get_pl_length(sp, '0ECChQuh17jvprg5R3iXzT') +
                          get_pl_length(sp, '7vgHNyZLYQrZa8rwt5kaiV') +
                          get_pl_length(sp, '0zQyxyuRIqj2YEenFM7z4z') +
                          get_pl_length(sp, '1HGn5JlHoUse3roXozm7Oo') +
                          get_pl_length(sp, '7y5I8V6H7HfRHRQi1V0lD9') +
                          get_pl_length(sp, '0FVJtzVj1ihfBH9rC3CRPQ') +
                          get_pl_length(sp, '0zeUqZZI8xX0jtN5vr691H') +
                          get_pl_length(sp, '2TajSMPFMby1HcclouN0Oj') +
                          get_pl_length(sp, '7qSxZG8uX2mmqHRQZCjKmK') +
                          get_pl_length(sp, '32xm47VLpBheTfapOl4bnl') +
                          get_pl_length(sp, '5JUYroPwqRYACOZ1H7o3o1') +
                          get_pl_length(sp, '30dOk9TiUMEAFhrc6qEfol') +
                          get_pl_length(sp, '22iz3QqsGx8kaYThdjWCBG') +
                          get_pl_length(sp, '5EDv7LePYBedd1zdZryAuD') +
                          get_pl_length(sp, '61j044WNbE33xZG79HQr4n') +
                          get_pl_length(sp, '4RYUSOrn1CcjhYv70ixoPo') +
                          get_pl_length(sp, '76cm1EjlOYGBsAOlIUQFje') +
                          get_pl_length(sp, '6KFxLJY3ppzw93zY90zpVL') + 
                          get_pl_length(sp, '1jYNhRXcktnJy012aOAy70') +
                          get_pl_length(sp, '0Do5TRQTJCx79XcPeDWfrD') +
                          get_pl_length(sp, '5pGxPUXOyjaaiGiHubJXvJ') +
                          get_pl_length(sp, '2HBnkpcsrXpAO5RtNuMZYZ') +
                          get_pl_length(sp, '7Gb08zCy1eP2TStAuCMR4Y') +
                          get_pl_length(sp, '3mX4EZtzeGpADDJpmLaGEL') +
                          get_pl_length(sp, '0UeoTuac1wzCXK5iZDQ9vk') +
                          get_pl_length(sp, '7hK4QfjEt4TpJUXySzwwmI') +
                          get_pl_length(sp, '4H9d6nYmeNkrxqUg8bJqU1') +
                          get_pl_length(sp, '5M9fd97TItOTU1VLvy19d1') +
                          get_pl_length(sp, '7skMngKUlem958O4NUtP6U') +
                          get_pl_length(sp, '4wkH1p6BIq5y5Hw1xrp5YQ') +
                          get_pl_length(sp, '6Uxe9hahGISHJMvHL2SDTV') +
                          get_pl_length(sp, '5iNBw3BjBFoDIsi487zE2R') +
                          get_pl_length(sp, '2Ex5aRThAk9gO0QjuQtG0F'))

     if print(len(track_ids2)) == pl_length2:
         print("検収条件達成")
     else:
         print("検収条件未達成")

     #現在再生できない曲のidを削除
     track_ids2_filtered = [x for x in track_ids2 if x]

     #楽曲idをcsvに書き込み
     track_ids2_df = pd.DataFrame(track_ids2_filtered)
     track_ids2_df.to_csv('spotify_natsumelo_id.csv', sep = ',')

#実行
if __name__ == "__main__":
     main()
     print('Finished')
