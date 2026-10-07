import csv
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

        self.strumenti = []
        self.prestiti = []

    @property
    def responsabile(self):

        return self.responsabile

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):

        self._responsabile = nuovo_responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:

                reader = csv.reader(file, delimiter = ",")

                for riga in reader:
                    codice = riga[0].strip()
                    tipo = riga[1].strip()
                    marca = riga[2].strip()
                    anno_acquisto = riga[3].strip()
                    valore = riga[4].strip()

                    nuovo_strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)

                    self.strumenti.append(nuovo_strumento)

        except FileNotFoundError:
            raise FileNotFoundError


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""

        if len(self.strumenti) == 0:
            nuovo_codice = "S1"
        else:
            ultimo_strumento = self.strumenti[-1]

            ultimo_codice = ultimo_strumento.codice

            ultimo_numero = int(ultimo_codice[1:])

            nuovo_codice = "S" + str(ultimo_numero+1)

        nuovo_strumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)

        self.strumenti.append(nuovo_strumento)

        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key = attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""



    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore


    def __str__(self):

        return f"{self.codice} {self.tipo} {self.marca} Anno: {self.anno_acquisto} Valore: {self.valore}"

class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo


    def __str__(self):

        return f"{self.codice} {self.data} ID: {self.id_strumento} Cognome{self.cognome_allievo}"