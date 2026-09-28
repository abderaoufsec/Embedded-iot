# Phase 11 — Linux for Embedded

> **Goal:** Develop practical Linux command-line skills and understanding of Linux architecture from an embedded developer's perspective, preparing for embedded Linux development and Raspberry Pi usage.
>
> **Prerequisite:** Phase 10 — MQTT and IoT
>
> **Outcome:** You can navigate Linux systems, manage files and permissions, write Bash scripts, manage processes, use systemd services, compile C programs, and understand embedded Linux architecture concepts.

---

## What You Will Learn

By completing this phase, you will understand:

- **Linux Fundamentals:** Kernel vs distribution, shell vs terminal, CLI vs GUI, Linux distributions
- **Filesystem:** Linux filesystem hierarchy, paths, navigation, file management
- **Text Processing:** grep, pipes, redirection, log filtering, command composition
- **Users and Permissions:** Users, groups, ownership, read/write/execute, chmod, chown, sudo
- **Processes:** Process management, PIDs, signals, foreground/background, system monitoring
- **Package Management:** apt repositories, installing/removing packages, dependencies
- **Shell Scripting:** Bash scripting, variables, control flow, functions, automation
- **Environment Variables:** PATH, HOME, export, configuration management
- **Services and systemd:** Services, daemons, systemd, unit files, journalctl
- **Logging:** Logs, stdout/stderr, journalctl, dmesg, troubleshooting
- **Networking:** Interfaces, IP addresses, routes, DNS, ports, sockets (building on Phase 9)
- **SSH:** Remote shell, authentication, SCP/SFTP, remote management
- **Hardware Concepts:** /dev, device files, block vs character devices, sysfs, procfs
- **Development Environment:** gcc, make, cmake, git, gdb, compilation, debugging
- **Embedded Linux Concepts:** Bootloader, kernel, device tree, root filesystem, cross-compilation, host vs target

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Completed Phase 3 — Digital Electronics
- ✅ Completed Phase 4 — Electronics
- ✅ Completed Phase 5 — Microcontrollers
- ✅ Completed 06 — ESP32
- ✅ Completed Phase 7 — Sensors and Actuators
- ✅ Completed Phase 8 — Embedded Communication
- ✅ Completed Phase 9 — Networking
- ✅ Completed Phase 10 — MQTT and IoT
- ✅ Understanding of networking from Phase 9
- ✅ Understanding of C programming from Phase 2

**Required for labs:**
- Linux system (Ubuntu, Debian, or similar Debian-based distribution recommended)
- VM or dual-boot setup if not using Linux as primary OS
- Internet connectivity for package installation
- SSH access to remote Linux system (optional for SSH lab)

**Recommended:**
- Ubuntu 20.04 LTS or 22.04 LTS (desktop or server)
- Debian 11 or 12
- WSL2 (Windows Subsystem for Linux 2) - Ubuntu

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain Linux architecture (kernel, distribution, shell, terminal)
- Navigate Linux filesystem using command line
- Manage files and directories safely
- Use text processing tools (grep, pipes, redirection)
- Understand and manage users, groups, and permissions
- Manage processes and signals
- Install and manage software packages
- Write basic Bash scripts for automation
- Use environment variables for configuration
- Manage systemd services and inspect logs
- Configure and troubleshoot networking
- Use SSH for remote access and file transfer
- Understand Linux device files (/dev, /sys, /proc)
- Compile C programs on Linux
- Use basic debugging tools
- Explain embedded Linux architecture concepts
- Understand host vs target and cross-compilation concepts

---

## Concepts

### Linux Fundamentals

**What is Linux:**
- Unix-like operating system kernel
- Created by Linus Torvalds in 1991
- Open source and freely available
- Used in servers, desktops, embedded systems, mobile devices

**Kernel vs Operating System:**
- **Kernel:** Core of the operating system, manages hardware (CPU, memory, devices)
- **Operating System:** Kernel + user space tools, libraries, applications
- Linux distributions combine kernel with user space tools

**Linux Distribution:**
- Complete operating system built around Linux kernel
- Includes package manager, default applications, configuration tools
- Examples: Ubuntu, Debian, Fedora, RHEL, Arch Linux
- Distributions differ in package management, default software, configuration

**CLI vs GUI:**
- **CLI (Command Line Interface):** Text-based interface, powerful, scriptable, remote-friendly
- **GUI (Graphical User Interface):** Visual interface, user-friendly, less scriptable
- Embedded systems often use CLI (headless) for resource efficiency

**Terminal:**
- Program that provides CLI access
- Examples: GNOME Terminal, Konsole, xterm, SSH client
- Terminal emulator sends commands to shell

**Shell:**
- Command interpreter that reads and executes commands
- Examples: Bash, Zsh, Fish
- Provides scripting capabilities
- Manages user environment

**Bash (Bourne Again Shell):**
- Default shell on most Linux distributions
- Compatible with POSIX sh
- Rich scripting features
- Most common for embedded Linux

**Filesystem:**
- Hierarchical tree structure starting at root `/`
- Everything is a file (including devices)
- Case-sensitive
- Uses forward slash `/` as separator

**Processes:**
- Running instance of a program
- Has unique Process ID (PID)
- Parent/child process relationships
- Can be foreground or background

**Users:**
- User accounts with permissions
- Root user has full system access
- Regular users have restricted access
- Groups organize users for permission management

**Permissions:**
- Read, write, execute permissions
- Owner, group, others
- Numeric (755, 644) and symbolic (rwxr-xr-x) notation
- `sudo` grants temporary root privileges

**Why This Matters:**
- Linux is the foundation of embedded Linux systems
- Understanding Linux is essential for Raspberry Pi and embedded Linux development
- CLI skills are critical for headless embedded systems
- Permissions and processes are essential for system administration

---

### Linux Filesystem Hierarchy

**Standard Linux Filesystem Hierarchy (FHS):**

**`/` (Root):**
- Top-level directory
- All files and directories start here

**`/bin`:**
- Essential user binaries (programs)
- Common commands: ls, cp, mv, cat, grep

**`/sbin`:**
- System binaries
- Administration commands: fdisk, ifconfig, systemctl

**`/etc`:**
- System configuration files
- Network config, user info, service config

**`/home`:**
- User home directories
- `/home/username` contains user files

**`/root`:**
- Root user's home directory
- System administration files

**`/tmp`:**
- Temporary files
- Cleared on reboot (usually)

**`/var`:**
- Variable data
- Logs, spool files, cache

**`/usr`:**
- User programs and data
- Most installed software

**`/opt`:**
- Optional software
- Third-party applications

**`/dev`:**
- Device files
- Hardware devices as files: `/dev/sda`, `/dev/ttyUSB0`

**`/proc`:**
- Virtual filesystem
- Kernel and process information
- `/proc/cpuinfo`, `/proc/meminfo`

**`/sys`:**
- Virtual filesystem
- Hardware and kernel configuration
- `/sys/class/gpio`, `/sys/class/net`

**`/run`:**
- Runtime data
- Process-specific information

**`/mnt`:**
- Mount points
- External storage mounted here

**Note:** Exact contents can vary by distribution and version.

---

### Paths

**Absolute Path:**
- Full path from root `/`
- Example: `/home/user/documents/report.txt`
- Always starts with `/`

**Relative Path:**
- Path relative to current directory
- Example: `documents/report.txt` (if in `/home/user`)
- Example: `../file.txt` (parent directory)
- Does not start with `/`

**Current Directory:**
- Directory you are currently in
- Displayed with `pwd` command
- Some commands use current directory as default

**Home Directory:**
- User's personal directory
- Usually `/home/username`
- Can be accessed with `~` or `$HOME`

**Hidden Files:**
- Files starting with `.`
- Not shown by default in `ls`
- Configuration files often hidden: `.bashrc`, `.gitconfig`
- Show with `ls -a`

