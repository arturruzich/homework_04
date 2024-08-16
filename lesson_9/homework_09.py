import unittest

# hw 7, task 7

def calculate_total_sea_area(black_sea_area, azov_sea_area):
    return black_sea_area + azov_sea_area

class TestCalculateTotalSeaArea(unittest.TestCase):

    def test_positive_areas(self):
        black_sea = 436402
        azov_sea = 37800
        result = calculate_total_sea_area(black_sea, azov_sea)
        self.assertEqual(result, 474202)

    def test_zero_area(self):
        black_sea = 0
        azov_sea = 37800
        result = calculate_total_sea_area(black_sea, azov_sea)
        self.assertEqual(result, 37800)

if __name__ == '__main__':
    unittest.main()


#hm 7, task 5


def find_longest_word(words):
    if not words:
        return ""
    return max(words, key=len)

class TestFindLongestWord(unittest.TestCase):

    def test_longest_word(self):
        words_list = ["QA", "Automation", "Python", "Manual", "Engineer"]
        result = find_longest_word(words_list)
        self.assertEqual(result, "Automation")

    def test_empty_list(self):
        words_list =[]
        result = find_longest_word(words_list)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()



#hw 7, task 9

def calculate_computer_cost(monthly_payment, months):
    return monthly_payment * months

class TestCalculateComputerCost(unittest.TestCase):

    def test_standard_case(self):
        monthly_payment = 1179
        months = 18
        result = calculate_computer_cost(monthly_payment, months)
        self.assertEqual(result, 21222)

    def test_zero_months(self):
        monthly_payment = 1179
        months = 0
        result = calculate_computer_cost(monthly_payment, months)
        self.assertEqual(result, 0)


if __name__ == '__name__':
    unittest.main()



#hw 7, task 10


def calculate_order_cost(order_list):
    total_cost = sum(quantity * price for _, quantity, price in order_list)
    return total_cost

class TestCalculateOrderCost(unittest.TestCase):

    def test_standard_order(self):
        orders = [
            ("Large pizza", 4, 274),
            ("Middle pizza", 2, 218),
            ("Juice", 4, 35),
            ("Cake", 1, 350),
            ("Water", 3, 21)
        ]
        result = calculate_order_cost(orders)
        expected = (4 * 274) + (2 * 218) + (4 * 35) + (1 * 350) + (3 * 21) # 1831 uah
        self.assertEqual(result, expected)

    def test_single_order(self):
        orders = [
            ("Juice", 4, 35)
        ]
        result = calculate_order_cost(orders)
        expected = (4 * 35) # 140
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


#hm 7, task 6

def find_substring(str1, str2):
    return str1.find(str2)

class TestFindSubstring(unittest.TestCase):

    def test_substring_found(self):
        str1 = "Hello, world!"
        str2 = "world"
        result = find_substring(str1, str2)
        expected = 7 # index of world!
        self.assertEqual(result, expected)

    def test_empty_substring(self):
        str1 = ""
        str2 = "cat"
        result = find_substring(str1, str2)
        expected = -1
        self.assertEqual(result, expected)

if __name__ == '__name__':
    unittest.main()


# total 10 test's