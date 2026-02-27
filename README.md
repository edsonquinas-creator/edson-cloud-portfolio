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
* 📁 **[View Project Details & Proof](./Monitoring%20%26%20Alerting%20System)**

---

## ⚙️ Project 4: Infrastructure as Code (IaC) Deployment
**Overview:** Wrote and deployed a declarative template to automatically provision and manage compute resources.
* **Services Used:** AWS CloudFormation, Amazon EC2, YAML
* **Key Features:** Automated resource provisioning, parameter-based AMI selection, and one-click stack teardown for cost control.
* 📁 **[View Project Details & Proof](./03-infrastructure-as-code)**