**File Extensions:**
- Not mandatory in Linux
- `.txt`, `.c`, `.sh` are conventions, not requirements
- Executables often have no extension
- File permissions (`chmod +x`) determine executability

---

### Text and File Management

**cat:**
- Display file contents
- `cat file.txt`
- `cat file1.txt file2.txt` (concatenate)

**less:**
- View file contents with pagination
- `less file.txt`
- Navigate with arrow keys, `/` to search, `q` to quit

**head:**
- Display first lines of file
- `head -n 10 file.txt` (first 10 lines)
- Default: first 10 lines

**tail:**
- Display last lines of file
- `tail -n 10 file.txt` (last 10 lines)
- `tail -f file.txt` (follow file as it grows, useful for logs)

**grep:**
- Search for patterns in files
- `grep "pattern" file.txt`
- `grep -r "pattern" directory/` (recursive)
- `grep -i "pattern" file.txt` (case-insensitive)
- `grep -v "pattern" file.txt` (invert match)

**sort:**
- Sort lines alphabetically or numerically
- `sort file.txt`
- `sort -n file.txt` (numeric)
- `sort -u file.txt` (unique)

**uniq:**
- Remove duplicate adjacent lines
- `uniq file.txt`
- Often used with `sort`: `sort file.txt | uniq`

**wc:**
- Word count
- `wc -l file.txt` (line count)
- `wc -w file.txt` (word count)
- `wc -c file.txt` (byte count)

**cut:**
- Extract columns from text
- `cut -d: -f1 file.txt` (colon-delimited, field 1)
- `cut -c1-10 file.txt` (characters 1-10)

**tr:**
- Translate or delete characters
- `tr 'A-Z' 'a-z' file.txt` (convert to lowercase)
- `tr -d '\n' file.txt` (delete newlines)

**diff:**
- Compare files
- `diff file1.txt file2.txt`
- Shows differences line by line

**Redirection:**

**Output Redirection (`>`):**
- Redirect output to file
- `ls > files.txt`
- Overwrites existing file

**Append (`>>`):**
- Append output to file
- `ls >> files.txt`
- Adds to existing file

**Input Redirection (`<`):**
- Read input from file
- `sort < names.txt`

**Error Redirection (`2>`):**
- Redirect error messages
- `command 2> errors.txt`

**Pipes (`|`):**
- Pass output of one command as input to another
- `ls | grep "pattern"`
- `cat file.txt | grep "pattern" | sort`

**Command Composition:**
- Combine commands using pipes and redirection
- `cat file.txt | grep "error" | wc -l` (count error lines)
- `ps aux | grep "process" | sort -k2 -n` (sort by CPU usage)

**Why This Matters:**
- Text processing is essential for log analysis
- Pipes enable powerful command-line workflows
- Scripting automation depends on these tools
- Embedded developers use these for system monitoring

---

### Users and Permissions

**Users:**
- Accounts with username and UID
- Root user (UID 0) has full system access
- Regular users have restricted access
- User information in `/etc/passwd`

**Groups:**
- Collections of users
- Simplify permission management
- Group information in `/etc/group`
- Each user has primary group

**Ownership:**
- Every file has owner and group
- `ls -l` shows ownership
- `user:group file`

**Permissions:**
- Read (r): Read file/list directory
- Write (w): Modify file/create/delete in directory
- Execute (x): Execute file/enter directory
- Apply to owner, group, others

**Numeric Permissions:**
- 755: rwxr-xr-x (owner: rwx, group: r-x, others: r-x)
- 644: rw-r--r-- (owner: rw-, group: r--, others: r--)
- 700: rwx------ (owner: rwx, group: ---, others: ---)
- 600: rw------- (owner: rw-, group: ---, others: ---)

**Symbolic Permissions:**
- `u`: User (owner)
- `g`: Group
- `o`: Others
- `r`: Read
- `w`: Write
- `x`: Execute
- `chmod u+x file` (add execute for owner)
- `chmod go-w file` (remove write for group and others)

**chmod:**
- Change file permissions
- `chmod 755 script.sh` (set executable)
- `chmod +x script.sh` (add execute)
- `chmod -R 644 directory/` (recursive)

**chown:**
- Change file owner
- `chown user file`
- `chown user:group file`

**chgrp:**
- Change file group
- `chgrp group file`

**sudo:**
- Execute command as root
- `sudo apt install package`
- Prompts for password
- Use sparingly for security

**Least Privilege:**
- Grant only necessary permissions
- Use regular user when possible
- Use sudo only when necessary
- Avoid logging in as root for daily use

**Why This Matters:**
- Permissions are critical for security
- Multi-user systems require proper permission management
- Embedded systems often run as non-root for security
- Understanding permissions is essential for system administration

---

### Processes

**Process:**
- Running instance of a program
- Has unique Process ID (PID)
- Has parent process
- Has user and group ownership

**PID (Process ID):**
- Unique number identifying process
- `ps` shows PIDs
- `kill` uses PID to send signals

**Parent/Child Processes:**
- Process can spawn child processes
- Parent waits for child to exit
- Process tree shows hierarchy
- `pstree` shows process tree

**Foreground vs Background:**
- **Foreground:** Runs in terminal, occupies terminal
- **Background:** Runs in background, terminal free
- `command &` runs in background
- `Ctrl+Z` suspends foreground process
- `bg` resumes suspended process in background
- `fg` brings background process to foreground

**Process States:**
- Running: Currently executing
- Sleeping: waiting for event
- Stopped: suspended
- Zombie: terminated but not yet cleaned up

**Signals:**
- Messages sent to processes
- `SIGTERM (15)`: Terminate gracefully
- `SIGKILL (9)`: Terminate immediately (cannot be ignored)
- `SIGHUP (1)`: Hangup (terminal closed)
- `SIGINT (2)`: Interrupt (Ctrl+C)
- `SIGSTOP (19)`: Stop process

**SIGTERM vs SIGKILL:**
- **SIGTERM:** Asks process to terminate gracefully, allows cleanup
- **SIGKILL:** Terminates immediately, no cleanup, dangerous
- **Prefer SIGTERM** for normal termination
- Use SIGKILL only when process is unresponsive

**Commands:**
- `ps`: List processes
- `top`: Interactive process monitor
- `htop`: Interactive process monitor (color-coded)
- `pgrep`: Find processes by name
- `pkill`: Kill processes by name
- `kill`: Send signal to process by PID
- `jobs`: List background jobs
- `bg`: Background a job
- `fg`: Foreground a job
- `nohup`: Run command immune to hangup

**Why This Matters:**
- Process management is essential for system administration
- Understanding signals is critical for graceful shutdown
- Background processes are essential for services
- Resource monitoring helps optimize system performance

---

### Package Management

**Ubuntu/Debian Package Management with apt:**

**Repository:**
- Collection of software packages
- Maintained by distribution
- Contains package metadata and dependencies

**Package:**
- Compiled software with dependencies
- Installed from repository
- Can be updated or removed

**Dependency:**
- Package required by another package
- Package manager resolves dependencies automatically
- Dependency tree can be complex

**Commands:**
- `sudo apt update`: Update package lists
- `sudo apt upgrade`: Upgrade installed packages
- `sudo apt install package`: Install package
- `sudo apt remove package`: Remove package (keep config)
- `sudo apt purge package`: Remove package and config
- `apt search pattern`: Search for packages
- `apt show package`: Show package information

**Package Managers by Distribution:**
- Debian/Ubuntu: apt
- Fedora/RHEL: dnf
- Arch Linux: pacman
- openSUSE: zypper

**Why This Matters:**
- Package management is essential for software installation
- Understanding dependencies prevents conflicts
- Different distributions use different package managers
- Embedded Linux often uses custom package management

---

### Shell Scripting

**Bash Scripting:**
- Bash (Bourne Again Shell) is default shell
- Scripts automate repetitive tasks
- Shebang indicates interpreter

**Shebang:**
- First line of script
- `#!/bin/bash`
- Tells system which interpreter to use

