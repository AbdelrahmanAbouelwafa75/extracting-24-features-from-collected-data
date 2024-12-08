import csv
import numpy as np

# File paths
input_file = "input_without_target.csv"  # Replace with your input file path
output_file = "output_with_features.csv"

# Define the functions for the 24 equations
def calculate_features(values):
    try:
        # Convert the values to numeric values, leaving non-numeric values as NaN
        values_numeric = []
        for value in values:  # Iterate over the provided values
            try:
                values_numeric.append(float(value))
            except ValueError:
                values_numeric.append(np.nan)
        
        # Remove NaN values from the values for calculation
        values_clean = [x for x in values_numeric if not np.isnan(x)]
        
        # If there are no valid values, return None for all features
        if len(values_clean) == 0:
            return [None] * 24

        # Keep numbers in `arr` rounded to 2 decimal places
        arr = np.array(values_clean)
        arr = np.round(arr, 2)

        # Calculate basic statistics
        mean = np.mean(arr)
        minimum = np.min(arr)
        maximum = np.max(arr)
        median = np.median(arr)
        std_dev = np.std(arr, ddof=0)
        coeff_var = std_dev / mean if mean != 0 else None
        peak_to_peak = maximum - minimum

        # Percentiles and interquartile range
        percentile_25 = np.percentile(arr, 25)
        percentile_75 = np.percentile(arr, 75)
        interquartile_range = percentile_75 - percentile_25

        # Higher-order statistics
        skewness = (np.mean((arr - mean) ** 3)) / (std_dev ** 3) if std_dev != 0 else None
        kurtosis = (np.mean((arr - mean) ** 4)) / (std_dev ** 4) if std_dev != 0 else None

        # Signal properties
        signal_power = np.sum(arr ** 2)
        root_mean_square = np.sqrt(np.mean(arr ** 2))

        # Peak intensity (number of peaks)
        peak_intensity = np.sum((arr[1:-1] > arr[:-2]) & (arr[1:-1] > arr[2:]))

        # Autocorrelation
        autocorrelation = np.sum((arr - mean) * (np.roll(arr, 1) - mean)) / len(arr) if len(arr) > 1 else None

        # Trapezoidal Numerical Integration
        trapezoidal_integration = np.trapz(arr)

        # Angular features (only if there are at least 3 values)
        pitch_angle = np.arctan2(arr[0], np.sqrt(arr[1]**2 + arr[2]**2)) if len(arr) >= 3 else None
        roll_angle = np.arctan2(arr[1], np.sqrt(arr[0]**2 + arr[2]**2)) if len(arr) >= 3 else None

        # Signal magnitude and vector magnitude
        signal_magnitude_area = np.mean(np.abs(arr))
        signal_vector_magnitude = np.sqrt(np.sum(arr ** 2))

        # Median crossings
        median_crossings = np.sum((arr[:-1] - median) * (arr[1:] - median) < 0)

        # Power spectral density (PSD)
        frequencies = np.fft.fftfreq(len(arr))
        fft_values = np.fft.fft(arr)
        psd = np.sum((fft_values.real ** 2 + fft_values.imag ** 2) * np.abs(frequencies))

        # Return all computed features
        return [
            mean, minimum, maximum, median, std_dev, coeff_var, peak_to_peak,
            percentile_25, percentile_75, interquartile_range, skewness, kurtosis,
            signal_power, root_mean_square, peak_intensity,
            autocorrelation, trapezoidal_integration,
            pitch_angle, roll_angle, signal_magnitude_area,
            signal_vector_magnitude, median_crossings, psd
        ]
    except Exception as e:
        # Handle any computation errors and return None for all features
        print(f"Error calculating features: {e}")
        return [None] * 24

def get_every_seventh_number(arr,s):
    return arr[s::7]

