import subprocess
import argparse
from pathlib import Path

def deploy_to_k8s(app_name, chart_path, namespace, values_file, image_tag):
    helm_cmd = [
        'helm', 'upgrade', '--install', app_name, chart_path,
        '--namespace', namespace,
        '--values', values_file,
        '--set', f'image.tag={image_tag}',
        '--wait',
        '--timeout', '5m'
    ]
    
    try:
        subprocess.run(helm_cmd, check=True)
        print(f"Successfully deployed {app_name} with tag {image_tag}")
        
        # Verify deployment
        subprocess.run(['kubectl', '-n', namespace, 'rollout', 'status', 
                       f'deployment/{app_name}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--app-name', required=True)
    parser.add_argument('--chart-path', required=True)
    parser.add_argument('--namespace', default='default')
    parser.add_argument('--values-file', required=True)
    parser.add_argument('--image-tag', required=True)
    
    args = parser.parse_args()
    deploy_to_k8s(
        args.app_name, args.chart_path, args.namespace,
        args.values_file, args.image_tag
    )
