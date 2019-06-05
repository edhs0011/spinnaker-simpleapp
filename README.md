## A Simple app for Spinnaker and Istio on Kubernetes platform

### Build docker image
```
docker build -t edhs0011/simple-app .
docker push edhs0011/simple-app
```

### Apply the kubernetes manifest for deployment and settings for Istio
```
kubectl apply -f app_v1.yaml
```

### Check pods
```
$ kubectl get po
NAME                                  READY     STATUS    RESTARTS   AGE
simpleapp-baseline-7f7b9bd599-kl26z   2/2       Running   0          9m
```

### Check services
```
$ kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
kubernetes   ClusterIP   10.55.240.1     <none>        443/TCP             1d
simpleapp    ClusterIP   10.55.247.103   <none>        9080/TCP            11m
```

### Check Istio gateway
```
$ kubectl get gateway
NAME                AGE
simpleapp-gateway   12m
```

### Confirm results
```
curl http://34.80.185.62/
Hello World!
```
