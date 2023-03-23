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

    #Rahan laataaminen kasvattaa saldoa oikein
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    #Rahan ottaminen toimii
    #Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_ota_rahaa_vahentaa_rahaa_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    #Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    #Metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_ota_rahaa_True_jos_rahaa_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_ota_rahaa_False_jos_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)