# Notes



**Helm**
<https://medium.com/@geraldcroes/kubernetes-traefik-101-when-simplicity-matters-957eeede2cf8>
*Helm is a package manager for Kube and, for me, the most convenient way to configure Traefik without messing it up.*
```
brew install kubernetes-helm
helm init
helm install stable/traefik --set dashboard.enabled=true,dashboard.domain=traefik.securethebox.us
helm ls --all --short | xargs -L1 helm delete
```



**Create Project**
Enable Kubernetes Engine API

**Console**
<https://console.cloud.google.com/kubernetes/list?project=securethebox>

**Tasks**

**DNS Control**
https://github.com/kubernetes-incubator/external-dns/blob/master/docs/tutorials/cloudflare.md

**Traefik Setup**
<https://docs.traefik.io/configuration/backends/kubernetes/>


**Kubernetes Vocab**
nodeport = global port
port = container port
svc = loadbalancer

**Commands**
```
kubectl get nodes
kubectl apply -f k8s_file.yml
kubectl get deploy
kubectl get pods -o wide
kubectl exec -it root k8s_node_name /bin/sh
kubectl get svc --watch
```

**Creating user**
```
openssl x509 -req -in _username_.csr
openssl req -new -key _username_.key out _username_.csr -sbj "/CN=_username_/O=_namespace_
kubectl set credentials _username_ client-certificate=/path/to/_username_.crt client-key=/path/to/_username_.key
```
- requires role and rolebinding
**Changing User Context**
```
kubectl config use-context _username_
```
