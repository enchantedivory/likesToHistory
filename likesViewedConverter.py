#! /usr/bin/python3
import csv
import time
import datetime

# inserisco in un array gli id di tutti i video già presenti su FreeTube
with open("freetube_playlists/freetube-history-2022-09-27.db") as playlistFreeTube:
    freeTubeHistory = []
    playlistFreeTube = csv.reader(playlistFreeTube, delimiter=',')
    for row in playlistFreeTube:
        freeTubeHistory.append(row[0].replace('{"videoId":"',"").replace('"',"").strip())

# apro file scrittura
fileScrittura = open("exports_python/liked_to_viewed_videos.db", "w")
# apro file lettura
with open('youtube_playlists/likedVideos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # scorro file
    for row in csv_reader:
        # controllo che l'id video dei miei likes non sia già presente nella history di FreeTube
        if row[0].strip() not in freeTubeHistory:
            # trasformo data in unix
            time = row[1].replace("-","").replace(":","").replace("UTC","").replace(" ","").strip()
            time = int(datetime.datetime.strptime(time,"%Y%m%d%H%M%S").timestamp()+2*60*60)

            # stampo su file righe corrette
            line ='{"videoId":"' + row[0].strip() + '","title":"","author":"","authorId":"","published":"","viewCount":"","lengthSeconds":"","watchProgress":0,"timeWatched":' + str(time) + ',"isLive":"","paid":false,"type":"video"}\n'
            fileScrittura.write(line)
# chiudo file scrittura
fileScrittura.close()