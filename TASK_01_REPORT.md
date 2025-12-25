# Web Application Security Testing – Task 1
## Internship: Future Interns – Cyber Security
**Track Code:** CS  
**Task Number:** 01  
**Trainee Name:** Dhanush G  
**Date:** December 23-24, 2025

---

## 📌 Objective
The objective of this task is to perform comprehensive web application security testing on vulnerable web applications to identify and document common security vulnerabilities including:
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Authentication Weaknesses
- Security Misconfigurations
- Missing Security Headers

---

## 🧰 Tools Used
- **Kali Linux** – Penetration testing operating system
- **OWASP ZAP** – Automated vulnerability scanner
- **Burp Suite** – Web application security testing
- **SQLMap** – SQL injection testing tool
- **DVWA** – Damn Vulnerable Web Application (intentionally vulnerable)
- **Docker** – Application containerization
- **VMware Workstation** – Virtual machine environment

---

## 🌐 Target Application
**DVWA (Damn Vulnerable Web Application)**
- Hosted locally on the system
- URL: `http://localhost/DVWA/`
- Database: MariaDB
- Framework: PHP
- This application is intentionally vulnerable and designed for security learning

---

## 🪜 Step-by-Step Procedure

### Step 1: Environment Setup
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install required dependencies
sudo apt install apache2 mariadb-server php php-mysql -y
```

### Step 2: Start Required Services
```bash
# Start Apache web server
sudo systemctl start apache2

# Start MariaDB database
sudo systemctl start mariadb

# Enable services on startup
sudo systemctl enable apache2
sudo systemctl enable mariadb
```

### Step 3: Install and Configure DVWA
```bash
# Navigate to web root
cd /var/www/html

# Clone DVWA repository
sudo git clone https://github.com/digininja/DVWA.git

# Set permissions
sudo chown -R www-data:www-data /var/www/html/DVWA
```

### Step 4: Database Configuration
```bash
# Access MariaDB
sudo mariadb -u root

# Create database and user
CREATE DATABASE dvwa;
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
EXIT;
```

### Step 5: DVWA Configuration
- Copy config file: `cp config/config.inc.php.dist config/config.inc.php`
- Edit config.inc.php with database credentials
- Access http://localhost/DVWA/ in browser
- Complete setup wizard

### Step 6: Launch OWASP ZAP
```bash
# Open OWASP ZAP
zap.sh &

# Or from Kali menu: Applications > Security > OWASP ZAP
```

### Step 7: Perform Automated Scan
1. In OWASP ZAP, select "Automated Scan"
2. Enter target URL: `http://localhost/DVWA/`
3. Configure scan options
4. Click "Attack" to begin scanning
5. Wait for scan to complete

### Step 8: Manual Testing with Burp Suite
1. Launch Burp Suite Community Edition
2. Configure browser proxy to 127.0.0.1:8080
3. Navigate through DVWA application
4. Capture and analyze HTTP requests/responses
5. Test for vulnerabilities manually

---

## 🚨 Identified Vulnerabilities

### 1️⃣ SQL Injection (SQLi)
**Risk Level:** 🔴 **HIGH**

**Location:** User authentication login form

**Description:**  
Improper input validation on the login page allows attackers to manipulate SQL database queries. By injecting SQL commands in the username field, an attacker can bypass authentication and gain unauthorized access.

**Vulnerable Code Pattern:**
```php
$user = $_GET['username'];
$query = "SELECT * FROM users WHERE username='" . $user . "'";
$result = mysqli_query($connection, $query);
```

**Proof of Concept:**
```
Username: admin' OR '1'='1
Password: anything
```

**Impact:**
- Unauthorized database access
- Data theft and manipulation
- Complete application compromise
- Potential system takeover

**Mitigation:**
- Use prepared statements and parameterized queries
- Implement input validation and sanitization
- Apply least privilege principle to database users
- Use Web Application Firewall (WAF)
- Regular security testing and code reviews

---

### 2️⃣ Cross-Site Scripting (XSS)
**Risk Level:** 🟡 **MEDIUM**

**Location:** Search functionality, comment sections

**Description:**  
Malicious JavaScript code can be injected into web pages and executed in the victim's browser. This allows attackers to steal cookies, session tokens, or perform actions on behalf of the user.

**Types Identified:**
- **Reflected XSS:** Via URL parameters
- **Stored XSS:** Persisted in database
- **DOM-based XSS:** Client-side script vulnerabilities

**Proof of Concept:**
```html
<script>alert('XSS Vulnerability')</script>
<img src=x onerror="alert('XSS')">
```

**Impact:**
- Session hijacking
- Credential theft
- Malware distribution
- Defacement of web content

**Mitigation:**
- Input validation and output encoding
- Content Security Policy (CSP)
- Use security-focused template engines
- Regular security audits
- User education and awareness

---

### 3️⃣ Security Misconfiguration
**Risk Level:** 🟢 **LOW-MEDIUM**

**Description:**  
Missing HTTP security headers expose the application to various attacks.

**Missing Headers Identified:**
- `X-Frame-Options` – Clickjacking protection
- `Content-Security-Policy` – XSS and injection prevention
- `X-Content-Type-Options` – MIME type sniffing prevention
- `Strict-Transport-Security` – HTTPS enforcement
- `X-XSS-Protection` – Browser-level XSS filter

