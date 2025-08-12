# Developer Guide

## Setting Up Development Environment
1. Install Python 3.10+ and Docker.
2. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Adding a New LLM
1. Update `src/models/model_manager.py` to load a new model.
2. Test the integration using `tests/test_api.py`.

## Deploying to Kubernetes
1. Build the Docker image:
   ```bash
   docker build -t chatbot-app -f deployment/docker/Dockerfile .
   ```
2. Apply Kubernetes manifests:
   ```bash
   kubectl apply -f deployment/kubernetes/
   ```
