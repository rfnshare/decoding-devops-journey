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

## What is CI/CD

- **CI**: Continuous integration is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.
- **CD**: Continuous delivery is a software development practice where code changes are automatically prepared for a release to production.

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




