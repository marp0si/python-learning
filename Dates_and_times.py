import datetime
simdikitarihzaman=datetime.datetime.now()
simdikitarih=str(simdikitarihzaman).split(" ")
simdikitarih1=simdikitarih[0].split("-")
simdikizaman=simdikitarih[1].split(":")
simdikisaat=simdikizaman[0]
simdikidakika=simdikizaman[1]
simdikisaniye=simdikizaman[2]
simdikiyıl=simdikitarih1[0]
simdikiAy=simdikitarih1[1]
simdikiGün=simdikitarih1[2]

gün=simdikitarihzaman.strftime("%A")
print(simdikitarihzaman)
