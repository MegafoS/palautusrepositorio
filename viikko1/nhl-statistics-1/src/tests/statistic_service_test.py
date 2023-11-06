import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_haku_löytää_pelaajan(self):
        pelaaja = self.stats.search("Gretzky")
        self.assertEqual(pelaaja.name, "Gretzky")
    def test_haku_ei_löydä_pelaajaa_jota_ei_ole(self):
        pelaaja = self.stats.search("XXXXXXXXXX")
        self.assertIsNone(pelaaja)

    def test_tiimihaku_toimii(self):
        tiimi = self.stats.team("PIT")
        self.assertEqual(len(tiimi), 1)
        tiimi = self.stats.team("EDM")
        self.assertEqual(len(tiimi), 3)
        tiimi = self.stats.team("JAA")
        self.assertEqual(len(tiimi), 0)

    def test_parhaat_pisteet_haku_toimii(self):
        parhaat = self.stats.top(2)
        self.assertEqual(len(parhaat),3)
        parhaat = self.stats.top(4)
        self.assertEqual(len(parhaat),5)
        parhaat = self.stats.top(0)
        self.assertEqual(len(parhaat),1)
