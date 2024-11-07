from machine import ADC, Pin
import time

# Configure the ADC pin (use GPIO34 or GPIO32, which are valid ADC pins)
UVsensorIn = ADC(Pin(34))  # Use GPIO34 or GPIO32 for ADC
UVsensorIn.atten(ADC.ATTN_11DB)  # Set the attenuation to 0-3.3V range
UVsensorIn.width(ADC.WIDTH_12BIT)  # Set the resolution to 12 bits (0-4095)

# Function to take an average of readings
def average_analog_read(pinToRead, num_readings=8):
    running_value = 0
    for _ in range(num_readings):
        running_value += pinToRead.read()  # Read the analog value
        time.sleep(0.05)  # Small delay between readings to reduce noise
    return running_value // num_readings  # Return the average

# Function to map a float value from one range to another
def mapfloat(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Main loop
while True:
    uv_level = average_analog_read(UVsensorIn)  # Read the averaged analog value
    
    # Calculate the output voltage (3.3V reference)
    output_voltage = 3.3 * uv_level / 4095.0  # Scaling the value to 0-3.3V
    
    # Debug: Print the raw UV level and corresponding output voltage
    print("Raw UV Level: {}".format(uv_level))
    print("Output Voltage: {:.2f} V".format(output_voltage))
    
    # Adjusted map function for voltage-to-UV intensity conversion
    # Modify the voltage range to more accurately reflect your sensor's behavior
    # Assume 0.85V corresponds to around 3.85 mW/cm², which is a typical indoor UV reading.
    # Map voltage range 0V-3.3V to UV intensity range 0-15 mW/cm².
    uv_intensity = mapfloat(output_voltage, 0.0, 3.3, 0.0, 15.0)
    
    # Debug: Print the calculated UV intensity
    print("UV Intensity: {:.2f} mW/cm^2".format(uv_intensity))
    
    # Wait 200ms before the next reading
    time.sleep(0.2)
