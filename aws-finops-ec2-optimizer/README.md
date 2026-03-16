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

* ## 📸 Proof of Execution
<details>
  <summary>Click to view step-by-step execution logs</summary>

  ### 1. Provisioning & Security
  * **Environment Setup:** Launching the target EC2 instance with specific FinOps tags.
  * **IAM Governance:** Creating a least-privilege IAM user and generating secure access keys.
  
  ### 2. Automation in Action
  * **The "Kill Shot":** Execution of the Python script via CloudShell, successfully identifying the 'Dev' instance and issuing the stop command.
  
  ### 3. Lifecycle Completion
  * **Verified State:** Confirmation of the instance moving to a 'Stopped' state, followed by a 'Terminated' state to ensure a zero-cost footprint.

  *(Screenshots available in the /screenshots folder)*
</details>
