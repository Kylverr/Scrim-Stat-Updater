import unittest
from main import text_from_box

"""
Testing file for main.py.

Author: Kyle Stewart
Date: 2024-06-16

Usage:
    python -m unittest tests.test_main
"""

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
    [708, 570, 1000, 606],
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
    [708, 678, 1002, 716],
    [1043, 683, 1131, 712],
    [1156, 683, 1214, 712],
    [1255, 683, 1311, 712],
    [1355, 685, 1400, 710],
    [1450, 683, 1510, 712]
]

class TestMain(unittest.TestCase):

    # TESTS FOR test1.png
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
    def test_text_from_box_g1_p2_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[6]), "Im Schrédinger")
    
    def test_text_from_box_g1_p2_score(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[7]), "385")

    def test_text_from_box_g1_p2_goals(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[8]), "0")
        
    def test_text_from_box_g1_p2_assists(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[9]), "1")

    def test_text_from_box_g1_p2_saves(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[10]), "4")

    def test_text_from_box_g1_p2_shots(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[11]), "1")  

    # TESTS FOR test1.png 3rd PLAYER
    def test_text_from_box_g1_p3_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[12]), "vek.")
    
    def test_text_from_box_g1_p3_score(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[13]), "321")

    def test_text_from_box_g1_p3_goals(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[14]), "0")
        
    def test_text_from_box_g1_p3_assists(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[15]), "3")

    def test_text_from_box_g1_p3_saves(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[16]), "0")

    def test_text_from_box_g1_p3_shots(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[17]), "0")

    # TESTS FOR test1.png 4th PLAYER
    def test_text_from_box_g1_p4_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[18]), "LEGEND? YT")
    
    def test_text_from_box_g1_p4_score(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[19]), "292")

    def test_text_from_box_g1_p4_goals(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[20]), "2")
        
    def test_text_from_box_g1_p4_assists(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[21]), "0")

    def test_text_from_box_g1_p4_saves(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[22]), "0")

    def test_text_from_box_g1_p4_shots(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[23]), "3")

    # TESTS FOR test1.png 5th PLAYER
    def test_text_from_box_g1_p5_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[24]), "TT7")
    
    def test_text_from_box_g1_p5_score(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[25]), "290")

    def test_text_from_box_g1_p5_goals(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[26]), "0")
        
    def test_text_from_box_g1_p5_assists(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[27]), "0")

    def test_text_from_box_g1_p5_saves(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[28]), "2")

    def test_text_from_box_g1_p5_shots(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[29]), "3")

    # TESTS FOR test1.png 6th PLAYER
    def test_text_from_box_g1_p6_name(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[30]), "RICO")
    
    def test_text_from_box_g1_p6_score(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[31]), "194")

    def test_text_from_box_g1_p6_goals(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[32]), "0")
        
    def test_text_from_box_g1_p6_assists(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[33]), "1")

    def test_text_from_box_g1_p6_saves(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[34]), "0")

    def test_text_from_box_g1_p6_shots(self):
        self.assertEqual(text_from_box("Images/test1.png", BOXES[35]), "3")


##########################################################################################################################################
    # TESTS FOR test2.png 1st PLAYER
    def test_text_from_box_g2_p1_name(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[0]), "twitch.tv/kylverr")
    
    def test_text_from_box_g2_p1_score(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[1]), "488")

    def test_text_from_box_g2_p1_goals(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[2]), "2")
        
    def test_text_from_box_g2_p1_assists(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[3]), "1")

    def test_text_from_box_g2_p1_saves(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[4]), "1")

    def test_text_from_box_g2_p1_shots(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[5]), "5")

    # TESTS FOR test2.png 2nd PLAYER
    def test_text_from_box_g2_p2_name(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[6]), "Im Schrédinger")
    
    def test_text_from_box_g2_p2_score(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[7]), "486")

    def test_text_from_box_g2_p2_goals(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[8]), "2")
        
    def test_text_from_box_g2_p2_assists(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[9]), "1")

    def test_text_from_box_g2_p2_saves(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[10]), "1")

    def test_text_from_box_g2_p2_shots(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[11]), "5")  

    # TESTS FOR test2.png 3rd PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[12]), "RICO")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[13]), "282")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[14]), "0")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[15]), "1")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[16]), "1")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[17]), "1")

    # TESTS FOR test2.png 4th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[18]), "TT7")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[19]), "371")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[20]), "0")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[21]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[22]), "3")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[23]), "3")

    # TESTS FOR test2.png 5th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[24]), "LEGEND? YT")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[25]), "333")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[26]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[27]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[28]), "1")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[29]), "4")

    # TESTS FOR test2.png 6th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[30]), "vek.")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[31]), "235")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[32]), "0")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[33]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[34]), "2")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test2.png", BOXES[35]), "1")

