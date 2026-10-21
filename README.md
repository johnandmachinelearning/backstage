helm repo add argo https://argoproj.github.io/argo-helm      

helm upgrade --install argocd argo/argo-cd -n argocd --create-namespace -f ../argocd/values.yaml   

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

## Install ARC

* Install cert manager
```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
```
* Install ARC
```
# REPLACE "v0.25.2" with the version you wish to deploy
kubectl create -f https://github.com/actions/actions-runner-controller/releases/download/v0.25.2/actions-runner-controller.yaml
```

```
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
```