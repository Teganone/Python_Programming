import unittest

def is_true_subset(sublst, lst):
    return set(sublst) < set(lst)


class TestIsTrueSubset(unittest.TestCase):
    def test_is_true_subset(self):
        test_cases = [
            # 测试用例1：sublst是lst的真子集
            {
                "input": ([1, 2], [1, 2, 3, 4]),
                "expected": True
            },
            # 测试用例2：sublst不是lst的真子集，但是是其子集
            {
                "input": ([1, 2, 3, 4], [1, 2, 3, 4]),
                "expected": False
            },
            # 测试用例3：sublst不是lst的子集
            {
                "input": ([1, 2, 5], [1, 2, 3, 4]),
                "expected": False
            },
            # 测试用例4：sublst和lst都为空
            {
                "input": ([], []),
                "expected": False
            },
            # 测试用例5：sublst为空，lst不为空
            {
                "input": ([], [1, 2, 3, 4]),
                "expected": True
            },
        ]

        for test_case in test_cases:
            sublst, lst = test_case["input"]
            expected = test_case["expected"]
            with self.subTest(sublst=sublst, lst=lst):
                self.assertEqual(is_true_subset(sublst, lst), expected)

if __name__ == '__main__':
    unittest.main()


