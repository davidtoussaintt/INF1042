import datetime

maintenant = datetime.datetime.now()
dans_100_heures = maintenant + datetime.timedelta(hours=100)
print("Il sera", dans_100_heures, "dans 100 heures.")