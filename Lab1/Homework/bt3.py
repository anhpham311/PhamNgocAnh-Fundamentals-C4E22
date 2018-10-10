from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
import matplotlib.pyplot as plt

client = MongoClient(uri)
db = client.get_default_database()

customers = db["customers"]

ads = customers.find({"ref":"ads"})
ads_count = ads.count()
print("No of customers by ads is", ads_count)

wom = customers.find({"ref":"wom"})
wom_count = wom.count()
print("No of customers by word of mouth is", wom_count)

events = customers.find({"ref":"events"})
events_count = events.count()
print("No of customers by events is", events_count)

# insert pie chart
labels = ["Ads", "Events", 'Word of mouth']
sizes = [ads_count, events_count, wom_count]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()