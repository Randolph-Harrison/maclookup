import netmiko
import os

def lookup_mac(mac: str, site: str) -> str:
    print(os.environ.get("PASSWORD"))
    return f"Look up: {mac} and {site}"
