import unittest
import BERT2

class Testtemp(unittest.TestCase):
    def test_AI(self):
        
        test1 = "Those agents may have gotten a lift in the waning days of Mr. Trumps administration, when Trump loyalists tried to codify the influence of those unions. The day before Mr. Bidens inauguration, union leaders signed a labor agreement with Kenneth T. Cuccinelli II, an immigration hard-liner and the acting deputy secretary of the Department of Homeland Security, that requires ICEs political leadership to consult with the union on policy decisions. Under federal law, an agency chief has 30 days to cancel such an agreement once it is signed"
        
        test2 = "Translation: in the absence of symptoms, a high Ct value means you are highly unlikely to become ill or get anyone else sick in the absence of very recent exposure to an infected person. Dr. Fauci knew this in July when he said that tests with a Ct above 35 were likely picking up viral debris or dead virus. Even at a Ct of 35, the incidence of virus samples that could replicate is very low, according to Jaafar et al. The only state I know that requires reporting the Ct with every test is Florida, which started this policy in December. The WHO went on"

        test3 = "be magically solved just in time for Joe Biden to look like a hero. For doing absolutely nothing. Do not tell me there is not a politicized deep state in these health agencies. Do not ever tell me I need to listen to Dr. Anthony Fauci again. And every business owner who has been ruined because of lockdowns due to a high number of cases should be livid. Any parent whose child has lost a year of school should be furious. None of this was for your health. It was to get rid of Orange Man Bad. Editors Note: This article has been updated to remove language"

        test4 = "That was fast. All Department of the Interior employees today received a system-wide email from the incoming Biden administration leadership, which I obtained. Instead of worrying about bison, national parks, and federal lands, the message had a different focus. It was race and identity politics. The email to all Department of the Interior employees starts: Good afternoon! My name is Jennifer Van der Heide, and it is my distinct honor to serve as the incoming Chief of Staff for the Interior Department. On behalf of the Biden-Harris"
        
        result1 = BERT2.main_func(test1)
        result2 = BERT2.main_func(test2)
        result3 = BERT2.main_func(test3)
        result4 = BERT2.main_func(test4)

        self.assertEqual(result1, 0)
        self.assertEqual(result2, 1)
        self.assertEqual(result3, 1)
        self.assertEqual(result4, 2)

if __name__ == "__main__":
    unittest.main()