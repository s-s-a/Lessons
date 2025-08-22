import os
import subprocess

def  scan_wifi():
	print("Сканирование доступных WiFi сетей\n")

	if os.name == "nt":	# Windows
		result = subprocess.run(["netsh", "wlan", "show", "networks" "mode=bssid"], capture_output=True, text=True)
	else: # Linux, Mac
    # result = subprocess.run(["sudo", "iwlist", "scan"], capture_output=True, text=True)
		result = subprocess.run(["nmcli", "-f", "SSID,SIGNAL,CHAN", "dev", "wifi"], capture_output=True, text=True)

	print(result.stdout)


scan_wifi()
