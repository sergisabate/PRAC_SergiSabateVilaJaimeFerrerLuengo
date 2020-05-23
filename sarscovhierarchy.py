import csv


def read():
    m1 = open("sequences.csv", "r")
    m2 = open("sequences2.csv", "w")
    m3 = open("Accesions.txt", "w")
    m1_csv = csv.reader(m1)
    m2_csv = csv.writer(m2)

    locations_list = ['Geo_Location', ':', '\"']
    repetit = False
    for Accession, Length, Geo_Location in m1_csv:
        l1 = [Accession, Length, Geo_Location]
        for x in locations_list:
            if not Geo_Location.find(x) == -1:
                repetit = True
        if len(Length) < 4 or Geo_Location == '':
            repetit = True
        if not repetit:
            locations_list.append(Geo_Location)
            m2_csv.writerow(l1)
            m3.write(Accession + "\n")
        repetit = False
    m1.close()
    m2.close()


read()
