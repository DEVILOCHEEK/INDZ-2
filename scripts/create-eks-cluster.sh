CLUSTER_NAME="my-eks-cluster"
REGION="us-west-2"
NODEGROUP_NAME="my-nodegroup"

echo "Creating EKS Cluster: $CLUSTER_NAME in region $REGION"

aws eks create-cluster \
  --name $CLUSTER_NAME \
  --region $REGION \
  --kubernetes-version 1.27 \
  --role-arn arn:aws:iam::<AWS_ACCOUNT_ID>:role/EKS-Cluster-Role \
  --resources-vpc-config subnetIds=subnet-abc123,subnet-def456,securityGroupIds=sg-12345678

echo "Creating Node Group: $NODEGROUP_NAME"

aws eks create-nodegroup \
  --cluster-name $CLUSTER_NAME \
  --nodegroup-name $NODEGROUP_NAME \
  --subnets subnet-abc123 subnet-def456 \
  --instance-types t3.medium \
  --scaling-config minSize=2,maxSize=5,desiredSize=3 \
  --disk-size 20 \
  --region $REGION \
  --node-role arn:aws:iam::<AWS_ACCOUNT_ID>:role/EKS-Worker-Node-Role

echo "EKS Cluster and Node Group creation started."
echo "Please wait until cluster is ACTIVE before deploying."
