import unittest
import Generator

class GeneratorTest(unittest.TestCase):
     def test_generator_exit(self):
         invalid_URL = "htt:/hh.com"
         generator = Generator.Generator(invalid_URL)
         res = generator.generate()
         self.assertEqual(res, -1)


if __name__ == '__main__':
    unittest.main()