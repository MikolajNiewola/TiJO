from src import lottery
import unittest


class LotteryTest(unittest.TestCase):
    def test_lottery_with_2_pairs(self):
        # arrange
        data = [1, 2, 2, 3, 4, 5, 5, 6]
        size = 2

        # act
        result = lottery.lottery(data, size)

        # assert
        self.assertEqual(result, [2, 5], "lottery should return array containing 2 and 5")

    def test_lottery_with_None_as_data(self):
        data = None
        size = 1

        result = lottery.lottery(data, size)

        self.assertEqual(result, [], "Lottery with no data should return empty array")

    def test_lottery_with_None_as_size(self):
        data = [1, 1, 2, 3, 4, 8, 4, 2]
        size = None

        result = lottery.lottery(data, size)

        self.assertEqual(result, [], "lottery with no size should return empty array")

    def test_lottery_with_None_as_both_size_and_data(self):
        data = None
        size = None

        result = lottery.lottery(data, size)

        self.assertEqual(result, [], "lottery should return an empty array if both size and data are None")

if __name__ == '__main__':
    unittest.main()
