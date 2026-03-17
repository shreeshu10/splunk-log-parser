# System Monitor

A Python script that continuously monitors system health metrics —
CPU, memory, and disk usage — and alerts when thresholds are breached.

Built as part of my SRE portfolio to demonstrate Python automation
and real-time system observability skills.

## What it does

- Monitors CPU, memory, and disk usage every 5 minutes
- Timestamps every reading
- Prints an alert to terminal when any metric exceeds its threshold
- Runs continuously until manually stopped

## How to run

Install dependency:
```bash
pip3 install psutil
```

Run the script:
```bash
python3 system_monitor.py
```

## Sample output
```
==================================================
[2026-03-17 19:25:41] CPU:    100.0%
ALERT: CPU usage at 100.0% — exceeds threshold of 90%
[2026-03-17 19:25:41] Memory: 51.9%
[2026-03-17 19:25:41] Disk:   93.9%
==================================================
```

## Thresholds

| Metric | Threshold |
|--------|-----------|
| CPU    | > 90%     |
| Memory | > 90%     |
| Disk   | > 95%     |

## Tech used

- Python 3
- psutil — system metrics collection
- datetime — timestamping each reading
- time — interval based monitoring

## Concepts demonstrated

- Real-time system resource monitoring
- Threshold based alerting
- Continuous monitoring with configurable intervals
- Clean function based code structure
