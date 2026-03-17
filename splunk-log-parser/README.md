# Splunk Log Parser & Anomaly Detector

A Python CLI tool that parses raw Splunk log files, flags critical events,
and detects anomalies using a sliding window algorithm.

Built as part of my SRE portfolio to demonstrate Python automation
and observability skills.

## What it does

- Parses raw Splunk log files line by line
- Extracts timestamp, log level, host, and message from each line
- Flags ERROR and CRITICAL log levels
- Flags messages containing keywords: failed, timeout, connection refused
- Detects anomalies when 50+ errors occur within any 2-minute window
- Prints a clean summary report to terminal

## How to run
```bash
python3 log_parser.py
```

## Sample output
```
======================================
         SPLUNK LOG PARSER REPORT
======================================
Total lines parsed:      66
Total flagged lines:     56
Anomaly detected:        YES ⚠️
Anomaly window:          2024-03-01 14:21:00 → 2024-03-01 14:23:00
Errors in window:        56
======================================
```

## Tech used

- Python 3
- re — regex for message extraction
- datetime / timedelta — sliding window anomaly detection

## Concepts demonstrated

- Log parsing and structured data extraction
- Rate-based threshold alerting (sliding window)
- File I/O and error handling
- Clean function-based code structure
