install.packages("dplyr")
library(dplyr)

#データ読みこみ
#stay
stay <- read.csv("spotify_stay_data.csv")
#ドライブソング
drive <- read.csv("spotify_drivesong_data.csv")
#懐メロ
natsu <- read.csv("spotify_natsumelo_data.csv")

#データ集計
#stay
head(stay)
staysong <- stay[, 2:13]
staysong

#ドライブソング
drive_omitted <-
 drive %>% distinct(name, artist, .keep_all = TRUE)
#3000曲超あることを確認
count(drive_omitted) 
drivesong <- drive_omitted[, 4:15]
#曲のアコースティック感
#stayは0.0383
drivesong_ac <- drive_omitted[, 2:4]
#曲の踊りやすさ
#stayは0.591
drivesong_d <- drive_omitted[, c(2,3,5)]
#曲のエネルギー量
#stayは0.764
drivesong_eng <- drive_omitted[, c(2,3,6)]
#曲のインスト曲感
#stayは0
count(drive_omitted[drive_omitted$instrumentalness == 0,])
drivesong_inst <- drive_omitted[drive_omitted$instrumentalness!=0, c(2,3,7)]
#曲のキー
#stayは1
drivesong_key <- drive_omitted[, c(2,3,8)]
count(drivesong_key[drivesong_key$key == 11,])
count(drivesong_key[drivesong_key$key == 10,])
count(drivesong_key[drivesong_key$key == 9,])
count(drivesong_key[drivesong_key$key == 8,])
count(drivesong_key[drivesong_key$key == 7,])
count(drivesong_key[drivesong_key$key == 6,])
count(drivesong_key[drivesong_key$key == 5,])
count(drivesong_key[drivesong_key$key == 4,])
count(drivesong_key[drivesong_key$key == 3,])
count(drivesong_key[drivesong_key$key == 2,])
count(drivesong_key[drivesong_key$key == 1,])
count(drivesong_key[drivesong_key$key == 0,])
#曲のライブ感
#stayは0.103
drivesong_live <- drive_omitted[, c(2,3,9)]
#曲のうるささ
#stayは-5.484
drivesong_loud <- drive_omitted[, c(2,3,10)]
#長調・短調
#stayは1=長調
drivesong_mode <- drive_omitted[, c(2,3,11)]
drivesong_minor <- filter(drivesong_mode, drivesong_mode$mode == 0)
drivesong_major <- filter(drivesong_mode, drivesong_mode$mode == 1)
#曲のスピーチ感
#stayは0.0483
drivesong_speech <- drive_omitted[, c(2,3,12)]
#曲のテンポ
#stayは169.928
drivesong_tempo <- drive_omitted[, c(2,3,13)]
#曲の拍子
#stayは4
drivesong_time <- drive_omitted[, c(2,3,14)]
count(drivesong_time[drivesong_time$time_signature == 5,])
count(drivesong_time[drivesong_time$time_signature == 4,])
count(drivesong_time[drivesong_time$time_signature == 3,])
count(drivesong_time[drivesong_time$time_signature == 1,])
count(drivesong_time[drivesong_time$time_signature == 0,])
#曲のポジティブ感
#stayは0.478
drivesong_val <- drive_omitted[, c(2,3,15)]

#懐メロ
natsu_omitted <-
  natsu %>% distinct(name, artist, .keep_all = TRUE)