**Variables:**
- `name=value` (no spaces around `=`)
- `$name` or `${name}` to access
- Variables are untyped by default
- Double quotes for string expansion: `echo "$name"`

**Arguments:**
- `$0`: Script name
- `$1`, `$2`, `$3`: Positional arguments
- `$@`: All arguments
- `$#`: Number of arguments

**Exit Status:**
- Command returns exit status (0 = success, non-zero = error)
- `$?`: Exit status of last command
- `exit 0`: Explicitly exit with success
- `exit 1`: Exit with error

**if Statement:**
```bash
if [ condition ]; then
    # commands
elif [ condition ]; then
    # commands
else
    # commands
fi
```

**case Statement:**
```bash
case "$variable" in
    pattern1)
        # commands
        ;;
    pattern2)
        # commands
        ;;
    *)
        # default
        ;;
esac
```

**Loops:**
```bash
# For loop
for i in 1 2 3 4 5; do
    echo $i
done

# While loop
while [ $count -lt 10 ]; do
    echo $count
    count=$((count + 1))
done
```

**Functions:**
```bash
function function_name {
    # commands
    return
}
```

**Command Substitution:**
- `$(command)`: Run command and capture output
- ``command``: Alternative syntax
- `output=$(command)`

**Quoting:**
- Double quotes: Variable expansion, globbing
- Single quotes: Literal text, no expansion
- Backslash: Escape character

**Environment Variables:**
- Variables accessible to processes
- `export`: Make variable available to child processes
- Environment variable names are conventionally uppercase

**Executable Scripts:**
- `chmod +x script.sh`: Make executable
- `./script.sh`: Run script in current directory
- `./` indicates current directory

**Why This Matters:**
- Scripting automates repetitive tasks
- Bash is universal on Linux systems
- Scripting is essential for embedded Linux automation
- Understanding scripting enables custom system tools

---

### Environment Variables

**Environment Variables:**
- Variables passed to processes
- Available to child processes
- Configure program behavior

**Common Environment Variables:**
- `PATH`: Colon-separated list of directories to search for executables
- `HOME`: User's home directory
- `USER`: Current username
- `PWD`: Present working directory
- `SHELL`: Default shell
- `EDITOR`: Default text editor
- `LANG`: Language and locale

**export:**
- Make variable available to child processes
- `export MY_VAR=value`
- Changes persist for current session

**Shell Variables vs Environment Variables:**
- Shell variables: Local to current shell session
- Environment variables: Passed to child processes
- `export` converts shell variable to environment variable

**Why This Matters:**
- Environment variables configure system behavior
- PATH determines which commands are available
- Configuration often done via environment variables
- Understanding environment variables is essential for debugging

---

### Services and systemd

**Service:**
- Background program that runs continuously
- Examples: web server, database, SSH server
- Runs as daemon

**Daemon:**
- Background process with no controlling terminal
- Often starts at boot
- Managed by init system

**systemd:**
- Init system and service manager
- Default on most modern Linux distributions
- Manages services, logging, dependencies
- Replaces older init systems (SysVinit, Upstart)

**Unit:**
- Configuration file for systemd
- Service unit (`.service` file)
- Defines service behavior

**Service Unit:**
- `[Unit]` section: Metadata (description, dependencies)
- `[Service]` section: Service configuration (command, user, environment)
- `[Install]` section: Install behavior (when to start)

**Commands:**
- `systemctl status service`: Check service status
- `systemctl start service`: Start service
- `systemctl stop service`: Stop service
- `systemctl restart service`: Restart service
- `systemctl enable service`: Enable at boot
- `systemctl disable service`: Disable at boot
- `systemctl status`: Show system status

**journalctl:**
- View systemd logs
- `journalctl -u service`: View logs for specific service
- `journalctl -f`: Follow logs in real-time
- `journalctl -k`: View kernel logs

**Not Universal:**
- systemd is common but not universal
- Some systems use SysVinit, OpenRC, runit
- Embedded Linux may use custom init systems

**Why This Matters:**
- Services are essential for system functionality
- systemd is the modern standard for service management
- Understanding services is critical for system administration
- Logs are essential for troubleshooting

---

### Logging

**Logs:**
- Records of system events
- Essential for troubleshooting
- Stored in various locations

**stdout/stderr:**
- Standard output and standard error
- Programs write to these streams
- Can be redirected to files

**Log Files:**
- `/var/log/`: System log directory
- `/var/log/syslog`: System log
- `/var/log/auth.log`: Authentication log
- Application logs in `/var/log/` or application-specific locations

**journalctl:**
- View systemd journal logs
- `journalctl -u service`: Service-specific logs
- `journalctl -f`: Follow logs in real-time
- `journalctl -k`: Kernel logs

**dmesg:**
- Kernel ring buffer messages
- Hardware events, driver messages
- Boot messages
- `dmesg | tail`: Recent kernel messages
- May require root access

**Log Rotation:**
- Logs grow over time
- System rotates logs to prevent disk space exhaustion
- Old logs compressed or deleted
- Configuration in `/etc/logrotate.conf`

**Troubleshooting through Logs:**
- Identify time of issue
- Check relevant service logs
- Search for error messages
- Check for warnings that preceded failure
- Correlate multiple log sources

**Why This Matters:**
- Logs are primary troubleshooting tool
- Understanding logs is essential for system administration
- Embedded systems rely on logs for debugging
- Log rotation prevents disk exhaustion

---

### Networking for Embedded Linux

**Building on Phase 9:**

**Network Interfaces:**
- Physical and virtual interfaces
- Ethernet: `eth0`, `ens33`, `enp0s3`
- Wi-Fi: `wlan0`, `wlp3s0`
- Loopback: `lo`

**IP Addresses:**
- IPv4 and IPv6 addresses
- Addresses assigned to interfaces
- Can be static or dynamic (DHCP)

**MAC Addresses:**
- Hardware addresses
- Assigned to network interfaces
- Used for layer 2 addressing

**Routes:**
- Kernel routing table
- Default route (gateway)
- Static routes

**DNS:**
- Domain name resolution
- DNS servers in `/etc/resolv.conf`
- `resolvectl` query tool

**Ports:**
- Application-specific endpoints
- 0-1023: Well-known ports
- 1024-65535: Registered ports
- 65536-65535: Dynamic/private ports

**Sockets:**
- IP address + port = socket
- TCP sockets (connection-oriented)
- UDP sockets (connectionless)
- Applications bind to sockets

**Commands:**
- `ip addr`: Show IP addresses
- `ip link`: Show network interfaces
- `ip route`: Show routing table
- `ping`: Test connectivity
- `ss`: Socket statistics
- `hostname`: Show or set hostname
- `hostnamectl`: System hostname configuration
- `resolvectl`: DNS management

**Why This Matters:**
- Networking is essential for IoT systems
- Understanding network configuration is critical
- Embedded Linux devices often need network troubleshooting
- Building on Phase 9 networking knowledge

---

### SSH

**SSH (Secure Shell):**
- Protocol for secure remote access
- Encrypted communication
- Replaces insecure telnet/rlogin

**Client/Server Model:**
- SSH client connects to SSH server
- Server authenticates client
- Encrypted channel established
- Remote shell session started

**Remote Shell:**
- Access remote system via SSH
- Execute commands on remote system
- As if physically present at remote console

**Host/IP/Port:**
- Connect to host by IP or hostname
- Default port: 22
- Can specify different port: `ssh -p 2222 user@host`

**Authentication:**
- Password authentication
- SSH key authentication (more secure)
- Known hosts verification
- `/etc/known_hosts` stores trusted host keys

**SSH Keys:**
- Public/private key pair
- `ssh-keygen`: Generate keys
- `ssh-copy-id`: Copy public key to remote
- Private key must be kept secret
- Public key placed in `~/.ssh/authorized_keys` on remote

