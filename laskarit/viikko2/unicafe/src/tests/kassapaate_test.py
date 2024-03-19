import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti




class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()


    def test_luotu_kassapääte_on_olemassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)


    def test_lounaita_maukkaita_myyty_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_lounaita_edullisia_myyty_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_käteisostot_toimii_edullinen(self):
         self.kassapaate.syo_edullisesti_kateisella(240)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_käteisostot_toimii_maukas(self):
         self.kassapaate.syo_maukkaasti_kateisella(400)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_käteisostot_toimii_edullinen_vaihtorahat(self):
         self.assertEqual( self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_käteisostot_toimii_maukas_vaihtorahat(self):
         self.assertEqual( self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_käteisostot_toimii_edullinen_määrä_kasvaa(self):
         self.kassapaate.syo_edullisesti_kateisella(240)
         self.assertEqual(self.kassapaate.edulliset, 1)

    def test_käteisostot_toimii_maukas_määrä_kasvaa(self):
         self.kassapaate.syo_maukkaasti_kateisella(400)
         self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_käteisostot_edullinen_eiriittävästirahaa(self):
         self.kassapaate.syo_edullisesti_kateisella(200)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_käteisostot_maukas_eiriittävästirahaa(self):
         self.kassapaate.syo_maukkaasti_kateisella(300)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_käteisostot_toimii_edullinen_vaihtorahat_kuneiriitäraha(self):
         self.assertEqual( self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_käteisostot_toimii_maukas_vaihtorahat_kuneiriitäraha(self):
         self.assertEqual( self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_käteisostot_toimii_edullinen_määrä_eikasva(self):
         self.kassapaate.syo_edullisesti_kateisella(200)
         self.assertEqual(self.kassapaate.edulliset, 0)

    def test_käteisostot_toimii_maukas_määräeikasva(self):
         self.kassapaate.syo_maukkaasti_kateisella(300)
         self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_korttiostot_toimii_edullinen_true(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)

    def test_korttiostot_toimii_maukas_true(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)


    def test_korttiostot_toimii_edullinen_veloitus(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(kortti.saldo, 760)

    def test_korttiostot_toimii_maukas_veloitus(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(kortti.saldo, 600)

    def test_korttiostot_toimii_edullinen_lounaidenmääräkasvaa(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiostot_toimii_maukas_lounaidenmääräkasvaa(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_korttiostot_toimii_edullinen_false(self, kortti=Maksukortti(100)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_korttiostot_toimii_maukas_false(self, kortti=Maksukortti(100)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)


    def test_korttiostot_toimii_edullinen_veloituseimeneläpi(self, kortti=Maksukortti(100)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(kortti.saldo, 100)

    def test_korttiostot_toimii_maukas_veloitus(self, kortti=Maksukortti(100)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(kortti.saldo, 100)

    def test_korttiostot_toimii_edullinen_lounaidenmääräeikasvaa(self, kortti=Maksukortti(100)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiostot_toimii_maukas_lounaidenmääräeikasvaa(self, kortti=Maksukortti(100)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_korttiostot_toimii_edullinen_kassaeimuutu(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_edullisesti_kortilla(kortti)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiostot_toimii_maukas_kassaeimuutu(self, kortti=Maksukortti(1000)):
         self.kassapaate.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_kortille_ladatessa_rahaa_kortin_saldo_muuttuu(self, kortti=Maksukortti(1000)):
         self.kassapaate.lataa_rahaa_kortille(kortti, 100)
         self.assertEqual(kortti.saldo, 1100)

    def test_kortille_ladatessa_rahaa_kassan_saldo_kasvaa(self, kortti=Maksukortti(1000)):
         self.kassapaate.lataa_rahaa_kortille(kortti, 100)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortille_ladatessa_rahaa_summa_ei_ole_suurempaa_kuin_nolla(self, kortti=Maksukortti(1000)):
         self.kassapaate.lataa_rahaa_kortille(kortti, -1)
         self.assertEqual(kortti.saldo, 1000)

    def test_kortille_ladatessa_rahaa_summa_ei_tässäkään_ole_suurempaa_kuin_nolla(self, kortti=Maksukortti(1000)):
         self.kassapaate.lataa_rahaa_kortille(kortti, -1)
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladatessa_rahaa_ei_returnia(self, kortti=Maksukortti(1000)):
         self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti, -1), None)