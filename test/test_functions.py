# test all functions

from calculator import Calculator

class TestCalculator():
    def test_calculator(self):
        self.calc = Calculator()

        def test_add(self):
            assert self.calc.add(3,4) == 7
        
        def test_sub(self):
            assert self.calc.sub(5,3) == 2

        def test_mul(self):
            assert self.calc.mul(4,2) == 8

        def test_div(self):
            assert self.calc.div(6,3) == 2

        def test_pow(self):
            assert self.calc.pow(3,2) == 9
        
        test_add(self)
        test_sub(self)
        test_mul(self)
        test_div(self)
        test_pow(self)

    

    
        



