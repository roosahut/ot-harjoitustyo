import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    
    def test_saldo_vähenee_oikein_kun_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_saldo_ei_muutu_kun_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palauttaa_true_kun_riittaa(self):
        tulo = self.maksukortti.ota_rahaa(10)
        self.assertEqual(tulo, True)

    def test_palauttaa_false_kun_ei_riita(self):
        tulo = self.maksukortti.ota_rahaa(20)
        self.assertEqual(tulo, False)