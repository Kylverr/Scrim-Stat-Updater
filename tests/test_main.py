import unittest
from main import text_from_box

BOXES = [
    # first player
    [708, 310, 1000, 346],
    [1044, 308, 1128, 344],
    [1158, 316, 1205, 342],
    [1255, 314, 1311, 346],
    [1350, 310, 1410, 343],
    [1447, 309, 1511, 340],
    # second player
    [708, 362, 1002, 400],
    [1043, 367, 1131, 396],
    [1156, 368, 1214, 394],
    [1255, 372, 1311, 395],
    [1352, 373, 1410, 394],
    [1446, 369, 1510, 396],
    # third player
    [708, 418, 1000, 454],
    [1043, 419, 1131, 450],
    [1156, 420, 1214, 448],
    [1255, 424, 1311, 449],
    [1355, 423, 1413, 450],
    [1450, 421, 1510, 450],
    # fourth player
    [708, 568, 1002, 604],
    [1043, 580, 1131, 600],
    [1156, 580, 1214, 600],
    [1255, 580, 1311, 600],
    [1355, 580, 1413, 600],
    [1450, 580, 1510, 600],
    # fifth player
    [708, 625, 1002, 660],
    [1043, 630, 1131, 655],
    [1156, 630, 1214, 655],
    [1255, 630, 1311, 655],
    [1355, 630, 1413, 655],
    [1450, 630, 1505, 655],
    # sixth player
    [708, 678, 1002, 712],
    [1043, 683, 1131, 712],
    [1156, 683, 1214, 712],
    [1255, 683, 1311, 712],
    [1355, 685, 1400, 710],
    [1450, 683, 1510, 712]
]

class TestMain(unittest.TestCase):

    # TESTS FOR test1.png 1st PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[0]), "twitch.tv/kylverr")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[1]), "955")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[2]), "5")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[3]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[4]), "2")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[5]), "7")

    # TESTS FOR test1.png 2nd PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[6]), "Im Shrodinger")
    
    # def test_text_from_box_g1_p1_score(self):
    #     self.assertEqual(text_from_box("Images/test1.png", BOXES[1]), "955")

    # def test_text_from_box_g1_p1_goals(self):
    #     self.assertEqual(text_from_box("Images/test1.png", BOXES[2]), "5")
        
    # def test_text_from_box_g1_p1_assists(self):
    #     self.assertEqual(text_from_box("Images/test1.png", BOXES[3]), "0")

    # def test_text_from_box_g1_p1_saves(self):
    #     self.assertEqual(text_from_box("Images/test1.png", BOXES[4]), "2")

    # def test_text_from_box_g1_p1_shots(self):
    #     self.assertEqual(text_from_box("Images/test1.png", BOXES[5]), "7")
if __name__ == '__main__':
    unittest.main()