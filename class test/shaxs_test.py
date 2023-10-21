import unittest
from shaxs_talaba import Shaxs

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        ism = "Jamshid"
        familiya = "Iskanderov"
        passport = "AA1234567"
        tyil = 1994
        self.shaxs1 = Shaxs(ism, familiya, passport, tyil)
         

    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        
            
    def test_get_info(self):
        shaxs1 = "Jamshid Iskanderov. Passport:AA1234567, 1994-yilda tug'ilgan."
        self.assertEqual(shaxs1,self.shaxs1.get_info())
        
    def test_get_age(self):
        shaxs1 = 29
        self.assertEqual(shaxs1, self.shaxs1.get_age(2023))
    
    
unittest.main()