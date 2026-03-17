import psutil
import time
from datetime import datetime

threshold_cpu= 90
threshold_mem= 90
threshold_disk= 95

def print_alert(metric, threshold, value):
    print(f"ALERT: {metric} usage at {value}% — exceeds threshold of {threshold}%")

def check_cpu(timestamp):
    cpu=psutil.cpu_percent(interval=1)
    print(f"[{timestamp}] CPU : {cpu}%")

    if cpu > threshold_cpu:
        print_alert("cpu", threshold_cpu, cpu)

def check_memory(timestamp):
    mem=psutil.virtual_memory().percent
    print(f"[{timestamp}] Memory : {mem}%")
    if mem > threshold_mem:
        print_alert("memory", threshold_mem, mem)

def check_disk(timestamp):
    disk=psutil.disk_usage("/").percent
    print(f"[{timestamp}] Disk : {disk}%")
    if disk > threshold_disk:
        print_alert("disk", threshold_disk, disk)
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("="*50)
    check_cpu(timestamp)
    check_memory(timestamp)
    check_disk(timestamp)
    time.sleep(300)