**Mitigation:**
```apache
# Add to Apache configuration
Header set X-Frame-Options "SAMEORIGIN"
Header set X-Content-Type-Options "nosniff"
Header set X-XSS-Protection "1; mode=block"
Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

---

### 4️⃣ Weak Authentication
**Risk Level:** 🔴 **HIGH**

**Issues Found:**
- Default credentials enabled (admin/password)
- No account lockout mechanism
- No password complexity requirements
- Session tokens exposed in URLs
- No multi-factor authentication

**Mitigation:**
- Enforce strong password policies
- Implement account lockout after failed attempts
- Use secure session management
- Enable multi-factor authentication (MFA)
- Regular access control reviews

---

### 5️⃣ Information Disclosure
**Risk Level:** 🟡 **MEDIUM**

**Findings:**
- Detailed error messages revealing system information
- Server version exposed in HTTP headers
- Sensitive data in HTML comments
- Directory listing enabled

**Mitigation:**
- Display generic error messages
- Hide server version information
- Disable directory listing
- Remove sensitive comments from code

---

## 📊 Vulnerability Summary Table

| Vulnerability | Risk Level | Found | Confirmed | Mitigation Applied |
|---|---|---|---|---|
| SQL Injection | HIGH | ✓ | ✓ | Planned |
| XSS | MEDIUM | ✓ | ✓ | Planned |
| Security Headers | MEDIUM | ✓ | ✓ | Planned |
| Weak Authentication | HIGH | ✓ | ✓ | Planned |
| Information Disclosure | MEDIUM | ✓ | ✓ | Planned |
| CSRF | MEDIUM | ✓ | ✓ | Planned |
| Broken Access Control | HIGH | ✓ | ✓ | Planned |

---

## 🎯 Testing Methodology

### Phase 1: Information Gathering
- Identified application technology stack
- Documented application functionality
- Mapped all user input points

### Phase 2: Automated Scanning
- Ran OWASP ZAP automated scan
- Captured vulnerability reports
- Documented findings with evidence

### Phase 3: Manual Testing
- Tested each input vector manually
- Verified automated findings
- Attempted exploitation techniques
- Documented successful exploits

### Phase 4: Analysis & Reporting
- Categorized vulnerabilities by severity
- Documented impact and mitigation
- Prepared recommendations

---

## ✅ Recommendations

### Immediate Actions (Critical)
1. **Patch SQL Injection Vulnerabilities**
   - Implement prepared statements immediately
   - Audit all database queries
   - Deploy input validation middleware

2. **Implement Output Encoding**
   - Encode all user-controllable output
   - Deploy Content Security Policy
   - Enable browser XSS protections

3. **Fix Authentication Issues**
   - Enforce strong passwords
   - Implement account lockout
   - Enable security headers

### Short-term Actions (1-3 months)
1. Implement Web Application Firewall (WAF)
2. Set up security logging and monitoring
3. Conduct developer security training
4. Implement secure SDLC practices

### Long-term Actions (3-12 months)
1. Implement automated security testing in CI/CD
2. Conduct regular penetration testing
3. Establish bug bounty program
4. Achieve OWASP Top 10 compliance

---

## 📚 Learning Outcomes

Through this internship task, I have gained practical knowledge in:

✅ **Web Application Security Concepts**
- Understanding OWASP Top 10 vulnerabilities
- SQL Injection attack vectors and prevention
- XSS exploitation and mitigation techniques
- Authentication and authorization flaws

✅ **Security Testing Tools**
- OWASP ZAP automated scanning
- Burp Suite manual testing capabilities
- SQLMap exploitation techniques
- Vulnerability assessment and reporting

✅ **Vulnerability Management**
- Risk assessment and prioritization
- Impact analysis of security flaws
- Remediation planning
- Security best practices

✅ **Professional Skills**
- Security report documentation
- Technical communication
- Systematic problem-solving
- Attention to detail in security testing

---

## 📝 Conclusion

This security testing exercise on DVWA has successfully identified and documented multiple critical vulnerabilities in web applications. The findings demonstrate common security weaknesses that frequently exist in production systems.

**Key Takeaways:**

1. **Security is Essential:** Web applications handle sensitive data and require robust security measures from design through deployment.

2. **Multiple Layers Needed:** Single security controls are insufficient. Defense-in-depth approach with multiple layers is essential.
 n
3. **Testing is Critical:** Automated scanning combined with manual testing provides comprehensive vulnerability coverage.

4. **Continuous Improvement:** Security is an ongoing process requiring regular updates, patches, and security assessments.

5. **Developer Education:** Most vulnerabilities stem from insecure coding practices that can be prevented through proper training.

---

## 🔗 References

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- DVWA: https://dvwa.co.uk/
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP ZAP: https://www.zaproxy.org/
- CWE Top 25: https://cwe.mitre.org/top25/

---

## 📞 Contact & Support

**Trainee:** Dhanush G  
**Internship:** Future Interns – Cyber Security  
**Track:** CS – 01  
**Repository:** https://github.com/DHANUSHGCODE/FUTURE_CS_01  

*This report demonstrates practical application of web security concepts and testing methodologies.*