**known_hosts:**
- Stores fingerprints of remote hosts
- Prevents man-in-the-middle attacks
- `~/.ssh/known_hosts`
- Warning on first connection to new host

**SCP (Secure Copy):**
- Copy files over SSH
- `scp local_file user@host:remote_path`
- `scp user@host:remote_path local_file`
- `scp -r directory/ user@host:remote_path` (recursive)

**SFTP (SSH File Transfer Protocol):**
- Interactive file transfer over SSH
- Like FTP but encrypted
- `sftp user@host`

**Why This Matters:**
- SSH is essential for remote management
- Headless embedded systems require SSH
- SSH is secure (unlike telnet)
- SSH enables remote file transfer

---

### Hardware / Device Concepts

**/dev:**
- Directory containing device files
- Hardware exposed as files
- Access hardware by reading/writing device files

**Device Files:**
- Block devices: `/dev/sda` (entire disk), `/dev/sda1` (partition)
- Character devices: `/dev/ttyUSB0` (serial port), `/dev/random` (random number generator)
- `ls -l /dev` shows device types (b for block, c for character)

**Block vs Character Devices:**
- **Block devices:** Random access by block, storage devices (disks, SSDs)
- **Character devices:** Sequential access, communication devices (serial ports, terminals)

**USB Devices:**
- USB devices appear in `/dev/`
- USB serial: `/dev/ttyUSB0`, `/dev/ttyACM0`
- USB storage: `/dev/sdb`, `/dev/sdc`

**Serial Devices:**
- UART/USB serial adapters
- `/dev/ttyS0`, `/dev/ttyUSB0`
- Used for embedded communication
- Permissions restrict access

**Permissions on Devices:**
- Device files have permissions like regular files
- `/dev/ttyUSB0` often restricted to `dialout` group
- User must be in appropriate group to access device
- `sudo` often required for device access

**sysfs:**
- Virtual filesystem in `/sys`
- Kernel and hardware configuration exposed
- `/sys/class/`, `/sys/devices/`
- Used for configuring hardware dynamically

**/proc:**
- Virtual filesystem in `/proc`
- Kernel and process information
- `/proc/cpuinfo`, `/proc/meminfo`, `/proc/[pid]/`
- Text-based, human-readable

**Why This Matters:**
- Linux exposes hardware through device files
- Understanding /dev is essential for hardware access
- sysfs and procfs enable runtime configuration
- Embedded Linux relies on these interfaces

---

### Compilation and Development

**gcc:**
- GNU C compiler
- `gcc -o program program.c`
- Compiler warnings indicate potential issues
- `-Wall`: Enable all warnings

**g++:**
- GNU C++ compiler
- Similar to gcc but for C++

**make:**
- Build automation tool
- Reads Makefile
- Compiles project based on dependencies
- `make`, `make clean`

**cmake:**
- Build system generator
- Generates Makefiles from configuration
- Cross-platform build configuration
- `cmake .`, `make`

**git:**
- Version control system
- Already covered in curriculum
- Used for code management

**gdb:**
- GNU Debugger
- Debugging compiled programs
- Breakpoints, stepping, inspecting variables
- `gdb program`, `gdb program core`

**Compiling C Program:**
```bash
gcc -Wall -o program program.c
./program
```

**Executable Permissions:**
- Compiled files need execute permission
- `chmod +x program`
- Or compile with `gcc -o program program.c` (sets execute permission)

**Compiler Warnings:**
- Warnings indicate potential issues
- Address warnings before warnings become errors
- `-Wall` enables comprehensive warnings

**Basic Debugging:**
- Use `gdb` to debug compiled programs
- Set breakpoints to pause execution
- Step through code line by line
- Inspect variable values

**Why This Matters:**
- C compilation is fundamental for embedded development
- Understanding compilation process is essential
- Debugging is essential for development
- Build automation (make, cmake) is essential for projects

---

### Embedded Linux Concepts

**Bootloader:**
- First program that runs on power-on
- Initializes hardware
- Loads kernel into memory
- Examples: U-Boot, GRUB, vendor bootloaders

**Kernel:**
- Core of operating system
- Manages hardware, processes, memory
- Provides system calls to user space
- Embedded kernels may be customized

**Device Tree:**
- Data structure describing hardware
- Used by kernel to identify hardware
- Defines peripherals, memory map, interrupts
- Device tree blob passed to kernel at boot

**Root Filesystem:**
- Filesystem mounted at `/` at boot
- Contains essential system files
- Can be initramfs (initial RAM filesystem) or partition

**Init System:**
- First user-space process (PID 1)
- Starts other services
- Examples: systemd, SysVinit, busybox init
- Embedded systems may use minimal init

**Cross-Compilation:**
- Compiling for different architecture
- Compile on x86 for ARM target
- Requires cross-compiler toolchain
- Includes cross-compiler, libraries, tools

**Toolchain:**
- Collection of tools for building software
- Compiler, linker, assembler, debugger
- Native toolchain for host architecture
- Cross-compiler for target architecture

**Host vs Target:**
- **Host:** Machine doing compilation
- **Target:** Machine where software runs
- Native compilation: Host = Target
- Cross-compilation: Host ≠ Target

**Architecture Differences:**
- x86: Intel/AMD (desktop, server)
- ARM: Most embedded (Raspberry Pi, STM32, ESP32 has Xtensa)
- RISC-V: Emerging embedded architecture
- PowerPC: Some embedded systems

**Headless Systems:**
- No display, keyboard, mouse
- Managed remotely via SSH
- Common for embedded Linux
- CLI-only interface

**Yocto/Buildroot:**
- Build systems for custom Linux distributions
- Include bootloader, kernel, root filesystem
- Used for custom embedded Linux images
- Advanced topic (not covered in this phase)

**Why This Matters:**
- Understanding boot process is essential for embedded Linux
- Cross-compilation is required for embedded development
- Architecture differences affect compilation
- Headless systems require remote management
- Custom Linux requires advanced build systems

---

## Exact Resources

