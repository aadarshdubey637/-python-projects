import subprocess

def get_wifi_passwords():
    # कमांड से सभी WiFi प्रोफाइल प्राप्त करें
    output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout

    # WiFi प्रोफाइल के नाम निकालें
    profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]

    wifi_details = {}





    for profile in profiles:
        # हर प्रोफाइल का पासवर्ड निकालें
        result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True).stdout
        password_lines = [line.split(":")[1].strip() for line in result.split("\n") if "Key Content" in line]

        password = password_lines[0] if password_lines else "Not Found"
        wifi_details[profile] = password

    return wifi_details

# WiFi पासवर्ड प्राप्त करें और प्रिंट करें
wifi_passwords = get_wifi_passwords()
for wifi, password in wifi_passwords.items():
    print(f"WiFi: {wifi}, Password: {password}")

