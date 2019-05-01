Application should log these events:
Invalid Input
SQL Injection Attempts
Cross Site Scripting Attempts
Failed Authentication
Authorization Failures
Session Tracking Problems
Critical portions of business logic


Server Identity
Client IP Address
Username
Date/Time
URL
POST data
Cookies

Connections to DB with administrator privilege

Records detailed information 
Execution of stored procedures
Creation or deletion of objects like tables
Querying of tables
Permission changes

Captures login/logout 


What could have been done better:

Encryption of sensitive info in the DB

More advanced DB logging

Security reviews of code



What they should find:

This was a backdoor – an insider job?
Reviewed code archives to detect addition of code
The first check-in with this code was made by a developer contracted from a third-party in Asia
Found the URL with the additional parameter in the web server logs
The client IP traced back to Asia!


https://www.blackhat.com/presentations/bh-usa-06/BH-US-06-Willis.pdf