import csv


def read():
    m1 = open("sequences_clean.csv", "r")
    m4 = open("sequences_clean2.csv", "r")
    m2 = open("sequences2.csv", "w", newline='')
    m1_csv = csv.reader(m1)
    m2_csv = csv.writer(m2)
    m4_csv = csv.reader(m4)
    length_list = []
    geo_location_list = []
    count = []
    accession_list = []
    true_length_list = []
    found = False

    for Accession, Length, Geo_Location in m1_csv:
        for x in geo_location_list:
            position = geo_location_list.index(x)
            if x == Geo_Location:
                length_list[position] = int(length_list[position]) + int(Length)
                count[position] = count[position] + 1
                found = True
                break
        if not found:
            geo_location_list.append(Geo_Location)
            length_list.append(Length)
            count.append(1)
        found = False
    for x in geo_location_list:
        position = geo_location_list.index(x)
        length_list[position] = int(length_list[position]) / count[position]
    m1.close()
    for i in geo_location_list:
        accession_list.append("")
        true_length_list.append(0)
    found = False
    for Accession, Length, Geo_Location in m4_csv:
        for x in geo_location_list:
            if x == Geo_Location:
                position = geo_location_list.index(x)
                if true_length_list[position] == 0:
                    true_length_list[position] = Length
                    accession_list[position] = Accession
                    found = True
                    break
                elif (max(int(true_length_list[position]), length_list[position]) - min(int(true_length_list[position]),
                                                                                        length_list[
                                                                                            position])) > int(
                    max(int(Length), length_list[position]) - min(int(Length), length_list[position])) and int(Length) > 9999:
                    true_length_list[position] = Length
                    accession_list[position] = Accession
                    found = True
                    break
        found = False
    m4.close()
    for x in geo_location_list:
        position = geo_location_list.index(x)
        l1 = [accession_list[position], true_length_list[position], x]
        m2_csv.writerow(l1)
    m2.close()


read()