##########################################################################################################################################
    # TESTS FOR test3.png 1st PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[0]), "Anarchy Fridge")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[1]), "428")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[2]), "2")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[3]), "2")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[4]), "0")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[5]), "2")

    # TESTS FOR test3.png 2nd PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[6]), "TT7")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[7]), "386")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[8]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[9]), "1")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[10]), "2")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[11]), "4")  

    # TESTS FOR test3.png 3rd PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[12]), "twitch.tv/kylverr")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[13]), "300")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[14]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[15]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[16]), "1")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[17]), "3")

    # TESTS FOR test3.png 4th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[18]), "LEGEND? YT")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[19]), "337")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[20]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[21]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[22]), "2")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[23]), "2")

    # TESTS FOR test3.png 5th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[24]), "RICO")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[25]), "194")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[26]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[27]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[28]), "0")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[29]), "2")

    # TESTS FOR test3.png 6th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[30]), "Im Schrédinger")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[31]), "189")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[32]), "0")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[33]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[34]), "1")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test3.png", BOXES[35]), "1")

##########################################################################################################################################
    # TESTS FOR test4.png 1st PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[0]), "twitch.tv/kylverr")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[1]), "466")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[2]), "2")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[3]), "1")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[4]), "1")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[5]), "5")

    # TESTS FOR test4.png 2nd PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[6]), "Anarchy Fridge")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[7]), "303")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[8]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[9]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[10]), "0")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[11]), "4")  

    # TESTS FOR test4.png 3rd PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[12]), "LEGEND? YT")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[13]), "242")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[14]), "0")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[15]), "1")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[16]), "0")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[17]), "7")

    # TESTS FOR test4.png 4th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[18]), "TT7")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[19]), "757")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[20]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[21]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[22]), "6")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[23]), "3")

    # TESTS FOR test4.png 5th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[24]), "RICO")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[25]), "346")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[26]), "1")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[27]), "1")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[28]), "2")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[29]), "0")

    # TESTS FOR test4.png 6th PLAYER
    def test_text_from_box_g1_p1_name(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[30]), "Im Schrédinger")
    
    def test_text_from_box_g1_p1_score(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[31]), "290")

    def test_text_from_box_g1_p1_goals(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[32]), "0")
        
    def test_text_from_box_g1_p1_assists(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[33]), "0")

    def test_text_from_box_g1_p1_saves(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[34]), "2")

    def test_text_from_box_g1_p1_shots(self):
        self.assertEqual(text_from_box("Images/test4.png", BOXES[35]), "0")
        
##########################################################################################################################################
    # TESTS FOR test5.png 1st PLAYER
    def test_text_from_box_g5_p1_name(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[0]), "TT7")
    
    def test_text_from_box_g5_p1_score(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[1]), "404")

    def test_text_from_box_g5_p1_goals(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[2]), "1")
        
    def test_text_from_box_g5_p1_assists(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[3]), "1")

    def test_text_from_box_g5_p1_saves(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[4]), "1")

    def test_text_from_box_g5_p1_shots(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[5]), "6")

    # TESTS FOR test5.png 2nd PLAYER
    def test_text_from_box_g5_p2_name(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[6]), "Anarchy Fridge")
    
    def test_text_from_box_g5_p2_score(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[7]), "364")

    def test_text_from_box_g5_p2_goals(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[8]), "2")
        
    def test_text_from_box_g5_p2_assists(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[9]), "0")

    def test_text_from_box_g5_p2_saves(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[10]), "1")

    def test_text_from_box_g5_p2_shots(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[11]), "1")  

    # TESTS FOR test5.png 3rd PLAYER
    def test_text_from_box_g5_p3_name(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[12]), "LEGEND? YT")
    
    def test_text_from_box_g5_p3_score(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[13]), "364")

    def test_text_from_box_g5_p3_goals(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[14]), "1")
        
    def test_text_from_box_g5_p3_assists(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[15]), "2")

    def test_text_from_box_g5_p3_saves(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[16]), "0")

    def test_text_from_box_g5_p3_shots(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[17]), "3")

    # TESTS FOR test5.png 4th PLAYER
    def test_text_from_box_g5_p4_name(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[18]), "twitch.tv/kylverr")
    
    def test_text_from_box_g5_p4_score(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[19]), "750")

    def test_text_from_box_g5_p4_goals(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[20]), "3")
        
    def test_text_from_box_g5_p4_assists(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[21]), "0")

    def test_text_from_box_g5_p4_saves(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[22]), "3")

    def test_text_from_box_g5_p4_shots(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[23]), "5")

    # TESTS FOR test5.png 5th PLAYER
    def test_text_from_box_g5_p5_name(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[24]), "Im Schrédinger")
    
    def test_text_from_box_g5_p5_score(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[25]), "204")

    def test_text_from_box_g5_p5_goals(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[26]), "0")
        
    def test_text_from_box_g5_p5_assists(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[27]), "1")

    def test_text_from_box_g5_p5_saves(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[28]), "2")

    def test_text_from_box_g5_p5_shots(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[29]), "0")

    # TESTS FOR test5.png 6th PLAYER
    def test_text_from_box_g5_p6_name(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[30]), "RICO")
    
    def test_text_from_box_g5_p6_score(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[31]), "162")

    def test_text_from_box_g5_p6_goals(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[32]), "0")
        
    def test_text_from_box_g5_p6_assists(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[33]), "1")

    def test_text_from_box_g5_p6_saves(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[34]), "0")

    def test_text_from_box_g5_p6_shots(self):
        self.assertEqual(text_from_box("Images/test5.png", BOXES[35]), "3")
    
if __name__ == '__main__':
    unittest.main()