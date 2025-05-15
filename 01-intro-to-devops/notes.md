# 🛠️ Introduction to DevOps

## What is DevOps?

DevOps is a set of practices, tools, and a cultural philosophy that automates and integrates the processes between software development and IT operations teams.

- **Dev** = Software Development
- **Ops** = IT Operations
- Goal: Deliver applications and services at high velocity

---

## Key Benefits

- Faster time to market
- Improved collaboration and communication
- Increased deployment frequency
- Reduced failure rate of new releases
- Faster recovery time in case of failure

---

## Traditional vs DevOps Approach

| Aspect                | Traditional IT | DevOps               |
|-----------------------|----------------|----------------------|
| Development & Ops     | Siloed         | Collaborative        |
| Deployments           | Manual         | Automated (CI/CD)    |
| Feedback Cycle        | Slow           | Fast                 |
| Infrastructure Mgmt   | Manual setup   | IaC (e.g., Terraform)|
| Monitoring            | Reactive       | Proactive            |

---

## DevOps Lifecycle Phases

1. **Plan** – Requirements and planning (Agile, Jira, etc.)
2. **Develop** – Code development (Git, GitHub)
3. **Build** – Compilation and build (Maven, Gradle)
4. **Test** – Automated testing (JUnit, Selenium)
5. **Release** – Versioning and approval
6. **Deploy** – Automated deployment (CI/CD tools like Jenkins)
7. **Operate** – Infrastructure and system administration (Docker, K8s)
8. **Monitor** – Continuous feedback (Prometheus, ELK Stack)

---

## Core DevOps Tools (by Category)

- **Source Control**: Git, GitHub, GitLab
- **CI/CD**: Jenkins, GitHub Actions, CircleCI
- **Containers**: Docker
- **Container Orchestration**: Kubernetes
- **Infrastructure as Code (IaC)**: Terraform, Ansible
- **Monitoring**: Prometheus, Grafana, ELK Stack

---

## DevOps Culture

- **Collaboration**: Shared responsibilities between Dev and Ops
- **Automation**: Everything from testing to deployment
- **Measurement**: Metrics-driven improvements
- **Feedback**: Fast and continuous feedback loops

---

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

# Initialize Vagrant with CentOS 7
vagrant init centos/7

# Start the VM
vagrant up

# SSH into the machine
vagrant ssh

# (Optional) Reload or halt
vagrant reload
vagrant halt

# Create and enter project directory
mkdir ubuntu-vm && cd ubuntu-vm

# Initialize with Ubuntu Jammy64
vagrant init generic/ubuntu2204

# Start and SSH
vagrant up
vagrant ssh
```
#  AWS Setup

I have configured an Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instance for cloud-based deployments and experimentation.

- Configured an EC2 instance.  
- Added an SSH certificate for secure login.  
- Purchased a custom domain: **aalfaroque.me**.  
- Mapped the custom domain to the EC2 instance using Route 53 and the EC2 instance's IP address.  

# Personal Lab Setup & Tools

On my local Windows machine, I've installed various DevOps tools using Chocolatey, a package manager for Windows.

- **VirtualBox:** For running the local Ubuntu virtual machine.  
- **Vagrant:** For managing and provisioning the virtual machine.  
- **Git:** For version control and collaboration.  
- **Amazon Corretto (Java):** A no-cost, multiplatform, production-ready distribution of the Open Java Development Kit (OpenJDK).  
- **Maven:** A build automation tool primarily used for Java projects.  
- **AWS CLI:** The official command-line interface for interacting with AWS services.  
- **IntelliJ IDEA:** An integrated development environment (IDE) for Java and other languages.  
- **Visual Studio Code:** A lightweight but powerful source code editor.  
- **Sublime Text 3:** A sophisticated text editor for code, markup, and prose.  


