import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    #Kortin saldo alussa oikein
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    #Rahan lataaminen kasvattaa saldoa oikein
    def test_rahan_lataaminen_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

#Rahan ottaminen toimii:
    #Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_saldo_vähenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)
    

    #Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    #Metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_riittikö_raha_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)

    def test_riittikö_raha_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(0), True)
       
       