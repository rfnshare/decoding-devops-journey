# 🐧 Linux Basics Notes

## Basic Commands & Navigation

- `whoami` — Show current user  
- `pwd` — Show current working directory  
- `cd /path` — Change directory  
- `ls` — List directory contents  
- `ls -l` — List with details (permissions, owner, size, date)  
- `ls -a` — List including hidden files  
- `ls -lt` — List by modification time (newest first)  
- `ls -ltr` — List by modification time (oldest first)  

---

## Understanding File Types from `ls -l`

When you run `ls -l`, the very first character of each line shows the **file type**:

| Character | File Type           | Description                    |
|-----------|---------------------|--------------------------------|
| `-`       | Regular file        | Normal file                    |
| `d`       | Directory           | Folder containing files        |
| `l`       | Symbolic link       | Shortcut or reference to another file or directory |
| `c`       | Character device    | Device file for character devices (e.g., keyboard) |
| `b`       | Block device        | Device file for block devices (e.g., hard drives) |
| `p`       | Named pipe (FIFO)   | Special file for inter-process communication |
| `s`       | Socket              | Special file for network communication |


---

## File and Directory Management

- `mkdir dirname` — Create directory  
- `cp source destination` — Copy files or directories  
- `mv source destination` — Move or rename files/directories  
- `rm filename` — Remove file  
- `rm -r dirname` — Remove directory recursively  
- `touch filename` — Create empty file or update timestamp  
- `ln -s target linkname` — Create symbolic (soft) link  
- `unlink linkname` — Remove a symbolic link  

---

## Viewing and Editing Files

- `cat filename` — View file contents  
- `vim filename` — Open file in Vim editor  
- In Vim:
  - `i` — Insert mode  
  - `Esc` — Exit insert mode  
  - `5yy` — Yank (copy) 5 lines  
  - `p` — Paste after cursor  
  - `:wq` — Save and quit  
  - `:q!` — Quit without saving  

---

## System Information

- `uptime` — Show system uptime  
- `cat /proc/uptime` — Detailed uptime info  
- `free -m` — Show memory usage in MB  

---

## Searching & Filtering -- Ongoing

- `grep pattern filename` — Search for a pattern in a file  
- `grep -i pattern filename` — Case-insensitive search  
- `grep -R pattern directory` — Recursive search in directory  

---

## Miscellaneous

- `history` — Show command history  
- `clear` — Clear terminal screen  

---

## Notes from Practice Session

- Explored `/boot/grub/grub2/grub.cfg` file to understand boot loader config  
- Used `ln -s` to create symbolic links and practiced unlinking  
- Learned how moving original file breaks symbolic links until restored  
- Edited `/etc/hostname` to change the system hostname  
- Used `grep` extensively to search config files for keywords (e.g., "fire", "SELINUX")  
- Edited SELinux config file `/etc/selinux/config`  

---

Keep practicing these basics, they are the foundation of any DevOps or Linux admin work!
