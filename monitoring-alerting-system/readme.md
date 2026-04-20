# 🚨 Project: Automated NOC Alerting System

**Objective:** Architect a real-time monitoring and alerting system to automatically detect and report compute performance anomalies.

## 🗺️ Architecture Diagram
![NOC Alerting Architecture](noc-alerting-architecture.png)

### 🛠️ Architecture & Execution
* Provisioned an **Amazon EC2** instance to serve as the baseline monitored target.
* Configured an **Amazon SNS** (Simple Notification Service) topic and authorized an email subscription for secure alert routing.
* Deployed an **Amazon CloudWatch** alarm to continuously monitor `CPUUtilization`, setting a strict 80% threshold.
* Executed a simulated CPU stress test via the Linux terminal (creating continuous background processes) to intentionally breach the threshold and validate the automated alerting pipeline.

### 📸 Proof of Execution

**1. The Monitored Target (EC2 Instance):**
![EC2 Instance](noc.instance.png)

**2. Alarm Initialization (Gathering Baseline Metrics):**
![Alarm Before](noc.alarm.before.png)

**3. Normal Operations (System OK):**
![Alarm OK](noc.alarm.after.png)

**4. The Stress Test (CPU Threshold Breached):**
![Alarm Limit Hit](noc.alarm.limit.png)

**5. Automated Alert Delivery:**
![Email Alert](email.alarm.png)
