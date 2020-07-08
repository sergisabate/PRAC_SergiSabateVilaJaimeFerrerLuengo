import urllib.request


def downloader():
    m1 = open("Accesions.txt", "r")
    lines = []
    i = 0
    for line in m1:
        lines.append(line.strip())
    for i in lines:
        idd = i
        url = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id=' + idd
        urllib.request.urlretrieve(url, "arxius_fasta/" + idd + ".fasta")


downloader()
