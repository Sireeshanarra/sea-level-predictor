import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot(self):
        result = draw_plot()
        self.assertIsNotNone(result, "The plot should not be None")

if __name__ == "__main__":
    unittest.main()
