def avarage_of_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    if not evens:
        return 0
    return sum(evens)/len(evens)
import unittest

class TestAvarageOfEvens(unittest.TestCase):
    def test_avarage_of_evens(self):
        test_cases = [
            # 测试用例1：输入列表中包含偶数
            {
                "input": [1, 2, 3, 4, 5, 6],
                "expected": 4
            },
            # 测试用例2：输入列表中不包含偶数
            {
                "input": [1, 3, 5, 7, 9],
                "expected": 0
            },
            # 测试用例3：输入列表为空
            {
                "input": [],
                "expected": 0
            },
            # 测试用例4：输入列表中所有元素都是偶数
            {
                "input": [2, 4, 6, 8, 10],
                "expected": 6
            },
        ]

        for test_case in test_cases:
            result = avarage_of_evens(test_case["input"])
            self.assertEqual(result, test_case["expected"])

if __name__ == '__main__':
    unittest.main()
