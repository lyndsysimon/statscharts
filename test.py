import numpy as np
import pandas as pd
import unittest

from controlcharts import *

class TestIChart(unittest.TestCase):
    DATASET_LIST = [
        3.9756983644,
        3.7713126251,
        3.3275001762,
        3.6391279767,
        3.0765596079,
        3.9051652765,
        3.0581050608,
        3.0522579723,
        3.6764779016,
        3.3856052374,
        3.6913859495,
        3.7530375095,
        3.2907705139,
        3.7494910103,
        3.8052954823,
        3.9672484156,
        3.1350962478,
        3.4966814318,
        3.7202859251
    ]
    DATASET_DICT = { 'mycol': DATASET_LIST }
    DATASET_SERIES = pd.Series(DATASET_LIST)
    DATASET_DATAFRAME = pd.DataFrame(DATASET_SERIES, columns=['testcol',])

    def setUp(self):
        self.MEAN = np.mean(self.DATASET_SERIES)
        self.LCL = self.MEAN - (3 * np.std(self.DATASET_SERIES))
        self.UCL = self.MEAN + (3 * np.std(self.DATASET_SERIES))

    def test_ichart_with_list(self):
        r = ichart(self.DATASET_LIST)
        self.assertAlmostEqual(r['mean'][0], self.MEAN)
        self.assertAlmostEqual(r['lower_limit'][0], self.LCL)
        self.assertAlmostEqual(r['upper_limit'][0], self.UCL)

    def test_ichart_with_dict(self):
        r = ichart(self.DATASET_DICT)
        self.assertAlmostEqual(r['mean'][0], self.MEAN)
        self.assertAlmostEqual(r['lower_limit'][0], self.LCL)
        self.assertAlmostEqual(r['upper_limit'][0], self.UCL)

    def test_ichart_with_series(self):
        r = ichart(self.DATASET_SERIES)
        self.assertAlmostEqual(r['mean'][0], self.MEAN)
        self.assertAlmostEqual(r['lower_limit'][0], self.LCL)
        self.assertAlmostEqual(r['upper_limit'][0], self.UCL)

    def test_ichart_with_dataframe(self):
        r = ichart(self.DATASET_DATAFRAME)
        self.assertAlmostEqual(r['mean'][0], self.MEAN)
        self.assertAlmostEqual(r['lower_limit'][0], self.LCL)
        self.assertAlmostEqual(r['upper_limit'][0], self.UCL)


if __name__ == '__main__':
    unittest.main()