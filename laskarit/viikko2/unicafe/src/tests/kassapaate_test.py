import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_oikeat_alku_arvot_raha(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 10000)

    def test_oikeat_alku_arvot_raha(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_kateinen_maukas_maksu_riittava_raha_nousee(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kateinen_edullinen_maksu_riittava_raha_nousee(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateinen_maukas_maksu_riittava_oikea_vaihtoraha(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(maksu, 100)
    
    def test_kateinen_edullinen_maksu_riittava_oikea_vaihtoraha(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(340)
        self.assertEqual(maksu, 100)

    def test_kateinen_maukas_maksu_riittava_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateinen_edullinen_maksu_riittava_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(340)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateinen_maukas_maksu_ei_riittava_lounaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateinen_edullinen_maksu_riittava_lounaat_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_tarpeeksi_rahaa_veloitetaan_kortilta_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)

    def test_kortti_tarpeeksi_rahaa_veloitetaan_kortilta_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)

    def test_kortti_tarpeeksi_rahaa_true_tulee_maukas(self):
        tulo = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(tulo, True)

    def test_kortti_tarpeeksi_rahaa_true_tulee_edullinen(self):
        tulo = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(tulo, True)

    def test_kortti_tarpeeksi_rahaa_lounaat_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_tarpeeksi_rahaa_lounaat_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_ei_tarpeeksi_rahaa_rahamaara_ei_muutu_maukas(self):
        self.kortti.saldo = 200
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 200)

    def test_kortti_ei_tarpeeksi_rahaa_rahamaara_ei_muutu_edullinen(self):
        self.kortti.saldo = 200
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 200)

    def test_kortti_ei_tarpeeksi_rahaa_false_tulee_maukas(self):
        self.kortti.saldo = 200
        tulo = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(tulo, False)

    def test_kortti_ei_tarpeeksi_rahaa_false_tulee_edullinen(self):
        self.kortti.saldo = 200
        tulo = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(tulo, False)

    def test_kortti_ei_tarpeeksi_rahaa_lounaat_ei_kasva_maukas(self):
        self.kortti.saldo = 200
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_ei_tarpeeksi_rahaa_lounaat_ei_kasva_edullinen(self):
        self.kortti.saldo = 200
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_kassapaate_ei_nouse_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_kassapaate_ei_nouse_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_rahaa_ladatessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)
    
    def test_rahaa_ladatessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_rahaa_ladatessa_negatiivinen_summa_ei_vaikuta(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)