### Resource 1: GNU Bash Manual
- **Provider:** GNU Project (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Bash shell documentation
- **URL:** https://www.gnu.org/software/bash/manual/

### Resource 2: GNU Coreutils
- **Provider:** GNU Project (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Core Linux utilities documentation
- **URL:** https://www.gnu.org/software/coreutils/manual/

### Resource 3: Linux Man Pages
- **Provider:** Linux Kernel Organization (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Linux command documentation
- **URL:** https://man7.org/linux/man-pages/

### Resource 4: Ubuntu Documentation
- **Provider:** Canonical (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Ubuntu Linux documentation
- **URL:** https://ubuntu.com/server/docs/

### Resource 5: Debian Documentation
- **Provider:** Debian Project (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Debian Linux documentation
- **URL:** https://www.debian.org/doc/

### Resource 6: systemd Documentation
- **Provider:** freedesktop.org (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** systemd and journalctl documentation
- **URL:** https://www.freedesktop.org/software/systemd/man/

### Resource 7: OpenSSH Documentation
- **Provider:** OpenBSD Project (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** SSH, SCP, SFTP documentation
- **URL:** https://www.openssh.com/manual/

### Resource 8: GCC Documentation
- **Provider:** GNU Project (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** GCC compiler documentation
- **URL:** https://gcc.gnu.org/onlinedocs/

### Resource 9: GDB Documentation
- **Provider:** GNU Project (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** GDB debugger documentation
- **URL:** https://sourceware.org/gdb/documentation/

### Resource 10: Make Documentation
- **Provider:** GNU Project (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Make build automation documentation
- **URL:** https://www.gnu.org/software/make/manual/

---

## Study Order

Follow this exact sequence:

1. **Study Linux fundamentals** (kernel, distribution, shell, terminal, CLI vs GUI)
2. **Understand filesystem hierarchy** (FHS, paths, navigation)
3. **Study text processing** (grep, pipes, redirection, command composition)
4. **Study users and permissions** (users, groups, ownership, chmod, chown, sudo)
5. **Study processes** (PID, signals, foreground/background, monitoring)
6. **Study package management** (apt, repositories, dependencies)
7. **Study Bash scripting** (variables, control flow, functions, automation)
8. **Study environment variables** (PATH, HOME, export, configuration)
9. **Study services and systemd** (services, daemons, unit files, journalctl)
10. **Study logging** (logs, journalctl, dmesg, troubleshooting)
11. **Study networking** (interfaces, IP, routes, DNS, ports, sockets)
12. **Study SSH** (remote shell, authentication, keys, SCP)
13. **Study hardware concepts** (/dev, device files, sysfs, procfs)
14. **Study development environment** (gcc, make, cmake, git, gdb)
15. **Study embedded Linux concepts** (bootloader, kernel, device tree, cross-compilation)
16. **Complete all exercises**
17. **Complete all labs**
18. **Complete the project**
19. **Take the knowledge test**
20. **Take the practical test**
21. **Review completion checklist**

---

## Exercises

### Exercise 1: Linux Architecture

**Objective:** Understand Linux architecture components.

**Tasks:**
1. What is the difference between Linux kernel and Linux distribution?
2. What is the difference between shell and terminal?
3. What is the difference between CLI and GUI?
4. Why is CLI preferred for embedded systems?
5. What is the role of package manager?

**Expected Outcome:** You understand Linux architecture and layers.

### Exercise 2: Filesystem Navigation

**Objective:** Practice filesystem navigation.

**Tasks:**
1. What is the difference between absolute and relative paths?
2. What is the current directory?
3. What is the home directory?
4. How do you create a directory? Remove a directory?
5. What command shows disk usage?

**Expected Outcome:** You can navigate Linux filesystem comfortably.

### Exercise 3: Permissions

**Objective:** Understand Linux permissions.

**Tasks:**
1. What does 755 mean in symbolic notation?
2. What does 644 mean in symbolic notation?
3. What is the difference between chmod and chown?
4. When should you use sudo?
5. What is the principle of least privilege?

**Expected Outcome:** You understand permissions and security.

### Exercise 4: Process Management

**Objective:** Understand process management.

**Tasks:**
1. What is a PID?
2. What is the difference between SIGTERM and SIGKILL?
3. Why is SIGTERM preferred over SIGKILL?
4. What is the difference between foreground and background?
5. How do you suspend and resume a process?

**Expected Outcome:** You understand process management and signals.

### Exercise 5: Shell Pipelines

**Objective:** Understand command composition.

**Tasks:**
1. What does `|` do?
2. What does `>` do?
3. What does `>>` do?
4. What does `2>` do?
5. How would you count lines containing "error" in a log file?

**Expected Outcome:** You can compose commands using pipes and redirection.

### Exercise 6: Bash Scripting

**Objective:** Understand Bash scripting basics.

**Tasks:**
1. What is a shebang?
2. How do you access script arguments?
3. What is `$0`, `$1`, `$@`?
4. What is the difference between `=` and `==` in Bash?
5. How do you make a script executable?

**Expected Outcome:** You understand Bash scripting fundamentals.

### Exercise 7: Networking Commands

**Objective:** Understand Linux networking commands.

**Tasks:**
1. What does `ip addr` show?
2. What does `ip route` show?
3. What is the difference between ping and traceroute?
4. What does `ss` show?
5. How do you check DNS resolution?

**Expected Outcome:** You can use Linux networking commands.

### Exercise 8: SSH

**Objective:** Understand SSH fundamentals.

**Tasks:**
1. What is the difference between password and key authentication?
2. What is known_hosts?
3. What is the difference between SSH and telnet?
4. How do you copy a file using SCP?
5. Why is SSH important for embedded systems?

**Expected Outcome:** You understand SSH and remote access.

### Exercise 9: systemd

**Objective:** Understand systemd basics.

**Tasks:**
1. What is the difference between service and daemon?
2. What is a unit file?
3. What does `systemctl enable` do?
4. What does journalctl do?
5. How do you view service logs?

**Expected Outcome:** You understand systemd and service management.

### Exercise 10: Embedded Linux Architecture

**Objective:** Understand embedded Linux concepts.

**Tasks:**
1. What is the role of bootloader?
2. What is the device tree?
3. What is the root filesystem?
4. What is cross-compilation?
5. What is the difference between host and target?

**Expected Outcome:** You understand embedded Linux architecture concepts.

---

## Labs

### Lab 1: Linux CLI Fundamentals

**Objective:** Navigate Linux filesystem and manage files.

**Prerequisites:**
- Linux system access
- Basic understanding of terminal

**Components:**
- Linux system
- Terminal

**Theory:**
- Absolute vs relative paths
- Current directory, home directory
- File creation, copying, moving, deletion

**Procedure:**

**Navigate Filesystem:**
```bash
pwd                    # Show current directory
cd /                  # Go to root
ls                     # List root directory
cd /home               # Go to home
ls -la                 # Detailed listing
```

**Create and Manage Files:**
```bash
cd /tmp                  # Use /tmp for testing
mkdir linux-lab          # Create directory
cd linux-lab
touch file1.txt         # Create empty file
echo "Hello Linux" > file1.txt
cat file1.txt
cp file1.txt file2.txt
mv file2.txt file3.txt
rm file1.txt
cd ..
rmdir linux-lab          # Remove directory
```

**Inspect Files:**
```bash
ls -l /etc/passwd | head
ls -l /etc/group | head
file /bin/ls
```

**Expected Behavior:**
- Commands execute successfully
- Files created, copied, moved, deleted
- Directory created and removed
- File permissions displayed

**Troubleshooting:**
- Permission denied: Use sudo or appropriate permissions
- Command not found: Check PATH, install package
- No such file or directory: Check path

**Cleanup:**
```bash
# /tmp automatically cleaned on reboot
# No manual cleanup needed
```

**Completion Criteria:**
- Can navigate filesystem
- Can create, copy, move, delete files
- Can inspect file metadata
- Understand paths

---

### Lab 2: Filesystem Investigation

**Objective:** Explore Linux filesystem hierarchy.

**Prerequisites:**
- Completed Lab 1
- Linux system access

**Components:**
- Linux system
- Terminal

**Theory:**
- Filesystem hierarchy (FHS)
- Virtual filesystems (/proc, /sys, /dev)
- Configuration directories (/etc, /var)

**Procedure:**

**Explore Essential Directories:**
```bash
ls /                     # Root directory
ls /bin                  # User binaries
ls /sbin                 # System binaries
ls /etc                  # Configuration
ls /home                 # User home directories
ls /tmp                  # Temporary files
ls /var                  # Variable data
ls /usr                  # User programs
ls /opt                  # Optional software
```

**Explore Virtual Filesystems:**
```bash
ls /dev                  # Device files
ls /proc                 # Process information
cat /proc/cpuinfo       # CPU information
cat /proc/meminfo       # Memory information
ls /sys/class/net        # Network devices
```

**Inspect Configuration:**
```bash
cat /etc/os-release      # OS information
cat /etc/hostname        # Hostname
cat /etc/passwd | head    # User accounts
cat /etc/group | head     # Groups
```

**Expected Behavior:**
- Can explore directory structure
- Can inspect system information via /proc and /sys
- Can view configuration files

**Document:**
- Interesting directories found
- System information gathered
- Configuration files inspected

**Completion Criteria:**
- Understand filesystem hierarchy
- Can locate system information
- Can access /proc and /sys

---

### Lab 3: Text Processing

**Objective:** Use grep, pipes, and redirection for log analysis.

**Prerequisites:**
- Completed Lab 1
- Linux system access

**Components:**
- Linux system
- Terminal

**Theory:**
- Pattern matching with grep
- Pipes for command composition
- Redirection for output

**Procedure:**

**Grep Search:**
```bash
grep "root" /etc/passwd     # Find root user
grep -i "error" /var/log/syslog | head  # Find errors (case-insensitive)
grep -r "network" /etc/    # Search for network in /etc
```

**Pipes:**
```bash
ps aux | grep "systemd"  # Find systemd process
ps aux | grep "bash" | wc -l  # Count bash processes
```

**Redirection:**
```bash
ls > files.txt           # Save directory listing
ps aux > processes.txt    # Save process list
grep "ssh" /var/log/auth.log > ssh.log  # Save SSH log entries
```

**Combined Example:**
```bash
# Find high CPU processes
ps aux | awk '{print $11}' | grep -v "0.0" | sort -rn | head
```

**Expected Behavior:**
- Grep finds patterns
- Pipes enable command composition
- Redirection saves output to files

**Document:**
- Grep patterns tested
- Pipe examples
- Redirection examples

**Completion Criteria:**
- Can use grep effectively
- Can compose commands with pipes
- Can redirect output

---

### Lab 4: Users and Permissions

**Objective:** Understand and manage users and permissions.

**Prerequisites:**
- Completed Lab 1
- Linux system with sudo access

**Components:**
- Linux system
- Terminal

**Theory:**
- User accounts and groups
- Numeric vs symbolic permissions
- chmod, chown, chgrp

**Procedure:**

**Inspect Users and Groups:**
```bash
whoami                 # Current user
id                     # User and group IDs
groups                 # User groups
cat /etc/passwd | head    # All users
cat /etc/group | head     # All groups
```

**Create Test File:**
```bash
cd /tmp
touch testfile.txt
ls -l testfile.txt
```

**Change Permissions:**
```bash
chmod 644 testfile.txt     # rw-r--r--
chmod 755 testfile.txt     # rwxr-xr-x
chmod +x testfile.txt     # Add execute
chmod -x testfile.txt     # Remove execute
```

**Change Ownership:**
```bash
sudo chown $USER testfile.txt  # Change owner (if allowed)
sudo chgrp $USER testfile.txt  # Change group (if allowed)
```

**Clean Up:**
```bash
rm testfile.txt
cd /
```

**Expected Behavior:**
- Permissions changed successfully
- Ownership changes (if allowed)
- No modification to system files

**Troubleshooting:**
- Permission denied: Use sudo or appropriate permissions
- Operation not permitted: Check user/group membership

**Completion Criteria:**
- Understand numeric and symbolic permissions
- Can change file permissions
- Understand ownership
- Use sudo appropriately

---

### Lab 5: Process Management

**Objective:** Manage processes and signals.

**Prerequisites:**
- Completed Lab 1
- Linux system access

**Components:**
- Linux system
- Terminal

**Theory:**
- PIDs, parent/child processes
- Signals (SIGTERM, SIGKILL, SIGHUP, SIGINT)
- Foreground vs background

**Procedure:**

**Inspect Processes:**
```bash
ps aux | head            # List all processes
ps aux | grep "bash"     # Find bash processes
top                     # Interactive monitor (q to quit)
```

**Background Process:**
```bash
sleep 60 &               # Sleep in background
jobs                     # Show background jobs
fg %1                   # Bring job 1 to foreground
```

**Signals:**
```bash
# Test signals with sleep
sleep 60 &
PID=$!
kill -15 $PID            # SIGTERM (graceful)
```

**Process Monitoring:**
```bash
htop                    # Interactive monitor (if available)
ps aux --sort=-%cpu | head  # Sort by CPU usage
```

**Clean Up:**
```bash
# Background sleep process should have terminated
```

**Expected Behavior:**
- Can list and monitor processes
- Can run processes in background
- Can send signals to processes
- Can monitor resource usage

**Troubleshooting:**
- Permission denied: Use sudo
- Process not found: Check PID
- Signal failed: Process may not accept signal

**Completion Criteria:**
- Understand process monitoring
- Can manage background processes
- Understand signals
- Can use system monitoring tools

---

### Lab 6: Package Management

**Objective:** Install and manage software packages.

**Prerequisites:**
- Completed Lab 1
- Linux system with internet access
- sudo access

**Components:**
- Linux system
- Internet connection

**Theory:**
- Repositories and packages
- Dependencies
- Package management

**Procedure:**

**Update Package Lists:**
```bash
sudo apt update
```

**Upgrade Packages:**
```bash
sudo apt upgrade
```

**Search for Package:**
```bash
apt search htop
```

**Install Package:**
```bash
sudo apt install htop
```

**Inspect Package:**
```bash
apt show htop
```

**Remove Package:**
```bash
sudo apt remove htop    # Remove package, keep config
sudo apt purge htop     # Remove package and config
```

**Clean Up:**
```bash
sudo apt autoremove
```

**Expected Behavior:**
- Package lists updated
- Package installed successfully
- Package removed successfully
- Dependencies handled automatically

**Troubleshooting:**
- E: Package not found: Check package name, update repositories
- E: Unable to locate package: Check repository configuration
- Permission denied: Use sudo

**Completion Criteria:**
- Can search for packages
- Can install packages
- Can remove packages
- Understand dependencies

---

### Lab 7: Bash Automation

**Objective:** Write a system information script.

**Prerequisites:**
- Completed Lab 1
- Understanding of Bash basics

**Components:**
- Linux system
- Terminal

**Theory:**
- Shebang, variables, echo, command substitution
- Conditional logic

**Procedure:**
```bash
cd /tmp
nano system_info.sh
```

**Script Content:**
```bash
#!/bin/bash

echo "=== System Information ==="
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime -p)"
echo ""
echo "=== CPU Information ==="
lscpu | head -20
echo ""
echo "=== Memory Information ==="
free -h
echo ""
echo "=== Disk Usage ==="
df -h
echo ""
echo "=== Network Interfaces ==="
ip addr show
echo ""
echo "=== Running Processes ==="
ps aux | head -10
```

**Make Executable:**
```bash
chmod +x system_info.sh
./system_info.sh
```

**Test:**
```bash
./system_info.sh > system_report.txt
cat system_report.txt
```

**Clean Up:**
```bash
rm system_info.sh system_report.txt
cd /
```

**Expected Behavior:**
- Script runs without errors
- Output displays system information
- Script saves report to file

**Document:**
- Script content
- Output results

**Completion Criteria:**
- Can write Bash script
- Can make script executable
- Can use command substitution
- Can redirect output

---

### Lab 8: Network Diagnostics

**Objective:** Configure and troubleshoot networking.

**Prerequisites:**
- Completed Lab 1
- Linux system with network connectivity

**Components:**
- Linux system
- Network connection

**Theory:**
- Interfaces, IP addresses, routes, DNS
- Building on Phase 9 networking

**Procedure:**

**Inspect Interfaces:**
```bash
ip addr show
ip link show
```

**Inspect Routing:**
```bash
ip route show
```

**Test Connectivity:**
```bash
ping -c 4 8.8.8.8          # Test internet connectivity
ping -c 4 192.168.1.1      # Test local gateway
```

**Check DNS:**
```bash
resolvectl status
resolvectl query google.com
```

**Inspect Sockets:**
```bash
ss -t listening          # Listening TCP sockets
ss -u                   # UDP sockets
```

**Check Hostname:**
```bash
hostname
hostnamectl status
```

**Expected Behavior:**
- Network interfaces displayed
- Routing table displayed
- Connectivity tested
- DNS resolution tested
- Listening sockets displayed

**Document:**
- Network configuration
- Connectivity test results
- DNS resolution results

**Troubleshooting:**
- Network unreachable: Check physical connection, router
- DNS failure: Check DNS configuration
- Permission denied: Use sudo for some commands

**Completion Criteria:**
- Can inspect network configuration
- Can test connectivity
- Can troubleshoot basic network issues

---

### Lab 9: SSH

**Objective:** Use SSH for remote access and file transfer.

**Prerequisites:**
- Completed Lab 1
- Two Linux systems or VMs
- Network connectivity between systems

**Components:**
- Two Linux systems (client and server)
- Network connection

**Theory:**
- SSH client/server model
- Authentication (password or key)
- SCP for file transfer

**Procedure:**

**SSH Connection:**
```bash
ssh user@remote_host
# Enter password when prompted
```

**Execute Remote Command:**
```bash
ssh user@remote_host "hostname"
ssh user@remote_host "ls -l /tmp"
```

**SCP File Transfer:**
```bash
# Local to remote
scp local_file.txt user@remote_host:/remote/path/

# Remote to local
scp user@remote_host:/remote/file.txt .
```

**SCP Directory:**
```bash
scp -r local_dir/ user@remote_host:/remote/path/
```

**Exit SSH:**
```bash
exit
```

**Expected Behavior:**
- SSH connection established
- Remote commands execute
- Files transferred successfully

**Document:**
- Connection details
- Commands executed
- Files transferred

**Troubleshooting:**
- Connection refused: Check SSH service, firewall
- Permission denied: Check user permissions
- Host key verification: Known hosts issue

**Completion Criteria:**
- Can establish SSH connection
- Can execute remote commands
- Can transfer files with SCP
- Understand SSH authentication

---

### Lab 10: systemd Service

**Objective:** Create and manage a simple systemd service.

**Prerequisites:**
- Completed Lab 1
- Linux system with systemd
- sudo access

**Components:**
- Linux system
- systemd

**Theory:**
- Service vs daemon
- Unit files
- Enable/disable/start/stop/status

**Procedure:**

**Inspect Services:**
```bash
systemctl list-units --type=service
systemctl status ssh
systemctl status cron
```

**Create Simple Service:**
```bash
sudo nano /etc/systemd/system/test-service.service
```

**Unit File Content:**
```ini
[Unit]
Description=Test Service
After=network.target

[Service]
Type=simple
ExecStart=/bin/echo "Test service started"
ExecStop=/bin/echo "Test service stopped"
Restart=always

[Install]
WantedBy=multi-user.target
```

**Reload systemd:**
```bash
sudo systemctl daemon-reload
```

**Manage Service:**
```bash
sudo systemctl start test-service
sudo systemctl status test-service
sudo systemctl stop test-service
sudo systemctl enable test-service
sudo systemctl disable test-service
```

**View Logs:**
```bash
journalctl -u test-service
journalctl -u test-service -f
```

**Clean Up:**
```bash
sudo systemctl disable test-service
sudo rm /etc/systemd/system/test-service.service
sudo systemctl daemon-reload
```

**Expected Behavior:**
- Service created successfully
- Service starts/stops correctly
- Logs are viewable
- Service clean up successful

**Troubleshooting:**
- Failed to start: Check ExecStart path and permissions
- Permission denied: Check unit file permissions
- Service not found: Reload systemd daemon

**Completion Criteria:**
- Understand systemd unit files
- Can create simple service
- Can manage services
- Can view service logs

---

### Lab 11: C Development on Linux

**Objective:** Compile and debug a C program on Linux.

**Prerequisites:**
- Completed Lab 1
- Understanding of C from Phase 2
- Linux system

**Components:**
- Linux system
- gcc compiler

**Theory:**
- Compilation process (preprocessing, compilation, assembly, linking)
- Executable permissions
- Basic debugging

**Procedure:**

**Create C Program:**
```bash
cd /tmp
nano hello.c
```

**C Code:**
```c
#include <stdio.h>

int main() {
    printf("Hello, Linux!\n");
    return 0;
}
```

**Compile:**
```bash
gcc -Wall -o hello hello.c
```

**Run:**
```bash
./hello
```

**Create Program with Arguments:**
```bash
nano args.c
```

**C Code:**
```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Program: %s\n", argv[0]);
    printf("Arguments: %d\n", argc - 1);
    for (int i = 1; i < argc; i++) {
        printf("Arg %d: %s\n", i, argv[i]);
    }
    return 0;
}
```

**Compile and Test:**
```bash
gcc -Wall -o args args.c
./args arg1 arg2 arg3
```

**Debugging with gdb:**
```bash
gcc -g -o hello hello.c
gdb ./hello
(gdb) break main
(gdb) run
(gdb) next
(gdb) quit
```

**Clean Up:**
```bash
rm hello hello.c args args.c
cd /
```

**Expected Behavior:**
- C program compiles without errors
- Program runs correctly
- Arguments parsed correctly
- gdb can set breakpoints and step through code

**Document:**
- Compilation output
- Program output
- gdb experience

**Troubleshooting:**
- Command not found: Install build-essential: `sudo apt install build-essential`
- Permission denied: No sudo for write locations
- Compilation errors: Check code and compiler warnings

**Completion Criteria:**
- Can compile C programs
- Can run C programs
- Can handle command-line arguments
- Can use basic gdb

---

### Lab 12: Embedded Linux Exploration

**Objective:** Explore embedded Linux hardware/software interfaces.

**Prerequisites:**
- Completed Lab 2
- Linux system

**Components:**
- Linux system
- Hardware (if available)

**Theory:**
- Device files (/dev)
- sysfs (/sys)
- procfs (/proc)
- Hardware information

**Procedure:**

**Explore /dev:**
```bash
ls -la /dev
ls /dev/tty*    # Serial devices
ls /dev/sd*    # Block devices
```

**Explore /sys:**
```bash
ls /sys/class
ls /sys/class/net
ls /sys/class/gpio
```

**Explore /proc:**
```bash
cat /proc/cpuinfo
cat /proc/meminfo
cat /proc/devices
```

**Check Hardware:**
```bash
lspci | head -20
lsusb
```

**Identify Information:**
- CPU model, cores, architecture
- Memory size
- Network interfaces
- Available sensors (if supported)

**Document:**
- CPU information
- Memory information
- Network interfaces
- Available hardware

**Expected Behavior:**
- Can access /dev, /sys, /proc
- Can identify system hardware
- Can identify CPU architecture

**Troubleshooting:**
- Permission denied: Use sudo for some directories
- File not found: Device not present on system

**Completion Criteria:**
- Understand /dev, /sys, /proc
- Can identify system hardware
- Understand embedded Linux interfaces

---

## Projects

### Project: Linux System Monitor

**Objective:** Create a command-line tool that reports system information.

**Requirements:**
- Hostname
- Uptime
- CPU information
- Memory usage
- Disk usage
- Network interface information
- Process information
- Timestamp

**Implementation Options:**
- Bash script (recommended for Phase 11)
- C program (optional extension)

**Suggested Features:**
- Color-coded output
- Alert thresholds (CPU > 80%, memory > 90%, disk > 90%)
- Process filtering options
- Configuration file support

**Deliverables:**
- Working script or program
- Configuration documentation
- Usage documentation
- Testing documentation

**Time Estimate:** 4-6 hours

**Project Structure:**
```
linux-system-monitor/
├── README.md
├── src/
│   ├── monitor.sh (Bash script)
│   └── monitor.c (optional C version)
├── config/
│   └── config.conf
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project teaches Linux system monitoring and automation, preparing for embedded Linux system management.

---

## Common Mistakes

### Mistake 1: Not Understanding Absolute vs Relative Paths
**Problem:** Using wrong path causes command failures
**Consequence:** Commands fail, frustration
**Solution:** Always check current directory with `pwd`, use absolute paths when unsure

### Mistake 2: Using rm -rf Incorrectly
**Problem:** Deleting wrong files or directories
**Consequence:** Data loss, system damage
**Solution:** Always verify path before executing, use `rm -i` for confirmation

### Mistake 3: Ignoring Permissions
**Problem:** Command fails due to wrong permissions
**Consequence:** Operations fail unexpectedly
**Solution:** Check with `ls -l`, use `sudo` when appropriate

### Mistake 4: Using rm -rf on System Directories
**Problem:** Deleting critical system files
**Consequence:** System damage
**Solution:** Never use `rm -rf` on `/`, `/etc`, `/usr`, `/bin`, `/sbin`, `/var`, `/sys`, `/proc`

### Mistake 5: Not Using sudo When Required
**Problem:** Command fails due to insufficient permissions
**Consequence:** Cannot perform system administration
**Solution:** Use `sudo` for system administration tasks

### Mistake 6: Editing System Configuration Without Backup
**Problem:** Breaking system configuration
**Consequence:** System may not boot or work correctly
**Solution:** Always backup configuration files before editing

### Mistake 7: Killing Wrong Process
**Problem:** Killing critical system process
**Consequence:** System instability or crash
**Solution:** Verify PID and process name before killing, prefer SIGTERM over SIGKILL

### Mistake 8: Not Checking Before Destructive Operations
**Problem:** Executing destructive commands without verification
**Consequence:** Unintended data loss
**Solution:** Verify path, list directory contents before deletion

### Mistake 9: Hardcoding Paths in Scripts
**Problem:** Scripts fail when run from different directories
**Consequence:** Scripts not portable
**Solution:** Use relative paths or `$(pwd)` for absolute path

### Mistake 10: Not Quoting Variables in Shell Scripts
**Problem:** Spaces in variable values break commands
**Consequence:** Command fails with syntax error
**Solution:** Always quote variables: `"$var"`, `"$@"`

### Mistake 11: Not Checking Exit Status in Scripts
**Problem:** Script continues despite errors
**Consequence:** Errors propagate, silent failures
**Solution:** Check `$?` after critical commands, handle failures

---

## Troubleshooting

### Permission Denied
**Problem:** Permission denied when executing command
**Solutions:**
- Check file/directory permissions with `ls -la`
- Use `sudo` if you have permission
- Check user/group membership
- Verify you are the file owner

### Command Not Found
**Problem:** Command not found error
**Solutions:**
- Check PATH: `echo $PATH`
- Install package: `sudo apt install package`
- Check spelling: command name might be different
- Verify package is installed: `dpkg -l | grep command`

### Process Not Found
**Problem:** Kill fails with "No such process"
**Solutions:**
- Check PID: `ps aux | grep process`
- Verify process is running
- Process may have already exited

### Service Failed to Start
**Problem:** systemd service fails to start
**Solutions:**
- Check status: `systemctl status service`
- Check logs: `journalctl -u service`
- Check unit file syntax
- Check ExecStart path and permissions
- Check dependencies

### Port Already in Use
**Problem:** Port already in use error
**Solutions:**
- Find process using port: `ss -t listening`
- Kill process: `kill <PID>`
- Choose different port
- Check if service is supposed to be running

### DNS Failure
**Problem:** Cannot resolve hostname
**Solutions:**
- Check DNS configuration: `cat /etc/resolv.conf`
- Test DNS: `nslookup google.com`
- Check network connectivity
- Restart DNS service: `sudo systemctl restart systemd-resolved`

### Network Interface Unavailable
**Problem:** Interface not found or down
**Solutions:**
- Check interfaces: `ip link show`
- Bring interface up: `sudo ip link set eth0 up`
- Check network cable
- Restart network service: `sudo systemctl restart NetworkManager`

### Device Permission Denied
**Problem:** Cannot access device file
**Solutions:**
- Check device permissions: `ls -l /dev/ttyUSB0`
- Add user to appropriate group: `sudo usermod -aG dialout $USER`
- Or use sudo when accessing device

### No Space Left on Device
**Problem:** System cannot write data
**Solutions:**
- Check disk usage: `df -h`
- Clean package cache: `sudo apt clean`
- Remove old logs: `sudo journalctl --vacuum-time=30d`
- Remove large temporary files in `/tmp`

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between Linux kernel and Linux distribution?
2. What is the difference between shell and terminal?
3. What is the difference between absolute and relative paths?
4. What does 755 mean in symbolic permissions?
5. What is the difference between chmod and chown?
6. What is the difference between SIGTERM and SIGKILL?
7. Why is SIGTERM preferred over SIGKILL?
8. What is the difference between foreground and background processes?
9. What does sudo do?
10. What is the difference between apt repository and package?
11. What is a shebang?
12. What is `$0`, `$1`, `$@` in Bash?
13. What is the difference between `=` and `==` in Bash?
14. What is the difference between service and daemon?
15. What does journalctl do?
16. What is the difference between /dev, /sys, and /proc?
17. What is cross-compilation?
18. What is the difference between host and target?
19. What is the difference between SSH and telnet?
20. What is the difference between block and character devices?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Navigation:** Navigate to /etc, inspect passwd and group files, return to home
2. **File Management:** Create a directory structure, create files, set permissions, remove files
3. **Text Processing:** Use grep and pipes to filter a log file for errors
4. **Permissions:** Change file permissions, change ownership (if allowed), test different permission modes
5. **Process Management:** Start a background process, monitor it, send signals, check exit status
6. **Package Management:** Search for a package, install it, inspect it, remove it
7. **Bash Scripting:** Write a script that reports system information, make it executable, test it
8. **Networking:** Check network configuration, test connectivity, inspect DNS, check sockets
9. **SSH:** Connect to a remote system (if available), execute commands, transfer a file
10. **Hardware Exploration:** Inspect /proc and /sys, identify CPU/memory/network information

**Documentation Required:**
- Script content
- Test results
- System information gathered
- Network configuration discovered
- Hardware information discovered

**Passing Criteria:** All tasks completed with understanding demonstrated.

---

## Completion Checklist

Before moving to Phase 12, verify you have:

- [ ] Understand Linux architecture (kernel, distribution, shell, terminal)
- [ ] Can navigate Linux filesystem confidently
- [ ] Can manage files and directories safely
- [ ] Can use text processing tools (grep, pipes, redirection)
- [ ] Understand users, groups, permissions
- [ ] Can manage processes and signals
- [ ] Can install and manage packages
- [ ] Can write basic Bash scripts
- [ ] Understand environment variables
- [ ] Can manage systemd services
- [ ] Can inspect logs (journalctl, dmesg)
- [ ] Can configure and troubleshoot networking
- [ ] Can use SSH for remote access
- [ ] Understand Linux device files (/dev, /sys, /proc)
- [ ] Can compile C programs on Linux
- **Completed Lab 1** - Linux CLI Fundamentals
- **Completed Lab 2** - Filesystem Investigation
- **Completed Lab 3** - Text Processing
- **Completed Lab 4** - Users and Permissions
- **Completed Lab 5** - Process Management
- **Completed Lab 6** - Package Management
- **Completed Lab 7** - Bash Automation
- **Completed Lab 8** - Network Diagnostics
- **Completed Lab 9** - SSH (if available)
- **Completed Lab 10** - systemd Service
- **Completed Lab 11** - C Development on Linux
- **Completed Lab 12** - Embedded Linux Exploration
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Completed the Linux System Monitor project

---

## Do Not Continue Until...

**Do not start Phase 12 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can navigate Linux comfortably using CLI
5. You understand permissions and security
6. You can manage processes and services
7. You can write basic Bash scripts
8. You can inspect logs and troubleshoot networking
9. You can use SSH for remote access
10. You understand /dev, /sys, /proc interfaces
11. You can compile C programs on Linux
12. You understand embedded Linux architecture concepts
13. You understand host vs target and cross-compilation

**Linux is the foundation of embedded Linux and Raspberry Pi. Mastering Linux CLI and understanding embedded Linux architecture is essential before working with Raspberry Pi or custom embedded Linux systems.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 12 — Raspberry Pi**

Phase 12 will teach you about Raspberry Pi GPIO, sensors, hardware interfacing, embedded Linux on Raspberry Pi, and practical Raspberry Pi projects, building on the Linux foundation you established here.

---

**Linux CLI skills are essential for embedded Linux development. Understanding Linux architecture, permissions, processes, services, and development tools is critical for any embedded Linux work, including Raspberry Pi and custom embedded Linux systems.**
