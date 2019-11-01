# MVP API
/api/v1/...

# P1 - MVP

Kubernetes commands
[POST] - DONE
/api/kubernetes/challenges/1/deploy - Deploy challenge #1 pods (traefik, waf, app, splunk)
- params=userName,clusterName,action

[POST] - DONE
/api//kubernetes/challenges/1/destroy - Destroy challenge 1: deletes challenge 1 pods ; args=username ; exec
- params=userName,clusterName,action



# P2

[GET] 
/kubernetes/challenge/1/status/pods - Check deployment status of pods/containers (every 5 seconds)
/kubernetes/challenge/1/status/dns - Check status of dns records created (dig)
/kubernetes/challenge/1/status/pods/ready - Confirm when they are ready (if ready, ready=true)
- args=username,jwt
[GET] 
/kubernetes/challenge/1/status/pods/links - Get urls of containers and present it to frontend
- args=username,jwt
[POST]
/kubernetes/challenge/1/restart - Restart pod (destroy and redeploy)
- args=username,servicename,jwt
[POST]

# P3 - Other

Firebase
[GET]
/app/user/status/logged - Check if user is logged in
/app/user/status/logout
/app/user/status/login
[GET]
/app/challenges/list - list all challenges available
/app/challenge/1/checklist
/app/challenge/1/checklist/performance

Heroku Kubectl Client (securethebox-server)
[GET] 
/heroku/status/uptime - Get uptime status of Heroku Server (need this to deploy)
/heroku/status/resources - Get cpu/memory load

Google Kubernetes Engine 
[GET]
/kubernetes/status/clusters/uptime - Get all cluster uptime
/kubernetes/status/pods/uptime - Get all pod uptime
/kubernetes/status/resources - Get cpu/memory load
/kubernetes/status/zones - Get Regional clusters available
/kubernetes/status/dns - Get External-DNS status/records

Firebase Metrics
[GET]
/users/metrics/loggedin - How many users are logged in
/users/metrics/joined/24hours - How many users joined today
/usses/metrics/challenges - How many users are doing a challenge
- Collection: users
- Document: metrics

Stripe client
[POST] 
/stripe/subscription/start - Subscribe user via email address + CC (Should also send invoice)
- args=emailaddress,jwt
[GET] 
/stripe/invoice - Get invoice for frontend (save to Firebase storage)
- args=emailaddress,jwt
[GET] 
/stripe/subscription/status - Check user subscription (save to Firebase firestore)
- args=emailaddress,jwt
Sendgrid client