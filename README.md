# PRAC_SergiSabateVilaJaimeFerrerLuengo

--------------------
sarscovhierarchy.py
--------------------

Aquest programa es dedica a obrir l’arxiu CSV sequences, que és el descarregat a la pàgina del NCBI amb els nucleòtids corresponents. 
Amb les dades que té aprofitarem per a crear un nou arxiu: Accesions.txt on es guardarà el nom de cada Accession que ens interessi per 
a després poder descarregar-los i tractar-los en un altre .py.
L’arxiu extret del NCBI rebrà un filtre per a aconseguir tan sols els ID’s dels països que no estan repetits (és a dir, n’agafa tan 
sols un si n’hi ha més) i no conta amb les ciutats o regions mitjançant tractar les Locations sense: ‘:’ o ‘\’. 
