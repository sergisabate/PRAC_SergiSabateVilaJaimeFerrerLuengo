import csv


def clean():
    m1 = open("Accesions.txt", "w")
    m2 = open("sequences2.csv", "r")
    m2_csv = csv.reader(m2)

    for Accession, Length, Geo_Location in m2_csv:
        if int(Length) > 9999:
            m1.write(Accession + "\n")
    m2.close()


clean()
