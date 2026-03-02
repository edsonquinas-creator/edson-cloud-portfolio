# 🌍 Project: Serverless Global Static Website

**Objective:** Deploy a highly available, secure, and globally distributed static website using native AWS serverless architecture. 

### 🛠️ Architecture & Services
* **Amazon S3 (Simple Storage Service):** Acts as the origin server, hosting the foundational `index.html` web files.
* **Amazon CloudFront:** A global Content Delivery Network (CDN) that caches the website content in edge locations worldwide for ultra-low latency.
* **AWS IAM & Origin Access Control (OAC):** Secures the infrastructure by strictly blocking direct public access to the S3 bucket, forcing all traffic to route exclusively through the CloudFront distribution.

### 🔐 Security & Cost Optimization
* **Zero Direct Access:** The S3 bucket policy is configured to deny all `s3:GetObject` requests unless they originate from the specific CloudFront distribution ARN.
* **Free Tier Optimized:** Built entirely within the AWS Free Tier limits, utilizing serverless billing (pay-only-for-what-you-use) rather than provisioning always-on EC2 web servers.

### 📂 Repository Contents
* [index.html](./index.html): The source code for the static website deployed to the S3 bucket origin.

---
*This project demonstrates a fundamental understanding of decoupled cloud architecture, global content delivery, and the principle of least privilege using AWS IAM and bucket policies.*
