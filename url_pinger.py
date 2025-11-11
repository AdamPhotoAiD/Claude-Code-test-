#!/usr/bin/env python3
"""
URL Pinger - Pings a specified URL at random intervals
"""
import time
import random
import requests
from datetime import datetime
import sys

# Configuration
URL = "https://www.playtabissimo.com/"
MIN_INTERVAL_MINUTES = 10
MAX_INTERVAL_MINUTES = 20

def log_message(message):
    """Print a timestamped log message"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    sys.stdout.flush()

def ping_url(url):
    """Ping the specified URL and return the status"""
    # Headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        log_message(f"✓ Pinged {url} - Status: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        log_message(f"✗ Failed to ping {url} - Error: {str(e)}")
        return False

def get_random_interval():
    """Get a random interval between MIN and MAX minutes in seconds"""
    minutes = random.uniform(MIN_INTERVAL_MINUTES, MAX_INTERVAL_MINUTES)
    return minutes * 60

def main():
    """Main loop to ping URL at random intervals"""
    log_message(f"Starting URL pinger for {URL}")
    log_message(f"Interval: {MIN_INTERVAL_MINUTES}-{MAX_INTERVAL_MINUTES} minutes")

    try:
        while True:
            # Ping the URL
            ping_url(URL)

            # Calculate next interval
            interval_seconds = get_random_interval()
            interval_minutes = interval_seconds / 60

            log_message(f"Next ping in {interval_minutes:.1f} minutes ({interval_seconds:.0f} seconds)")

            # Wait for the random interval
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        log_message("Pinger stopped by user")
        sys.exit(0)
    except Exception as e:
        log_message(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
