# AWS Cloud Portfolio - Edson Quinas

Welcome to my AWS Cloud Architecture portfolio. This repository contains hands-on projects demonstrating core cloud infrastructure, security, FinOps, and automation skills. All projects were built adhering to the AWS Well-Architected Framework.

---

## 🌐 Project 1: Serverless Global Static Website
**Overview:** This project demonstrates a serverless static website hosted on AWS. It uses a global Content Delivery Network (CDN) to ensure low latency and high security.

**Architecture:**
* **Storage:** Amazon S3 (Standard Class)
* **CDN:** Amazon CloudFront (Edge Locations)
* **Security:** Origin Access Control (OAC) & Bucket Policies
* **Version Control:** GitHub

**Key Features:**
* **Global Reach:** Content is cached in 450+ Edge Locations.
* **Security:** Direct public access to S3 is blocked; traffic must flow through CloudFront.
* **Cost Optimization:** Uses Free Tier eligible services.

---

## 💰 Project 2: FinOps & Cost Governance
**Overview:** Implemented strict financial guardrails to maintain a zero-cost infrastructure footprint within the AWS Free Tier.
* **Services Used:** AWS Budgets, AWS Cost Anomaly Detection, AWS Cost Explorer
* **Key Features:** Automated $0 budget alerts, machine-learning anomaly detection, and granular cost tracking.
* 📁 **[View Project Details & Proof](/finops-auditor)**

---

## 🚨 Project 3: Automated NOC Alerting System
**Overview:** Architected a monitoring solution that tracks compute performance and triggers automated emergency alerts.
* **Services Used:** Amazon CloudWatch, Amazon SNS, Amazon EC2
* **Key Features:** Custom CloudWatch metric alarms, SNS email subscription routing, and simulated CPU stress-test validation.
* 📁 **[View Project Details & Proof](./monitoring-alerting-system)**

---

## ⚙️ Project 4: Infrastructure as Code (IaC) Deployment
**Overview:** Wrote and deployed a declarative template to automatically provision and manage compute resources.
* **Services Used:** AWS CloudFormation, Amazon EC2, YAML
* **Key Features:** Automated resource provisioning, parameter-based AMI selection, and one-click stack teardown for cost control.
* 📁 **[View Project Details & Proof](./infrastructure-as-code)**

---

# 🌐 Project 5: Custom VPC Architecture & Secure Networking

**Objective:** Architect a secure, highly available Virtual Private Cloud (VPC) from scratch, demonstrating strict network isolation and routing controls, followed by a complete infrastructure teardown.



### 🛠️ Architecture & Execution
* Provisioned a custom **Amazon VPC** with a dedicated CIDR block.
* Carved out strict network boundaries by creating a **Public Subnet** (auto-assigned public IPs enabled) and a **Private Subnet** (fully isolated).
* Deployed an **Internet Gateway (IGW)** to provide public internet access to the public tier.
* Deployed a **NAT Gateway** with an Elastic IP to allow resources in the private subnet to securely download updates without inbound internet exposure.
* Configured custom **Route Tables** to securely direct traffic between the subnets and gateways.
* Executed a complete, automated resource teardown to maintain a $0.00 FinOps footprint.

---

### 📸 Proof of Execution

#### Phase 1: The Foundation (VPC & Subnets)
**1. Custom VPC Created:**
![VPC Created](portfolio.vpc.png)

**2. Subnets Initialized:**
![Subnets Created](subnets.png)
![Private Subnet Creation](private.subnet.png)

**3. Configuring Network Isolation (Auto-Assign IPs):**
![Auto Assign Setting](subnet.auto.assign.png)
![Subnet Isolation Verified](auto.assign.png)

#### Phase 2: The Gateways (Public & Private Access)
**4. Internet Gateway Attached (Public Access):**
![IGW Attached](igw.attached.png)

**5. NAT Gateway Provisioned (Secure Private Access):**
![NAT Creation](portfolio.nat.png)

#### Phase 3: The Routing (Connecting the Pipes)
**6. Public Route Table & Subnet Association:**
![Public RT](public.rt.png)
![Public RT Routes](rt.routes.png)
![Public Association](sub.associations.png)

**7. Private Route Table & Subnet Association:**
![Private RT](private.rt.png)
![Private RT Routes](private.rt.updates.png)
![Private Association](private.association.png)

**8. Successful Routing Verification:**
![Success Routing](success.png)

#### Phase 4: FinOps & Infrastructure Teardown
**9. Destroying the NAT Gateway:**
![NAT Teardown Initiated](nat.teardown.png)
![NAT Deleted](nat.deleted.png)

**10. Releasing the Elastic IP (Cost Prevention):**
![EIP Released](elastic.ips.released.png)

**11. Final Clean Slate (VPC Destroyed):**
![VPC Deleted](vpc.deleted.png)
