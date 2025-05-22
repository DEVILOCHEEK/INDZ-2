import subprocess
import json
from typing import List

def check_cluster_health():
    print("=== Cluster health check ===")
    subprocess.run(['kubectl', 'get', 'nodes'])
    
    print("\n=== Resource usage ===")
    subprocess.run(['kubectl', 'top', 'nodes'])
    subprocess.run(['kubectl', 'top', 'pods', '-A'])
    
    print("\n=== Checking critical pods ===")
    critical_pods = ["prometheus", "grafana", "ingress-nginx"]
    for pod in critical_pods:
        subprocess.run(['kubectl', 'get', 'pods', '-A', '|', 'grep', pod])

def get_failed_pods() -> List[str]:
    result = subprocess.run(
        ['kubectl', 'get', 'pods', '-A', '-o', 'json'],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    
    return [
        f"{item['metadata']['namespace']}/{item['metadata']['name']}"
        for item in data['items']
        if item['status']['phase'] not in ('Running', 'Succeeded')
    ]

if __name__ == "__main__":
    check_cluster_health()
    failed = get_failed_pods()
    if failed:
        print(f"\n⚠️ Failed pods: {', '.join(failed)}")
        exit(1)