#3000曲超あることを確認
count(natsu_omitted) 
natsumelo <- natsu_omitted[, 4:15]
#曲のアコースティック感
#stayは0.0383
natsumelo_ac <- natsu_omitted[, 2:4]
#曲の踊りやすさ
#stayは0.591
natsumelo_d <- natsu_omitted[, c(2,3,5)]
#曲のエネルギー量
#stayは0.764
natsumelo_eng <- natsu_omitted[, c(2,3,6)]
#曲のインスト曲感
#stayは0
count(natsu_omitted[natsu_omitted$instrumentalness == 0,])
natsu_inst <- drive_omitted[drive_omitted$instrumentalness!=0, c(2,3,7)]
#曲のキー
#stayは1
natsumelo_key <- natsu_omitted[, c(2,3,8)]
count(natsumelo_key[natsumelo_key$key == 11,])
count(natsumelo_key[natsumelo_key$key == 10,])
count(natsumelo_key[natsumelo_key$key == 9,])
count(natsumelo_key[natsumelo_key$key == 8,])
count(natsumelo_key[natsumelo_key$key == 7,])
count(natsumelo_key[natsumelo_key$key == 6,])
count(natsumelo_key[natsumelo_key$key == 5,])
count(natsumelo_key[natsumelo_key$key == 4,])
count(natsumelo_key[natsumelo_key$key == 3,])
count(natsumelo_key[natsumelo_key$key == 2,])
count(natsumelo_key[natsumelo_key$key == 1,])
count(natsumelo_key[natsumelo_key$key == 0,])
#曲のライブ感
#stayは0.103
natsumelo_live <- natsu_omitted[, c(2,3,9)]
#曲のうるささ
#stayは-5.484
natsumelo_loud <- natsu_omitted[, c(2,3,10)]
#長調・短調
#stayは1=長調
natsumelo_mode <- natsu_omitted[, c(2,3,11)]
#曲のスピーチ感
#stayは0.0483
natsumelo_speech <- natsu_omitted[, c(2,3,12)]
#曲のテンポ
#stayは169.928
natsumelo_tempo <- natsu_omitted[, c(2,3,13)]
#曲の拍子
#stayは4
natsumelo_time <- natsu_omitted[, c(2,3,14)]
count(natsumelo_time[natsumelo_time$time_signature == 5,])
count(natsumelo_time[natsumelo_time$time_signature == 4,])
count(natsumelo_time[natsumelo_time$time_signature == 3,])
count(natsumelo_time[natsumelo_time$time_signature == 1,])
#曲のポジティブ感
#stayは0.478
natsumelo_val <- natsu_omitted[, c(2,3,15)]

#データ可視化
#ドライブソングをキー=0~3、調性=長調=1、拍子=4で絞り込む
pickup_key0 <- filter(drive_omitted, drive_omitted$key == 0, drive_omitted$mode == 1, drive_omitted$time_signature == 4)
pickup_key1 <- filter(drive_omitted, drive_omitted$key == 1, drive_omitted$mode == 1, drive_omitted$time_signature == 4)
pickup_key2 <- filter(drive_omitted, drive_omitted$key == 2, drive_omitted$mode == 1, drive_omitted$time_signature == 4)
pickup_key3 <- filter(drive_omitted, drive_omitted$key == 3, drive_omitted$mode == 1, drive_omitted$time_signature == 4)
pickup <- rbind(pickup_key0, pickup_key1, pickup_key2, pickup_key3)
#pickupをクラスタリングにかける
pickup_stay <- rbind(pickup[1:833, 4:15], staysong)
pickup2 <- data.frame(scale(pickup_stay))
pickup_dist <- dist(pickup2, method = 'euclidean')
result_pickup2 <- hclust(pickup_dist, method = 'ward.D2')
par(mex = 1.0)
plot(result_pickup2, hang = -1, sub = "", xlab = "")
n <- 10
rect.hclust(result_pickup2, k = n)
pickup_cluster <- cutree(result_pickup2, k=n)
table(pickup_cluster)
pickup2$cluster <- pickup_cluster
pickup3 <- pickup2[,c(1:4,6,7,9,10,12,13)]
str(pickup3)

pickup_mean <- pickup3 %>%
  group_by(cluster) %>%
  summarize_all(mean)

#レーダーチャート作成
pickup_max <- max(pickup_mean[, -1]) + 0.1 
pickup_min <- min(pickup_mean[, -1]) - 0.1 
pickup_radarchart <- rbind(pickup_max, pickup_min, pickup_mean[, -1])
library(fmsb)
radarchart(pickup_radarchart)

library(RColorBrewer)
color_setting <- brewer.pal(n, "Set1")
radarchart(pickup_radarchart, pcol = color_setting, plwd = 4) 
legend('topright', legend = c(1:n),  col=color_setting, lty = 1:n, lwd = 4, cex = 0.8) 

#クラスター7, 9を除いたレーダーチャート作成
#7はspeechiness割と高い
#9はinstrumentalness高い
pickup_cluster1 <- filter(pickup3, pickup3$cluster == 1)
pickup_cluster2 <- filter(pickup3, pickup3$cluster == 2)
pickup_cluster3 <- filter(pickup3, pickup3$cluster == 3)
pickup_cluster4 <- filter(pickup3, pickup3$cluster == 4)
pickup_cluster5 <- filter(pickup3, pickup3$cluster == 5)
pickup_cluster6 <- filter(pickup3, pickup3$cluster == 6)
pickup_cluster8 <- filter(pickup3, pickup3$cluster == 8)
pickup_cluster10 <- filter(pickup3, pickup3$cluster == 10)
pickup4 <- rbind(pickup_cluster1, pickup_cluster2, pickup_cluster3, pickup_cluster4, 
                 pickup_cluster5, pickup_cluster6, pickup_cluster8, pickup_cluster10)

