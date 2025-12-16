import time

logs = []

def log(msg):
    logs.append(msg)
    time.sleep(1)

log("[INFO] Home")
log("[INFO] Pick")
log("[INFO] Lift")
log("[INFO] Place")
log("Simulation Success")

# Print all logs so web app can capture them
for l in logs:
    print(l)

