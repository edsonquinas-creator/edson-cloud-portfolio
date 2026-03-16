# AWS Cloud Portfolio - Edson Quinas

Welcome to my AWS Cloud Architecture portfolio. This repository contains hands-on projects demonstrating core cloud infrastructure, security, FinOps, and automation skills. All projects were built adhering to the AWS Well-Architected Framework.

---

## 🌐 Project 1: Custom VPC & Secure Cloud Networking
**Overview:** Provisioned a custom AWS environment featuring both public-facing and fully isolated private subnets. Established secure outbound internet access for private resources using a NAT Gateway, mapped out the traffic flow with custom Route Tables, and executed a precise infrastructure teardown to maintain a strict zero-cost cloud footprint.
* **Services Used:** Amazon VPC, Subnetting, Route Tables, NAT Gateways, Internet Gateways
* **Key Features:** Strict network isolation, secure internet routing, and FinOps-driven teardown.
* 📁 **[View Project Details & Proof](./portfolio-vpc)**

---

## ⚙️ Project 2: Infrastructure as Code (IaC) Deployment
**Overview:** Wrote and deployed a declarative template to automatically provision and manage compute resources.
* **Services Used:** AWS CloudFormation, Amazon EC2, YAML
* **Key Features:** Automated resource provisioning, parameter-based AMI selection, and one-click stack teardown for cost control.
* 📁 **[View Project Details & Proof](./infrastructure-as-code)**

---

## 🌍 Project 3: Serverless Global Static Website
**Overview:** This project demonstrates a serverless static website hosted on AWS. It uses a global Content Delivery Network (CDN) to ensure low latency and high security.
* **Services Used:** Amazon S3, Amazon CloudFront, AWS IAM
* **Key Features:** Content cached globally in Edge Locations, direct public access to S3 blocked via Origin Access Control (OAC), and high availability.
* 📁 **[View Project Details & Proof](./serverless-website)**

---

## 🚨 Project 4: Automated NOC Alerting System
**Overview:** Architected a monitoring solution that tracks compute performance and triggers automated emergency alerts.
* **Services Used:** Amazon CloudWatch, Amazon SNS, Amazon EC2
* **Key Features:** Custom CloudWatch metric alarms, SNS email subscription routing, and simulated CPU stress-test validation.
* 📁 **[View Project Details & Proof](./monitoring-alerting-system)**

---

## 💰 Project 5: FinOps & Cost Governance
**Overview:** Implemented strict financial guardrails to maintain a zero-cost infrastructure footprint within the AWS Free Tier.
* **Services Used:** AWS Budgets, AWS Cost Anomaly Detection, AWS Cost Explorer
* **Key Features:** Automated $0 budget alerts, machine-learning anomaly detection, and granular cost tracking.
* 📁 **[View Project Details & Proof](./finops-auditor)**

  ---

  🛑 Project 6: Automated FinOps Cost Optimization Engine
Overview: Engineered an automated Python script to enforce cloud right-sizing and eliminate weekend OpEx waste by programmatically shutting down idle development servers.

Services Used: Python, AWS Boto3 SDK, Amazon EC2, AWS CloudShell
Key Features: Tag-based resource targeting, programmatic API execution, and automated cost-control governance.
📁 **[View Project Details & Proof](./aws-finops-ec2-optimizer)

