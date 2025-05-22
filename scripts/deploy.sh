echo "Deploying application to Kubernetes cluster..."

kubectl apply -f ../k8s/deployment.yaml
kubectl apply -f ../k8s/service.yaml

echo "Deployment complete."
