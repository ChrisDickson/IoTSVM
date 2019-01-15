import pandas as pd
import os

#Read in different files, add the 'Class' column to their data frame
df = pd.read_csv('Documents/Danmini_Doorbell_Data/bengin_traffic.csv')
df['Class']=0
df.to_csv('Documents/Danmini_Doorbell_Data/benign_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/gafgyt_combo.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/gafgyt_combo_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/gafgyt_junk.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/gafgyt_junk_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/gafgyt_scan.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/gafgyt_scan_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/gafgyt_tcp.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/gafgyt_tcp_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/gafgyt_udp.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/gafgyt_udp_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/mirai_ack.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/mirai_ack_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/mirai_scan.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/mirai_scan_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/mirai_syn.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/mirai_syn_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/mirai_udp.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/mirai_udp_with_class.csv')

df = pd.read_csv('Documents/Danmini_Doorbell_Data/mirai_udpplain.csv')
df['Class']=1
df.to_csv('Documents/Danmini_Doorbell_Data/mirai_udpplain_with_class.csv')

path = 'Documents/Danmini_Doorbell_Data/with_class/'
files = os.listdir(path)

#Combine all files in 'with_class' folder  
df = pd.concat([pd.read_csv(path+f, index_col=[0,1]) for f in files])
df.to_csv(path+'combined_data.csv')

df = pd.read_csv(path+'combined_data.csv')

#Removes 'Unnamed' column added during combining data
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

#Shuffles data set
df = df.sample(frac=1).reset_index(drop=True)

#Gets shuffled fraction of data set (10%)
df2 = df.sample(frac=0.1).reset_index(drop=True)

#outputs the above to .csv files
df.to_csv('Documents/Danmini_Doorbell_Data/with_class/combined_data.csv', index=False)
df2.to_csv('Documents/Danmini_Doorbell_Data/with_class/tenth_combined_data.csv', index=False)
