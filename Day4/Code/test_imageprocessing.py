"""
test_imageprocessing.py

Authors: Katie Williams (@kwi11iams) 

This code runs tests on the image processing code to check the outputs are as expected
"""
import unittest # This is the automatic test runner
from Assignment2 import cost, registered_images, shiftImage

import pydicom
import numpy as np
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import matplotlib.pyplot as plt

# Load the images “IMG-0004-00001.dcm” and “IMG-0004-00002.dcm”. get the pixel data
img1_dcm = pydicom.read_file("IMG-0004-00001.dcm")
img2_dcm = pydicom.read_file("IMG-0004-00002.dcm")

# Convert dicom file to a numpy array using img1_array = img1_dcm.pixel_array
img1_array = img1_dcm.pixel_array 
img2_array = img2_dcm.pixel_array

zero_shift = [0,0]

# start a new figure
fig, ax = plt.subplots()
ax.imshow(img1_array, alpha=0.5, cmap="Greens_r")
img2 = ax.imshow(img2_array, alpha=0.5, cmap="Purples_r")


class TestImageProcessing(unittest.TestCase):
    """
    Class TestImageProcessing automates running the tests, and reports failure if
    the output is not what is expected
    """

    def test_cost1(self):
        self.assertEqual(cost(img1_array, img1_array), 0)

    def test_cost2(self):
        self.assertEqual(cost(img2_array, img2_array), 0)
    
    def test_cost3(self):
        self.assertNotEqual(cost(img1_array, img2_array), 0)

    def test_cost34(self):
        self.assertTrue(cost(img1_array, img2_array)>0)


if __name__ == "__main__":
    unittest.main()