try:
    # Open the CSV file in read mode
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        # Create a CSV reader object
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        feature_names = [
        "accx_mean", "accx_min", "accx_max", "accx_median", "accx_std_dev",
        "accx_coeff_var", "accx_peak_to_peak", "accx_percentile_25", "accx_percentile_75", 
        "accx_interquartile_range", "accx_skewness", "accx_kurtosis", "accx_signal_power", 
        "accx_root_mean_square", "accx_peak_intensity", "accx_autocorrelation", 
        "accx_trapezoidal_integration", "accx_pitch_angle", "accx_roll_angle", 
        "accx_signal_magnitude_area", "accx_signal_vector_magnitude", "accx_median_crossings", 
        "accx_psd", 
        "accy_mean", "accy_min", "accy_max", "accy_median", "accy_std_dev",
        "accy_coeff_var", "accy_peak_to_peak", "accy_percentile_25", "accy_percentile_75", 
        "accy_interquartile_range", "accy_skewness", "accy_kurtosis", "accy_signal_power", 
        "accy_root_mean_square", "accy_peak_intensity", "accy_autocorrelation", 
        "accy_trapezoidal_integration", "accy_pitch_angle", "accy_roll_angle", 
        "accy_signal_magnitude_area", "accy_signal_vector_magnitude", "accy_median_crossings", 
        "accy_psd",
        "accz_mean", "accz_min", "accz_max", "accz_median", "accz_std_dev",
        "accz_coeff_var", "accz_peak_to_peak", "accz_percentile_25", "accz_percentile_75", 
        "accz_interquartile_range", "accz_skewness", "accz_kurtosis", "accz_signal_power", 
        "accz_root_mean_square", "accz_peak_intensity", "accz_autocorrelation", 
        "accz_trapezoidal_integration", "accz_pitch_angle", "accz_roll_angle", 
        "accz_signal_magnitude_area", "accz_signal_vector_magnitude", "accz_median_crossings", 
        "accz_psd",
        # Repeat similar naming for gyrox, gyroy, gyroz, and speed
        "gyrox_mean", "gyrox_min", "gyrox_max", "gyrox_median", "gyrox_std_dev",
        "gyrox_coeff_var", "gyrox_peak_to_peak", "gyrox_percentile_25", "gyrox_percentile_75", 
        "gyrox_interquartile_range", "gyrox_skewness", "gyrox_kurtosis", "gyrox_signal_power", 
        "gyrox_root_mean_square", "gyrox_peak_intensity", "gyrox_autocorrelation", 
        "gyrox_trapezoidal_integration", "gyrox_pitch_angle", "gyrox_roll_angle", 
        "gyrox_signal_magnitude_area", "gyrox_signal_vector_magnitude", "gyrox_median_crossings", 
        "gyrox_psd",
        "gyroy_mean", "gyroy_min", "gyroy_max", "gyroy_median", "gyroy_std_dev",
        "gyroy_coeff_var", "gyroy_peak_to_peak", "gyroy_percentile_25", "gyroy_percentile_75", 
        "gyroy_interquartile_range", "gyroy_skewness", "gyroy_kurtosis", "gyroy_signal_power", 
        "gyroy_root_mean_square", "gyroy_peak_intensity", "gyroy_autocorrelation", 
        "gyroy_trapezoidal_integration", "gyroy_pitch_angle", "gyroy_roll_angle", 
        "gyroy_signal_magnitude_area", "gyroy_signal_vector_magnitude", "gyroy_median_crossings", 
        "gyroy_psd",
        "gyroz_mean", "gyroz_min", "gyroz_max", "gyroz_median", "gyroz_std_dev",
        "gyroz_coeff_var", "gyroz_peak_to_peak", "gyroz_percentile_25", "gyroz_percentile_75", 
        "gyroz_interquartile_range", "gyroz_skewness", "gyroz_kurtosis", "gyroz_signal_power", 
        "gyroz_root_mean_square", "gyroz_peak_intensity", "gyroz_autocorrelation", 
        "gyroz_trapezoidal_integration", "gyroz_pitch_angle", "gyroz_roll_angle", 
        "gyroz_signal_magnitude_area", "gyroz_signal_vector_magnitude", "gyroz_median_crossings", 
        "gyroz_psd",
        "speed_mean", "speed_min", "speed_max", "speed_median", "speed_std_dev",
        "speed_coeff_var", "speed_peak_to_peak", "speed_percentile_25", "speed_percentile_75", 
        "speed_interquartile_range", "speed_skewness", "speed_kurtosis", "speed_signal_power", 
        "speed_root_mean_square", "speed_peak_intensity", "speed_autocorrelation", 
        "speed_trapezoidal_integration", "speed_pitch_angle", "speed_roll_angle", 
        "speed_signal_magnitude_area", "speed_signal_vector_magnitude", "speed_median_crossings", 
        "speed_psd"
    ]

        writer.writerow(feature_names)
        # Loop through each row in the CSV and print it
        for row in reader:
            feature_values = []
            
            # Get every 7th number starting from the first index of each column and calculate the features
            for i in range(7):  # Assuming 7 columns of data to process
                feature_values.extend(calculate_features(get_every_seventh_number(row, i)))
                print(get_every_seventh_number(row, i))
            #print(feature_values)
            writer.writerow(feature_values)

                

except FileNotFoundError:
    print(f"The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")