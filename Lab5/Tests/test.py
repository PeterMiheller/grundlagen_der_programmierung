from Repo.repository import *
import unittest
from Controller.logik import *
from Modelle.bestellungs_modelle import *


class TestAddGericht(unittest.TestCase):
    def test_add_gericht(self):
        repo = CookedDishRepo()
        controller = Controller(repo)

        # Hinzufügen eines Gerichts
        controller.add_neues_gericht(1, '250g', 15, 'Nudeln', 30)

        # Überprüfen, ob das Gericht hinzugefügt wurde
        self.assertEqual(len(repo.gerichte), 1)
        gericht = repo.gerichte[0]
        self.assertEqual(gericht.id, 1)
        self.assertEqual(gericht.portionsgröße, '250g')
        self.assertEqual(gericht.preis, 15)
        self.assertEqual(gericht.name, 'Nudeln')
        self.assertEqual(gericht.zubereitungszeit, 30)
