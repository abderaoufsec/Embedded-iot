# Linux Cheat Sheet

Quick reference for Linux commands useful in embedded systems.

## Basic Commands

### File Operations
```bash
ls                    # List directory contents
cd <path>             # Change directory
pwd                   # Print working directory
cp <src> <dst>        # Copy files
mv <src> <dst>        # Move/rename files
rm <file>             # Remove files
mkdir <dir>           # Create directory
rmdir <dir>           # Remove empty directory
rm -r <dir>           # Remove directory and contents
```

### File Viewing
```bash
cat <file>            # Display file contents
less <file>           # View file with pagination
head <file>           # View first lines
tail <file>           # View last lines
tail -f <file>        # Follow file (log monitoring)
```

### System Information
```bash
uname -a              # System information
df -h                 # Disk usage
free -h               # Memory usage
top                   # Process monitor
htop                  # Enhanced process monitor
ps aux                # Process list
```

## Permissions

### Change Permissions
```bash
chmod 755 <file>      # rwxr-xr-x
chmod +x <file>       # Make executable
chmod -x <file>       # Remove execute
```

### Change Owner
```bash
chown user:group <file>
```

## Networking

### Network Commands
```bash
ifconfig              # Network interfaces
ip addr               # Modern network config
ping <host>           # Test connectivity
ssh user@host         # Remote login
scp <src> <dst>       # Secure copy
wget <url>            # Download file
curl <url>            # Download/transfer
```

### Network Debugging
```bash
netstat -tulpn        # Network connections
ss -tulpn             # Modern netstat
nmap <host>           # Port scanner
tcpdump               # Packet capture
```

## Process Management

### Process Control
```bash
<command> &           # Run in background
jobs                  # List background jobs
fg %1                 # Bring to foreground
bg %1                 # Send to background
kill <pid>            # Kill process
kill -9 <pid>         # Force kill
```

### Service Management (systemd)
```bash
systemctl start <service>
systemctl stop <service>
systemctl restart <service>
systemctl status <service>
systemctl enable <service>   # Enable at boot
systemctl disable <service>  # Disable at boot
```

## Text Processing

### Text Manipulation
```bash
grep <pattern> <file>    # Search text
grep -r <pattern> <dir>  # Recursive search
sed 's/old/new/g' <file> # Find and replace
awk '{print $1}' <file>  # Process columns
sort <file>              # Sort lines
uniq <file>              # Remove duplicates
wc -l <file>             # Count lines
```

## Package Management

### Debian/Ubuntu (apt)
```bash
apt update              # Update package list
apt upgrade             # Upgrade packages
apt install <package>   # Install package
apt remove <package>    # Remove package
apt search <term>       # Search packages
```

### Red Hat/CentOS (yum/dnf)
```bash
yum install <package>
yum remove <package>
yum search <term>
```

## Raspberry Pi Specific

### GPIO Access
```bash
gpio readall            # Read all GPIO pins
gpio mode <pin> <mode>  # Set pin mode
gpio write <pin> <val>  # Write to pin
gpio read <pin>         # Read from pin
```

### System Configuration
```bash
raspi-config            # Raspberry Pi configuration
vcgencmd measure_temp   # CPU temperature
```

## Embedded Linux

### Cross-Compilation
```bash
arm-linux-gnueabihf-gcc  # ARM cross-compiler
file <binary>            # Check binary architecture
```

### Device Access
```bash
ls /dev/tty*            # List serial ports
sudo chmod 666 /dev/ttyUSB0  # Allow serial access
```

## Useful Tips

### Command History
```bash
history                 # Command history
!<number>               # Execute history item
!!                      # Last command
!<prefix>               # Last command starting with prefix
```

### Redirection
```bash
command > file          # Redirect output
command >> file         # Append output
command < file          # Redirect input
command 2> file         # Redirect error
command &> file         # Redirect all output
```

### Pipes
```bash
command1 | command2     # Pipe output
```

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 11 - Linux for Embedded.*
