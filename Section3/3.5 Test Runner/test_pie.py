import nose
class TestPie():
    def test_charge(self):
        x = 0
        assert 0 == 0
        x += 2
        x += 4

        assert x == 6
        assert x > 0

    def test_pay(self):
        assert 10 > 0


class TestPie():
    def test_pay(self):
        assert 10 > 0

    def test_negative(self):
        x = -10
        x += 10

        assert x == 0
        x += 10
        assert x == 10

        x = x *10
        assert x < 1000

        assert 10 < x
        assert x > 0

    def test_negative2(self):
        assert -10 < 0

