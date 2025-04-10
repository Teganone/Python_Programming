def intersection(list1, list2):
    return list(set(list1) & set(list2))


import unittest

class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        test_cases = [
            # 测试用例1：两个列表都为空
            {
                "name": "两个列表都为空",
                "input": ([], []),
                "expected": []
            },
            # 测试用例2：列表1为空，列表2不为空
            {
                "name": "列表1为空，列表2不为空",
                "input": ([], [1, 2, 3]),
                "expected": []
            },
            # 测试用例3：列表1不为空，列表2为空
            {
                "name": "列表1不为空，列表2为空",
                "input": ([1, 2, 3], []),
                "expected": []
            },
            # 测试用例4：两个列表都不为空，且有交集
            {
                "name": "两个列表都不为空，且有交集",
                "input": ([1, 2, 3], [2, 3, 4]),
                "expected": [2, 3]
            },
            # 测试用例5：两个列表都不为空，且无交集
            {
                "name": "两个列表都不为空，且无交集",
                "input": ([1, 2, 3], [4, 5, 6]),
                "expected": []
            },
        ]

        for test_case in test_cases:
            print(f"正在执行测试用例：{test_case['name']}")
            result = intersection(*test_case['input'])
            self.assertEqual(result, test_case['expected'])

if __name__ == '__main__':

    # list1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10,"ddd"]
    # list2 = [1, 2, 3, 4, 4, "ww",'sss','ddd']
    # print(intersection(list1, list2))

    unittest.main()
