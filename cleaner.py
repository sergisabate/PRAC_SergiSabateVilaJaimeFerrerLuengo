import csv


def read():
    m1 = open("sequences.csv", "r")
    m2 = open("sequences_clean.csv", "w", newline='')
    m3 = open("sequences_clean2.csv", "w", newline='')
    m1_csv = csv.reader(m1)
    m2_csv = csv.writer(m2)
    m3_csv = csv.writer(m3)

    for Accession, Length, Geo_Location in m1_csv:
        temp = Geo_Location
        if temp.find('\"'):
            temp = Geo_Location.split('\"')[0]
        if temp.find(":"):
            temp = temp.split(":")[0]
        if temp != '' and temp != "Geo_Location":
            l1 = [Accession, Length, temp]
            m2_csv.writerow(l1)
            m3_csv.writerow(l1)
    m1.close()
    m2.close()
    m3.close()


read()
