import random

class Hangman:
    def __init__(self):
        self.sanat = ["ohjelmistotuotanto", "tietokone", "peli", "puhelin", "ohjelma", "pääsiäinen", "saippuakauppias", "suklaamuna", "keltainen", "hirsipuu", "yliopisto", "ammatti", "vaaleanpunainen"]

    def generoi_sana(self):
        self.sana = random.choice(self.sanat)
        self.sanakirja = {}
        indeksi = 0 
        for i in (self.sana):
            self.sanakirja[indeksi] = i
            indeksi += 1

    def kirjainten_maara(self):
        self.kirjaimet = {}
        for i, t in enumerate(self.sana):
            self.kirjaimet[t] = i
        self.uniikit_kirjaimet_maara = len(self.kirjaimet)


    def aloitus(self):
        self.pelinsana = []
        print("")
        komento = input("aloita peli! paina enter")
        self.generoi_sana()
        for i in self.sana:
            self.pelinsana.append("_")
        print("arvaa sana")
        print("sanan pituus on ", len(self.pelinsana))
        print("saat tehdä enintään 6 virhettä")
        print(self.pelinsana)
        self.kirjainten_maara()


    def main(self):
        self.aloitus()
        annetutkirjaimet = []
        count = 0
    
    
        while True:
            komento = input("anna kirjain: ")
            if komento in annetutkirjaimet:
                print("annoit kirjaimen jo!")
                print("kokeile uudelleen")
                continue
            if komento not in "abcdefghijklmnopqrstuvwxyzåäö":
                print("et antanut sopivaa kirjainta")
                print("kokeile uudelleen")
                continue
            if komento == "":
                print("et antanut sopivaa kirjainta")
                print("kokeile uudelleen")
                continue
    
            if komento in self.kirjaimet:
                count += 1
        
            annetutkirjaimet.append(komento)

            for key, value in self.sanakirja.items():
                if value == komento:
                    self.pelinsana[key] = value

            print((len(annetutkirjaimet) - count), "virhettä")
            print(self.pelinsana)

            if count == self.uniikit_kirjaimet_maara:
                print("VOITIT PELIN")
                break
            if (len(annetutkirjaimet) - count) == 6:
                print("HÄVISIT PELIN")
                print("sana oli", self.sana)
                break



            
            


sovellus = Hangman()
sovellus.main()

