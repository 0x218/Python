import unittest
from Car_Rental import CarRental


class TestCarRental(unittest.TestCase):
    def setUp(self):
        self.cr = CarRental("Enterprise Cars")
    
    def test_Rent_a_car_cost_Premimum(self):
        self.cr.Rent_a_car(5, True)
        self.assertAlmostEqual(self.cr.Rental_cost(), 650)
    
    def test_Rent_a_car_cost_NonPremimum(self):
        self.cr.Rent_a_car(5, False)
        self.assertAlmostEqual(self.cr.Rental_cost(), 350)


if __name__ == '__main__':
    unittest.main()
