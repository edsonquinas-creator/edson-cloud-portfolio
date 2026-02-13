# AWS Cloud Portfolio - Edson Quinas

## Project Overview
This project demonstrates a serverless static website hosted on AWS. It uses a global Content Delivery Network (CDN) to ensure low latency and high security.

## Architecture
* **Storage:** Amazon S3 (Standard Class)
* **CDN:** Amazon CloudFront (Edge Locations)
* **Security:** Origin Access Control (OAC) & Bucket Policies
* **Version Control:** GitHub

## Key Features
* **Global Reach:** Content is cached in 450+ Edge Locations.
* **Security:** Direct public access to S3 is blocked; traffic must flow through CloudFront.
* **Cost Optimization:** Uses Free Tier eligible services.
