from machine import ADC, Pin
import time


class UV:
    
    def __init__(self, pin):
        # Configure the ADC pin (use GPIO34 or GPIO32, which are valid ADC pins)
        self.UVsensorIn = ADC(Pin(pin))  # Use GPIO34 or GPIO32 for ADC
        self.UVsensorIn.atten(ADC.ATTN_11DB)  # Set the attenuation to 0-3.3V range
        self.UVsensorIn.width(ADC.WIDTH_12BIT)  # Set the resolution to 12 bits (0-4095)


    # Function to take an average of readings
    def average_analog_read(self, pinToRead, num_readings=8):
        running_value = 0
        for _ in range(num_readings):
            running_value += pinToRead.read()  # Read the analog value
            time.sleep(0.05)  # Small delay between readings to reduce noise
        return running_value // num_readings  # Return the average


    # Function to map a float value from one range to another
    def mapfloat(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    
    def getUVIntensity(self):
        uv_level = self.average_analog_read(self.UVsensorIn)  # Read the averaged analog value
    
        # Calculate the output voltage (3.3V reference)
        output_voltage = 3.3 * uv_level / 4095.0  # Scaling the value to 0-3.3V
    
        uv_intensity = self.mapfloat(output_voltage, 0.0, 3.3, 0.0, 15.0)
        
        return uv_intensity
    
    
    def showData(self):
        # Debug: Print the raw UV level and corresponding output voltage
        #print("Raw UV Level: {}".format(uv_level))
        #print("Output Voltage: {:.2f} V".format(output_voltage))
        
        # Debug: Print the calculated UV intensity
        print("UV Intensity: {:.2f} mW/cm^2".format(self.getUVIntensity()))
