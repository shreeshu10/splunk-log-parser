import re
from datetime import datetime, timedelta
threshold=50
lines=0
WINDOW= timedelta(minutes=2)
def parse_log(log):
    if not log.strip():
        return None
        
    log_line=log.split()
    match= re.search(r'message="(.+?)"',log)
    log_entry={"timestamp": log_line[0] + " " + log_line[1],
        "log_level": log_line[2],
        "host": log_line[3].split('=')[1],
        "message": match.group(1) if match else "no message"
    }
    return log_entry

def detect_anomaly(log_entry):

    timestamps=[]

    for entry in log_entry:
        ts=datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
        timestamps.append(ts)

    for i in range(len(timestamps)):
        window_start=timestamps[i]
        window_end=window_start+WINDOW

        count=0
        for t in timestamps:
            if window_start<=t <=window_end :
                count+=1

        if count>threshold:
            #print(f" {count} Anomaly detected between time range {window_start} and {window_end}")  
            return True, window_start, window_end, count 
    print("[OK] No anomaly detected")
    return False, 0, 0, 0 

def print_summary(lines, flagged_lines, anomaly_detected, window_start, window_end, count):
    print("======================================")
    print("SUMMARY REPORT")
    print("======================================")
    print(f"Total line parsed: {lines}")
    print(f"Total flagged lines: {len(flagged_lines)}")
    print(f"Anomaly Detected: {anomaly_detected}")
    if anomaly_detected:
        print(f"Anomaly Time Window: {window_start} to {window_end}")
        print(f"Number of events in window: {count}")
    print("======================================")

anomaly=["failed", "timeout", "connection refused"]
flagged_lines=[]    
with open("splunk_sample.log", 'r') as log:
    for line in log:
        lines+=1
        entry= parse_log(line)
        if not entry:
            continue
        else:
            msg_flags=any( flag in entry["message"].lower() for flag in anomaly)
            if entry["log_level"] in ["ERROR", "CRITICAL"] or msg_flags:
                flagged_lines.append(entry)

anomaly_detected, window_start, window_end, count= detect_anomaly(flagged_lines)

print_summary(lines, flagged_lines, anomaly_detected, window_start, window_end, count)
