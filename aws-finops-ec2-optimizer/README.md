# ☁️ AWS FinOps: Automated EC2 Cost Optimization

## 📊 The Business Problem
In cloud environments, a common source of **OpEx waste** occurs when development and testing servers (Amazon EC2) are left running outside of business hours. Paying for idle compute capacity over the weekend directly violates cloud right-sizing and cost-efficiency principles.

## 🛠️ The Solution
I engineered an automated Python script utilizing the **AWS Boto3 SDK** to enforce cost-control governance. 

The script programmatically scans the AWS environment (eu-west-2) to identify any running instances carrying the specific resource tag `Environment: Dev`. It then safely issues a stop command to those specific instances, ensuring the business only pays for compute power when it is actively being utilized.

## 🚀 Technologies Used
* **Python 3** (Core logic and automation)
* **AWS Boto3** (Programmatic API interaction with AWS)
* **Amazon EC2** (Compute resource management)
* **AWS IAM** (Secure, least-privilege access execution)

## 💡 Commercial Impact
* Eliminates weekend CapEx/OpEx drain caused by human error (forgetting to turn off servers).
* Demonstrates practical application of cloud elasticity (paying only for what you use).
* Replaces manual IT Service Desk intervention with a scalable, £0.00 cost automated script.
