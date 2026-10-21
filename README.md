helm repo add argo https://argoproj.github.io/argo-helm      

helm upgrade --install argocd argo/argo-cd -n argocd --create-namespace -f ../argocd/values.yaml   

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d