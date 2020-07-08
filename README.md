# PRAC_SergiSabateVilaJaimeFerrerLuengo

--------------------
cleaner.py
--------------------

Aquest programa es dedica a obrir l’arxiu CSV sequences, que és el descarregat a la pàgina del NCBI amb els nucleòtids corresponents. 
Amb les dades que té aprofitarem per a crear un nou arxiu: Accesions.txt on es guardarà el nom de cada Accession que ens interessi per 
a després poder descarregar-los i tractar-los en un altre .py.
L’arxiu extret del NCBI rebrà un filtre per a aconseguir en columnes els accessions totals.

--------------------
mediana.py
--------------------

De cada país, se sumarà la llargària de tots els seus accessions per a dividir-se pel nombre d'accessions que té, fent així una mediana de la llargària.
Després es recorrerà cada mostra buscant qui tingui la llargària més propera a la mediana, tant si és més petita com més gran. L'accession escollit serà el representant del país en qüestió a l'hora d'alinear-los i comparar-los. 

--------------------
cleaner2.py
--------------------

Aquest cleaner es dedica a fer fora als arxius que tinguin menys de 10000 caràcters ja que considerem que són problemàtics i no són vàlids per a comparar-ho amb altres que doblen la seva llargària. Normalment, aquest tipus de fastas trets es deuen a països que van estudiar el genoma al principi i no van proseguir, o països que tan sols han fet un parell de mostres.

--------------------
downloader.py
--------------------

El programa que es dedica a obrir l'arxiu Accessions.txt on hi ha el nom de totes les mostres i descarrega el seu corresponent FASTA
un a un de la web del NCBI. Es fa ús de la llibreria "urllib.request" per fer anar la url necessària per baixar l'arxiu .fasta. 
Tots es guardaran al directori "arxius_fasta/" amb el seu ID corresponent com a nom d'arxiu.

--------------------
alignment.py
--------------------

Aquest programa busca comparar tots els arxius amb tots i crear una jerarquia de semblança entre ells.
Hi ha moltes coses a tenir en compte per a duu a terme aquest .py. Comparant caràcter a caràcter mai seran semblants perquè a nivell d'arxiu les seqüències sempre es trobaran desplaçades per un nombre de chars. D'això tractarà aquest alineament.
El nombre de semblança es basarà en el nombre de caràcters no coincidents, per tant, quan més baix més propers i com més alt més llunyants.
S'escollirà els primers 10000 caràcters per a comparar-los (raó per la que ens va be el cleaner2.py) per a que el programa no es sobrecarregui i no tingui tant temps d'execució. Un cop això, es mostrarà per pantalla el nombre de semblança amb la comparació que s'ha fet entre cada accession.
