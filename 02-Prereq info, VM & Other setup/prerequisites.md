# ⚙️ Prerequisites Info & Setup

## Tools Prerequisites Information

* **Source Code For This Project:** https://github.com/hkhcoder/vprofile-project

## Personal Lab Setup & Tools

On my local Windows machine, I've installed various DevOps tools using **Chocolatey**, a package manager for Windows. For MacOS use brew.

* **Install Choco [Windows]:**

    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('[https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)'))
    ```

    * **Common Commands:** `choco install <package>`, `choco upgrade <package>`

* **Install brew [MacOS]:**

    ```bash
    /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
    ```

    * **Common Commands:** `brew install <package>`, `brew upgrade <package>`

  
- **JDK8:** A no-cost, multiplatform, production-ready distribution of the Open Java Development Kit (OpenJDK).  
- **Maven:** A build automation tool primarily used for Java projects. 
- **IntelliJ IDEA:** An integrated development environment (IDE) for Java and other languages.  
- **Sublime Text 3:** A sophisticated text editor for code, markup, and prose.  
- **AWS CLI:** The official command-line interface for interacting with AWS services.
- **Visual Studio Code:** A lightweight but powerful source code editor.
### Installed Tools & Commands:

* **Oracle VirtualBox:**

    * **Purpose:** For running the local Ubuntu virtual machine.
    * **Install Command (Windows/Choco):** `choco install virtualbox --version=7.1.4 -y`
    * **Install Command (MacOS/Brew):** `brew install --cask virtualbox`

* **Git:**

    * **Purpose:** For version control and collaboration.
    * **Install Command (Windows/Choco):** `choco install git -y`
    * **Install Command (MacOS/Brew):** `brew install git`

* **Vagrant:**

    * **Purpose:** For managing and provisioning the virtual machine.
    * **Install Command (Windows/Choco):** `choco install vagrant --version=2.4.3 -y`
    * **Install Command (MacOS/Brew):** `brew install --cask vagrant`
    * **Install Command #2 (MacOS/Brew):** `brew install --cask vagrant-manager`

* **JDK8:**

    * **Purpose:** Open Java Development Kit (OpenJDK).
    * **Install Command (Windows/Choco):** `choco install corretto17jdk -y`
    * **Install Command (MacOS/Brew):** `brew install openjdk@17`
    * **Install Command #2 (MacOS/Brew):** `sudo ln -sfn $HOMEBREW_PREFIX/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk`
    * **Install Command #3 (MacOS/Brew):** `exec zsh -l`

* **Maven:**

    * **Purpose:** Build automation tool for Java projects.
    * **Install Command (Windows/Choco):** `choco install maven -y`
    * **Install Command (MacOS/Brew):** `brew install maven`

* **IntelliJ IDEA:**

    * **Purpose:** Integrated development environment (IDE) for Java.
    * **Install Command (Windows/Choco):** `choco install intellijidea-community -y`
    * **Install Command (MacOS/Brew Cask):** `brew install --cask intellij-idea`
    * **Install Command #2 (MacOS/Brew Cask):** `brew install --cask intellij-idea-ce`

* **Sublime Text 3:**

    * **Purpose:** A sophisticated text editor.
    * **Install Command (Windows/Choco):** `choco install sublimetext3 -y`
    * **Install Command (MacOS/Brew Cask):** `brew install --cask sublime-text`

* **AWS CLI:**

    * **Purpose:** Command-line interface for interacting with AWS services.
    * **Install Command (Windows/Choco):** `choco install awscli -y`
    * **Install Command (MacOS/Brew):** `brew install awscli`

* **Visual Studio Code:**

    * **Purpose:** A powerful source code editor.
    * **Install Command (Windows/Choco):** `choco install vscode -y`
    * **Install Command (MacOS/Brew Cask):** `brew install --cask visual-studio-code`
---
* You can verify installation using `choco list`
---

## Signups

* **Accounts Needed:**
    * [List of services requiring signup, e.g., GitHub, GoDaddy,Docker Hub, SonarCloud]
* **Important Notes for Each Signup:**
    * GitHub: [Select Free Plan]
    * GoDaddy: [Purchase a low-cost domain, e.g., yourdomainname.xyz]
    * SonarCloud:

## 15. AWS Setup

**I have configured an Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instance for cloud-based deployments and experimentation.**

* Created Free Tier Account, Root User [Assigned MFA]
* Created IAM user [Added AdministratorAccess policies, Assigned MFA], Account Alias
* Configured an EC2 instance.
    * Added an SSH certificate for secure login.
* Purchased a custom domain: **aalfaroque.me**.
* Mapped the custom domain to the EC2 instance using Route 53 and the EC2 instance's IP address.
* Added & Set Billing Alarm
* **AWS CLI Installation/Configuration:**
    * [Steps for setting up AWS CLI]
    * `aws configure`
* **Region/Availability Zone Considerations:**
    * [Notes: Region: US East N. Virginia]
