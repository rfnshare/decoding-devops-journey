## 🖥️ Local VM Setup for DevOps Practice

### 🔧 Tools Used:
- **Vagrant** – For VM automation
- **CentOS 7** – RHEL-based Linux for server practice
- **Ubuntu (Jammy Jellyfish 22.04)** – User-friendly Debian-based distro

---

### ✅ VM Setup: CentOS 7 using Vagrant

```bash
# Create and enter project directory
mkdir centos-vm && cd centos-vm

# Initialize Vagrant with CentOS Stream 9
vagrant init eurolinux-vagrant/centos-stream-9

# Start the VM
vagrant up

# SSH into the machine
vagrant ssh

# (Optional) Reload or halt/stop
vagrant reload
vagrant halt

# (Optional) Destroy Vagrant [Remove Created File]
vagrant destroy

# List of boxes
vagrant box list

# Create and enter project directory
mkdir ubuntu-vm && cd ubuntu-vm

# Initialize with Ubuntu Jammy64
vagrant init ubuntu/jammy64

# Start and SSH
vagrant up
vagrant ssh

# Common Commands
# See Status for all VM's
vagrant global-status

# Cleaned Extra VM's
vagrant global-status --prune
```