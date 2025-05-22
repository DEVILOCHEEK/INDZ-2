import subprocess
import argparse

def create_eks_cluster(name, region, node_type, nodes, nodes_min, nodes_max):
    cmd = [
        'eksctl', 'create', 'cluster',
        '--name', name,
        '--region', region,
        '--nodegroup-name', 'workers',
        '--node-type', node_type,
        '--nodes', str(nodes),
        '--nodes-min', str(nodes_min),
        '--nodes-max', str(nodes_max),
        '--managed'
    ]
    subprocess.run(cmd, check=True)
    
    # Update kubeconfig
    subprocess.run(
        ['aws', 'eks', '--region', region, 'update-kubeconfig', '--name', name],
        check=True
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='my-eks-cluster')
    parser.add_argument('--region', default='us-east-1')
    parser.add_argument('--node-type', default='t3.medium')
    parser.add_argument('--nodes', type=int, default=3)
    parser.add_argument('--nodes-min', type=int, default=1)
    parser.add_argument('--nodes-max', type=int, default=5)
    
    args = parser.parse_args()
    create_eks_cluster(
        args.name, args.region, args.node_type,
        args.nodes, args.nodes_min, args.nodes_max
    )
