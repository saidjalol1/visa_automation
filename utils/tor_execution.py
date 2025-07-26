import socket
import time
import subprocess
from pathlib import Path

TOR_EXE_PATH = Path(__file__).resolve().parent.parent / "tor-expert-bundle-windows-i686-14.5.5" / "tor" / "tor.exe"


def wait_for_tor_proxy(host="127.0.0.1", port=9050, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=3):
                print("Tor proxy is available.")
                return True
        except OSError:
            print("Waiting for Tor to start...")
            time.sleep(1)
    raise TimeoutError("Tor SOCKS5 proxy did not become available.")


def run_tor():
    print("Starting Tor...")
    return subprocess.Popen([str(TOR_EXE_PATH)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)