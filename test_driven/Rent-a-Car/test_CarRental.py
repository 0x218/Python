# 5 steps in TDD.
## 1. write test to pass the feature specification.
## 2. run the test and it will fail - as the feature is not implemented yet.
## 3. write simplest code to make the test pass.
## 4. modify core logic and ensure all tests pass
## 5. Refactor and improvise code.
### The process of writing failing test first, then write code that makes those test pass, and refactoring is called RED-GREEN-REFACTOR.


import unittest
from Car_Rental import CarRental


class TestCarRental(unittest.TestCase):
    def setUp(self):
        self.cr = CarRental("Enterprise Cars")##carrental has dataclass decorator and thus uninitialzed variable (company_name) becomes mandatory parameter
    
    def test_Rent_a_car_cost_Premimum(self):
        self.cr.Rent_a_car(5, True)
        self.assertAlmostEqual(self.cr.Rental_cost(), 650)
    
    def test_Rent_a_car_cost_NonPremimum(self):
        self.cr.Rent_a_car(5, False)
        self.assertAlmostEqual(self.cr.Rental_cost(), 350)


if __name__ == '__main__':
    unittest.main()
