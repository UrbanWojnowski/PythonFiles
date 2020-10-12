from configparser import ConfigParser

# Create object of ConfigParser class
config = ConfigParser()

# Read data from config file
config.read("C:\Development\Automation\Config.cfg")

print(config.get("Section1","username"))