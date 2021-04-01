import io
import unittest
"""
This entire test is a bit of a sledgehammer, ideally the functionality would be automated, I considered passing arguments
to the test, but I read that wasn't a great idea, maybe i've misconstrued the question and you wanted something built
into the sort_names.py file that checks correctness before completing. the unit tests looked cool though so I wanted to
use them. Should demonstrate two correct sorts, and a failed one.
"""


class TestFiles(unittest.TestCase):

    def test1(self):
        act_open = io.open('output/actual_+.txt')
        act = list(act_open)
        act_open.close()

        exp_open = io.open('reference/sorted_+.txt')
        exp = list(exp_open)
        exp_open.close()

        self.assertListEqual(act, exp)

    def test2(self):
        act_open = io.open('output/actual_-.txt')
        act = list(act_open)
        act_open.close()

        exp_open = io.open('reference/sorted_-.txt')
        exp = list(exp_open)
        exp_open.close()

        self.assertListEqual(act, exp)

    


if __name__ == '__main__':
    unittest.main()
