import csv
data= []
with open("planets_data.csv","r") as f :
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
headers=data[0]
planet_data = data[1:]
for data_point in planet_data:
    data_point[2] = data_point[2].lower()
#print(planet_data)
planet_data.sort(key=lambda planet_data:planet_data[2])
print(planet_data)
with open("planets_data.csv","w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerow(planet_data)