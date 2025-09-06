 ## Penetration Test Script (Python)

This is a simple Python script for performing **basic penetration testing checks** on a web application.  

It focuses on:
- Verifying if the target is served over **HTTPS**
- Checking for **common security headers** used to protect web applications

---

##  Features
-  Check if the target website enforces **HTTPS**
-  Inspect presence of important **security headers**:
  - `Content-Security-Policy`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Strict-Transport-Security`
  - `Referrer-Policy`
-  Handles connection errors gracefully

---

##  Usage

### 1. Clone the Repository
```bash
git clone https://github.com/istajoe/penetration-test.git
cd penetration-test/scripts
