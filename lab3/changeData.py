import pandas as pd
import csv
from sklearn import preprocessing
df = pd.read_csv('AppleStore.csv')
arr = df['prime_genre'].unique()
#print(arr)
j = 0
dic = {}
for i in arr:
    if not i in dic:
        dic[i] = j
        j = j+1
#print(dic)

res = []
size_bytesm=df['size_bytes'].max()
size_bytesn=df['size_bytes'].min()
print("size_bytesm "+str(size_bytesm)+" "+str(size_bytesn))

pricem=df['price'].max()
pricen=df['price'].min()
print("pricem "+str(pricem)+" "+str(pricen))

rating_count_totm=df['rating_count_tot'].max()
rating_count_totn=df['rating_count_tot'].min()
print("rating_count_totm "+str(rating_count_totm)+" "+str(rating_count_totn))

rating_count_verm=df['rating_count_ver'].max()
rating_count_vern=df['rating_count_ver'].min()
print("rating_count_verm "+str(rating_count_verm)+" "+str(rating_count_vern))

user_ratingm=df['user_rating'].max()
user_ratingn=df['user_rating'].min()
print("user_ratingm "+str(user_ratingm)+" "+str(user_ratingn))

user_rating_verm=df['user_rating_ver'].max()
user_rating_vern=df['user_rating_ver'].min()
print("user_rating_verm "+str(user_rating_verm)+" "+str(user_rating_vern))

verm=df['ver'].max()
vern=df['ver'].min()
print("verm "+str(verm)+" "+str(vern))

cont_ratingm=df['cont_rating'].max()
cont_ratingn=df['cont_rating'].min()
print("cont_ratingm "+str(cont_ratingm)+" "+str(cont_ratingn))

prime_genrem=df['prime_genre'].max()
prime_genren=df['prime_genre'].min()
print("prime_genrem "+str(prime_genrem)+" "+str(prime_genren))

sup_devicesm=df['sup_devices'].max()
sup_devicesn=df['sup_devices'].min()
print("sup_devicesm "+str(sup_devicesm)+" "+str(sup_devicesn))

ipadSc_urlsm=df['ipadSc_urls'].max()
ipadSc_urlsn=df['ipadSc_urls'].min()
print("ipadSc_urlsm "+str(ipadSc_urlsm)+" "+str(ipadSc_urlsn))

langm=df['lang'].max()
langn=df['lang'].min()
print("langm "+str(langm)+" "+str(langn))

vpp_licm=df['vpp_lic'].max()
vpp_licn=df['vpp_lic'].min()
print("vpp_licm "+str(vpp_licm)+" "+str(vpp_licn))


#
#
# with open('AppleStore.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#
#     for row in csv_reader:
#         #print(row[12])
#         #print(dic.get(row[12]))
#         if not line_count==0:
#
#             row[12] = str(dic.get(row[12]))
#             a = row[10].split(".")
#             if len(a)>1:
#                 row[10] = a[0]+"."+a[1]
#             #print(row[10])
#             row[11] = row[11][:-1]
#             #print(row)
#             # row2 = []
#             # for k in row:
#             #     row2 = row2.append(k)
#             res.append(row)
#         line_count = line_count+1
# count = 0
# # res = res[1:]
#print(res)
# with open('master4.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(res)
# #print(res)
