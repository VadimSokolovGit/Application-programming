import re

with open("log.txt", "r", encoding="utf-8") as f:
    logs = f.readlines()

print("=== 1. Log level ERROR или WARN ===")
for line in logs:
    match = re.search(r"(\d{2}:\d{2}:\d{2})\s+(ERROR|WARN(?:ING)?)\s+(.*)", line)
    if match:
        time, level, message = match.groups()
        print(f"{time} {level} {message}")

print("\n=== 2. Строки с IP-адресами ===")
for line in logs:
    if re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line):
        match = re.search(r"(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)", line)
        if match:
            time, level, message = match.groups()
            print(f"{time} {level} {message}")
