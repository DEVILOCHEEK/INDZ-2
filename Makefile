.PHONY: deploy check test

deploy:
	python scripts/deployment/k8s_deploy.py \
		--app-name my-app \
		--chart-path ./helm-charts/my-app \
		--values-file ./helm-charts/my-app/values-prod.yaml \
		--image-tag latest

check:
	python scripts/monitoring/health_check.py

test:
	pytest tests/

setup-eks:
	python scripts/cluster_management/eks_manager.py \
		--name my-cluster \
		--nodes 3
