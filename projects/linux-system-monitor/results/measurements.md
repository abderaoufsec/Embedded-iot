# Linux System Monitor Sample Output

## Sample Measurements

This file will contain sample output from the Linux System Monitor after implementation.

## Expected Output Format

```
=== System Information ===
Hostname: [hostname]
Timestamp: [timestamp]
Uptime: [uptime]

=== CPU Information ===
CPU Model: [model]
Cores: [cores]
Architecture: [architecture]
CPU Usage: [percentage]%

=== Memory Information ===
Total: [total MB]
Used: [used MB]
Free: [free MB]
Memory Usage: [percentage]%

=== Disk Usage ===
Filesystem     Size  Used Avail Use% Mounted on
/dev/sda1      50G   20G   30G  40% /
/dev/sdb1      100G  60G   40G  60% /data

=== Network Interfaces ===
eth0: [state] [IP address]
lo: [state] 127.0.0.1

=== Top Processes ===
PID   USER      %CPU  %MEM  COMMAND
1234  user     5.2   2.1   process1
5678  user     3.1   1.5   process2
```

---

*This is a project placeholder. Complete implementation is performed by the learner.*
