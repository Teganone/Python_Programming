def count_above_90(scores):
    return sum(1 for score in scores if score > 90)


import unittest

class TestCountAbove90(unittest.TestCase):
    def test_count_above_90(self):
        test_cases = [
            # 测试用例1：输入为空列表，期望输出为0
            {
                "input": [],
                "expected": 0
            },
            # 测试用例2：输入列表中所有元素都小于或等于90，期望输出为0
            {
                "input": [90, 80, 70],
                "expected": 0
            },
            # 测试用例3：输入列表中有一个元素大于90，期望输出为1
            {
                "input": [90, 80, 100],
                "expected": 1
            },
            # 测试用例4：输入列表中所有元素都大于90，期望输出为列表长度
            {
                "input": [91, 92, 93],
                "expected": 3
            },
            # 测试用例5：输入列表中有一些元素大于90，有一些元素小于或等于90，期望输出为大于90的元素个数
            {
                "input": [91, 90, 89, 100, 101],
                "expected": 3
            },
        ]

        for test_case in test_cases:
            actual = count_above_90(test_case["input"])
            self.assertEqual(actual, test_case["expected"])

if __name__ == "__main__":
    unittest.main()

