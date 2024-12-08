# Feature Extraction from Sensor Data

This Python script performs feature extraction on sensor data contained in a CSV file. The data is expected to have multiple columns representing different sensor readings (e.g., accelerometer, gyroscope, speed). The script extracts 24 statistical features (mean, standard deviation, skewness, kurtosis, etc.) from every 7th value in each column of the input CSV, then outputs the results to a new CSV file.

## Overview

The script processes raw sensor data and calculates several statistical features for each sensor (acceleration, gyroscope, speed, etc.). For each sensor type (acceleration on x, y, and z axes, gyroscope on x, y, and z axes, and speed), the script performs the following steps:

1. **Extract every 7th value** from each column in the input data (starting from the first row).
2. **Calculate 24 features** for each set of extracted values.
3. **Write the feature names and values** into an output CSV file.

The features computed for each sensor data column include:
- Mean
- Minimum and Maximum values
- Median
- Standard Deviation
- Coefficient of Variation
- Peak-to-Peak Range
- Percentiles (25th and 75th)
- Interquartile Range
- Skewness and Kurtosis
- Signal Power
- Root Mean Square (RMS)
- Peak Intensity (Number of peaks)
- Autocorrelation
- Trapezoidal Numerical Integration
- Pitch and Roll Angles (for angular data)
- Signal Magnitude Area
- Signal Vector Magnitude
- Median Crossings
- Power Spectral Density (PSD)

## Requirements

- Python 3.x
- Libraries: `numpy`, `csv`

To install the required libraries, you can use `pip`:

```bash
pip install numpy