pickup_mean2 <- pickup4 %>%
  group_by(cluster) %>%
  summarize_all(mean)

pickup_max2 <- max(pickup_mean2[, -1]) + 0.1
pickup_min2 <- min(pickup_mean2[, -1]) - 0.1
pickup_radarchart2 <- rbind(pickup_max2, pickup_min2, pickup_mean2[, -1])
library(fmsb)
radarchart(pickup_radarchart2)

library(RColorBrewer)
color_setting <- brewer.pal(10, "Set1")
radarchart(pickup_radarchart2, pcol = color_setting, plwd = 4) 
legend('topright', legend = c(1:6,8,10),  col=color_setting, lty = 1:n, lwd = 4, cex = 0.8) 

#stayのドライブソング「キー0~3調性1拍子4」におけるクラスターを調べる
dim(pickup3)
pickup3[834,] 

#クラスター5
cluster5_mean <- pickup_mean[5, 2:10]
par(mex = 2.0)
barplot(as.matrix(cluster1_mean), ylim = c(-1, 1), yaxp = c(-1, 1, 10), las = 2, 
        main = "ドライブソング「キー0~3調性1拍子4」【クラスター5】特徴量")

#懐メロをキー=0~3、調性=長調=1、拍子=4で絞り込む
natsu_pickup_key0 <- filter(natsu_omitted, natsu_omitted$key == 0, natsu_omitted$mode == 1, natsu_omitted$time_signature == 4)
natsu_pickup_key1 <- filter(natsu_omitted, natsu_omitted$key == 1, natsu_omitted$mode == 1, natsu_omitted$time_signature == 4)
natsu_pickup_key2 <- filter(natsu_omitted, natsu_omitted$key == 2, natsu_omitted$mode == 1, natsu_omitted$time_signature == 4)
natsu_pickup_key3 <- filter(natsu_omitted, natsu_omitted$key == 3, natsu_omitted$mode == 1, natsu_omitted$time_signature == 4)
natsu_pickup_undone <- rbind(natsu_pickup_key0, natsu_pickup_key1, natsu_pickup_key2, natsu_pickup_key3)
natsu_pickup <- natsu_pickup_undone[, c(2,3,4:7,9,10,12,13,15)]

#natsu_pickupをクラスタリングにかける
natsu_pickup2 <- data.frame(scale(natsu_pickup[,c(3:11)]))
natsu_pickup3 <- rbind(natsu_pickup2, cluster5_mean)
natsu_pickup_dist <- dist(natsu_pickup3, method = 'euclidean')
result_natsu_pickup <- hclust(natsu_pickup_dist, method = 'ward.D2')
par(mex = 1.0)
plot(result_natsu_pickup, hang = -1, sub = "", xlab = "")
n <- 60
rect.hclust(result_natsu_pickup, k = n)
natsu_pickup_cluster <- cutree(result_natsu_pickup, k=n)
table(natsu_pickup_cluster)
natsu_pickup3$cluster <- natsu_pickup_cluster
str(natsu_pickup3)

natsu_pickup_mean <- natsu_pickup3 %>%
  group_by(cluster) %>%
  summarize_all(mean)

#ドライブソング「キー0~3調性1拍子4」【クラスター5】の懐メロ「キー0~3調性1拍子4」におけるクラスターを調べる
dim(natsu_pickup3)
natsu_pickup3[901,] 

#クラスター6
natsu_cluster6 <- natsu_pickup_mean[6, 2:10]
par(mex = 2.0)
barplot(as.matrix(natsu_cluster6), ylim = c(-1, 1), yaxp = c(-1, 1, 10), las = 2, main = "懐メロ「キー0~3調性1拍子4」【クラスター6】特徴量")

#懐メロ「キー0~3調性1拍子4」【クラスター6】の曲を抽出
number_cluster6 <- which(natsu_pickup3$cluster == 6)
data2 <- natsu_pickup[number_cluster6, 1:2]
dim(data2)
data2[31,]
#csvに書き出し
write.csv(data2[1:30,], "You're gonna love this!!.csv", row.names = FALSE)
