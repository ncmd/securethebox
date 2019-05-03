# Challenge Template
## Content:
PART I - Introduction:
One-liner on why they are doing this challenge.
One-liner on what they will be graded on (provide some transparency here)
One-liner on the amount of time they have for this challenge (1hr)
One-liner involving limitations of attempting challenge
One-liner on recommended skills to successfully complete challenge

PART I Example:
*This challenge is used to assess your skills in defending, responding, and preventing an attack against a web application.*
*You will be graded on 1 Scenario with a max possible score of 10.*
*Time to complete this challenge is within 1 hour.*
*You will not be provided answers after this challenge, but your results will be emailed to you.*
*You are not allowed to....*
*Successful candidates have the following skills*
- [ ] Linux CLI experience
- [ ] Web Application Pentesting Experience
- [ ] Experience with javascript
- [ ] Experience editing files/code
- [ ] Experience with Web Application Firewalls
- [ ] Experience with searching log data
- [ ] Experience with Operating System Forensics

PART II - Problem:
One-liner involving the scenario.
One-liner involving current attack scenario, responsibility, and resources involved.

PART II Example:
*Scenario:*
*You receive alerts of an attack in progress against a web application from your SIEM (Splunk) and Web Application Firewall (Modsecurity)*
*There is an active attacker attempting hack your company's web application, detect and prevent them from stealing sensitive customer information!*

PART III - Resources:
Table containing resources
name | url_location

PART III - Example:
**Here are your resources**
name | url_location
splunk | http://splunk-userName.us-west1-a.securethebox.us
modsecurity | http://nginx-modsecurity-userName.us-west1-a.securethebox.us
modsecurity cloudcmd | http://nginx-modsecurity-userName-cloudcmd.us-west1-a.securethebox.us
vulnerable app | http://app-userName.us-west1-a.securethebox.us
vulnerable app cloudcmd | http://app-userName-cloudcmd.us-west1-a.securethebox.us
wireshark | http://wireshark-userName.us-west1-a.securethebox.us

*Tips:*
splunk cheatsheet | http://splunk-userName.us-west1-a.securethebox.us
modsecurity cheatsheet| http://nginx-modsecurity-userName.us-west1-a.securethebox.us
vulnerable app cheatsheet| http://app-userName.us-west1-a.securethebox.us
wireshark cheatsheet| http://wireshark-userName.us-west1-a.securethebox.us

PART IV - Grading Criteria:
- [ ] Identify asset under attack.
- [ ] Stop the attack in progress.
- [ ] Cut off the attack vector.
- [ ] Identify timeline of attack.
- [ ] Identify app vulnerabilities.
- [ ] Identify attacker artifacts.
- [ ] Apply additional mitigations, 
- [ ] Apply monitoring solutions.
- [ ] Identify compromised data/files/etc.
- [ ] Forensic analysis of compromised systems.
- [ ] Apply static analysis, scan code for vulnerabilities
- [ ] Apply dynamic analysis (burp suite)



# Data Format
**Categories:**
[
    {
        'id'   : 0,
        'value': 'sql_injection',
        'label': 'sql_injection',
        'color': red[500]
    },
    {
        'id'   : 1,
        'value': 'cross_site_scripting',
        'label': 'cross_site_scripting',
        'color': red[500]
    },
]

**Courses:**
[
    {
        'id'         : '15459251a6d6b397565',
        'title'      : 'SQL Injection (MYSQL)',
        'slug'       : 'challenge-1',
        'description': 'Handling SQL Injection Attacks',
        'category'   : 'sql_injection',
        'length'     : 120,
        'totalSteps' : 5,
        'activeStep' : 0,
        'updated'    : 'Apr 12, 2019',
        'steps'      : demoSteps
    },
    {
        'id'         : '15459251a6d6b397566',
        'title'      : 'Cross-Site Scripting (Angular)',
        'slug'       : 'challenge-1',
        'description': 'Handling Cross-Site Scripting Attacks',
        'category'   : 'cross_site_scripting',
        'length'     : 120,
        'totalSteps' : 5,
        'activeStep' : 0,
        'updated'    : 'Apr 12, 2019',
        'steps'      : demoSteps
    }
 ]

**Steps:**
[
    {
        'id'     : '0',
        'title'  : 'Introduction',
        'content': '<h1>Problem 1</h1>
    }
]