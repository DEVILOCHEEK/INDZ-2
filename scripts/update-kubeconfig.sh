CLUSTER_NAME="my-eks-cluster"
REGION="us-west-2"

echo "Updating kubeconfig for cluster $CLUSTER_NAME..."

aws eks update-kubeconfig --name $CLUSTER_NAME --region $REGION

echo "kubeconfig updated."
