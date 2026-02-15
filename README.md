# Task Manager

This is a small educational microservices project used to practice CI/CD pipelines and GitHub Actions.

Services
- api — Python (Flask). Contains unit tests and a Dockerfile.
- archiver — Java (Maven). Includes unit tests and a Dockerfile.
- frontend — Static web app (HTML/JS) served by Nginx.
- monitor — Go service with unit tests and a Dockerfile.

Purpose
- Serve as a training repository for building GitHub Actions workflows that run tests, build Docker images, and push them to a container registry.

CI / CD
- Workflows live in `.github/workflows/` and run per-service pipelines (test + build + push).
- The repository is configured to push images to Docker Hub under the `iltodbul` namespace; CI expects two repository secrets:
	- `DOCKERHUB_USERNAME` — your Docker Hub username
	- `DOCKERHUB_TOKEN` — a Docker Hub access token (recommended) or password

Local development
- api:
	- Install dependencies: `pip install -r services/api/requirements.txt`
	- Run tests: `python3 -m pytest services/api/tests/test_app.py`
- archiver:
	- Run tests: `cd services/archiver && ./mvnw test`
- monitor:
	- Run tests: `cd services/monitor && go test ./...`

Notes
- Tests are (mostly) mocked for CI purposes; Redis is an external dependency for the project and may be required when running the full stack locally.
- To publish images from CI, add the Docker Hub secrets in GitHub: Settings → Secrets and variables → Actions → New repository secret.
