# Vulnerability Assessment Tool
# FUTURE_CS_01 - Web Application Security Testing

import json
from datetime import datetime
from typing import List, Dict

class Vulnerability:
    def __init__(self, name, severity, cvss, description):
        self.name = name
        self.severity = severity
        self.cvss = cvss
        self.description = description
        self.date = datetime.now().isoformat()

class SecurityReport:
    def __init__(self, project, assessor):
        self.project = project
        self.assessor = assessor
        self.vulnerabilities = []
    
    def add_vulnerability(self, vuln):
        self.vulnerabilities.append(vuln)
    
    def get_stats(self):
        critical = sum(1 for v in self.vulnerabilities if v.cvss >= 9)
        high = sum(1 for v in self.vulnerabilities if 7 <= v.cvss < 9)
        medium = sum(1 for v in self.vulnerabilities if 4 <= v.cvss < 7)
        
        return {
            'total': len(self.vulnerabilities),
            'critical': critical,
            'high': high,
            'medium': medium,
            'avg_cvss': round(sum(v.cvss for v in self.vulnerabilities) / len(self.vulnerabilities), 2) if self.vulnerabilities else 0
        }
    
    def print_report(self):
        print(f"\n{'='*60}")
        print(f"SECURITY ASSESSMENT REPORT")
        print(f"{'='*60}")
        print(f"Project: {self.project}")
        print(f"Assessor: {self.assessor}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        stats = self.get_stats()
        print(f"\nVulnerability Summary:")
        print(f"  Total: {stats['total']}")
        print(f"  Critical: {stats['critical']}")
        print(f"  High: {stats['high']}")
        print(f"  Medium: {stats['medium']}")
        print(f"  Avg CVSS: {stats['avg_cvss']}")
        
        print(f"\nVulnerabilities:")
        for i, v in enumerate(self.vulnerabilities, 1):
            print(f"\n  {i}. {v.name}")
            print(f"     Severity: {v.severity} (CVSS: {v.cvss})")
            print(f"     {v.description}")

# Example usage
if __name__ == "__main__":
    report = SecurityReport("FUTURE_CS_01 - DVWA", "Dhanush G")
    
    report.add_vulnerability(
        Vulnerability("SQL Injection", "CRITICAL", 9.8, "Database query manipulation")
    )
    report.add_vulnerability(
        Vulnerability("Cross-Site Scripting", "HIGH", 6.1, "Malicious script injection")
    )
    report.add_vulnerability(
        Vulnerability("Security Misconfiguration", "MEDIUM", 5.3, "Missing security headers")
    )
    
    report.print_report()
