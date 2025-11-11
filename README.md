# Random Interval URL Pinger

A Python script that pings https://www.playtabissimo.com/ at random intervals between 10-20 minutes.

## Features

- Pings the URL at random intervals (10-20 minutes)
- Logs each ping attempt with timestamp
- Handles connection errors gracefully
- Can run continuously in the background

## Requirements

- Python 3.6+
- requests library

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run directly:
```bash
python url_pinger.py
```

### Run in background (Linux/Mac):
```bash
nohup python url_pinger.py > pinger.log 2>&1 &
```

### Run in background (Windows):
```bash
start /B python url_pinger.py
```

### Stop the script:
Press `Ctrl+C` if running in foreground, or find and kill the process if running in background.

## Configuration

You can modify the following variables in `url_pinger.py`:
- `URL`: The URL to ping
- `MIN_INTERVAL_MINUTES`: Minimum interval in minutes (default: 10)
- `MAX_INTERVAL_MINUTES`: Maximum interval in minutes (default: 20)

## Output

The script outputs timestamped logs for each ping attempt:
```
[2025-11-11 16:57:30] Starting URL pinger for https://www.playtabissimo.com/
[2025-11-11 16:57:30] Interval: 10-20 minutes
[2025-11-11 16:57:31] ✓ Pinged https://www.playtabissimo.com/ - Status: 200
[2025-11-11 16:57:31] Next ping in 15.3 minutes (918 seconds)
```
