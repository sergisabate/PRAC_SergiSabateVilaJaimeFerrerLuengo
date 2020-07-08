import csv


def calc():
    m1 = open("Accesions.txt", "r")
    m2 = open("sequences2.csv", "r")
    m2_csv = csv.reader(m2)
    valors = []
    lines = []
    lines2 = []
    j, x = 0, 0
    vaa = False

    for line in m1:
        lines.append(line.strip())
    m1.close()

    for i in lines:
        m4 = open("arxius_fasta/" + i + ".fasta", "r")
        numline = 0
        m4.readline()
        lines2.append(m4.readline().strip())

        while numline < 160:
            lines2[j] = lines2[j] + m4.readline().strip()
            numline += 1
        j += 1
        m4.close()

    while x < len(lines):
        temp_valors = []
        for y in lines2:
            temp_value2332 = 0
            char0 = lines2[x][temp_value2332]
            char1 = y[temp_value2332]
            cadena0 = char0
            cadena1 = char1
            temp_value2332 += 1
            mod = 0
            while not vaa:
                while (temp_value2332 + mod) < (20 + mod):
                    char0 = lines2[x][temp_value2332 + mod]
                    char1 = y[temp_value2332 + mod]
                    cadena0 = cadena0 + char0
                    cadena1 = cadena1 + char1
                    temp_value2332 += 1
                if lines2[x].find(cadena1) != -1:
                    vaa = True
                elif y.find(cadena0) != -1:
                    vaa = True
                else:
                    mod = mod + 1
                    temp_value2332 = 0
                    cadena0 = ""
                    cadena1 = ""
            vaa = False
            mod = 0

            temp_split0 = lines2[x]
            temp_split1 = y
            if cadena0 != cadena1:
                if lines2[x].find(cadena1) != -1:
                    temp_split0 = lines2[x].split(cadena1, 2)
                    temp_split0 = temp_split0[1]
                    temp_split1 = y.split(cadena1, 2)
                    temp_split1 = temp_split1[1]
                elif cadena0 != cadena1:
                    if y.find(cadena0) != -1:
                        temp_split0 = lines2[x].split(cadena0, 2)
                        temp_split0 = temp_split0[1]
                        temp_split1 = y.split(cadena0, 2)
                        temp_split1 = temp_split1[1]

            value = 0
            count = 0
            while count < 1000:
                next0 = temp_split0[count]
                next1 = temp_split1[count]
                if not next0 or not next1:
                    break
                if next0 != next1:
                    value += 1
                count += 1
            print("Comparació entre " + lines[x] + " i " + lines[lines2.index(y)] + " és: " + str(value))

            temp_valors.append(value)
        print("\n")
        valors.append(temp_valors)
        x += 1

    m2.close()


calc()
