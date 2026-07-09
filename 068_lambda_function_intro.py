# Simulated log lines from /var/log/syslog
logs = [
    "Jan 10 08:12:01 sshd[1234]: Accepted publickey for root",
    "Jan 10 08:15:22 kernel: [ 45.12] EXT4-fs error on dev sda1",
    "Jan 10 08:20:00 systemd: Started Periodic Command Scheduler",
    "Jan 10 08:22:11 kernel: [ 89.44] EXT4-fs error on dev sda1",
]
# Extract only the kernel errors in a single line
kernel_errors = list(filter(lambda line: "kernel" in line, logs))

print(kernel_errors)