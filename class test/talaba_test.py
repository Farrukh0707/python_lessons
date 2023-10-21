import unittest
from shaxs_talaba import Talaba

class TalabaTest(unittest.TestCase):
    def setUp(self):
        ism = "Adham"
        familiya = "Qorjovov"
        passport = "AB7654321"
        tyil = 30
        idraqam = "AB123456"
        manzil = "Qashqadaryo viloyati, G'uzor tumani, Olchazor ko'chasi, 5-uy"
        self.talaba1 = Talaba(ism,familiya,passport,tyil,idraqam,manzil)
        
    def test_create(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertEqual(30, self.talaba1.tyil)
        self.assertEqual("AB123456", self.talaba1.idraqam)
        self.assertEqual("Qashqadaryo viloyati, G'uzor tumani, Olchazor ko'chasi, 5-uy", self.talaba1.manzil)

    

unittest.main()    