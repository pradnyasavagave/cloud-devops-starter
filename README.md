# Cloud DevOps Starter: Flask + Docker + GitHub Actions

A beginner-friendly portfolio project that demonstrates a small Python web application, containerization with Docker, automated tests, and continuous integration using GitHub Actions.

## What this project demonstrates

- **Python + Flask:** a tiny web application.
- **Health endpoint:** `/health` returns a JSON health status.
- **Automated tests:** checks the homepage and health endpoint.
- **Docker:** packages the app into a container.
- **GitHub Actions CI:** runs tests automatically on pushes and pull requests to `main`.

> This starter includes continuous integration (CI). It does not automatically deploy to a cloud server yet.

## Project structure

```text
cloud-devops-starter/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_app.py
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.12 or newer
- Git
- A GitHub account
- Docker Desktop (optional, only for the Docker steps)

You can run and test the app with Python without Docker.

## 1. Run locally on Windows

Open Command Prompt or PowerShell and change directory to the project folder:

```powershell
cd path\to\cloud-devops-starter
```

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate it in **Command Prompt**:

```bat
.venv\Scripts\activate.bat
```

Or activate it in **PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of its execution policy, use Command Prompt instead, or run the app with the virtual environment's Python directly.

Install dependencies and start the app:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open these addresses in your browser:

- Homepage: http://127.0.0.1:5000
- Health check: http://127.0.0.1:5000/health

Stop the server with `Ctrl+C`.

## 2. Run the automated tests

With the virtual environment activated, run:

```powershell
python -m unittest discover -s tests -v
```

You should see two tests pass. If the tests pass locally, the same test command is used by the GitHub Actions workflow.

## 3. Build and run with Docker (optional)

Make sure Docker Desktop is installed and running. From the project root:

```powershell
docker build -t cloud-devops-starter .
docker run --rm -p 5000:5000 cloud-devops-starter
```

Open http://127.0.0.1:5000 and http://127.0.0.1:5000/health.

To stop the container, press `Ctrl+C`.

## 4. Upload the project to GitHub

### Create a repository

1. Sign in to GitHub.
2. Select **New repository**.
3. Enter `cloud-devops-starter` as the repository name.
4. Add a short description such as: `Flask app containerized with Docker and tested automatically using GitHub Actions`.
5. Choose **Public** if you want recruiters to view it.
6. Create the repository. If you already have this local project, do not initialize the GitHub repository with another README.

### Push from your computer

Run these commands inside the project folder. Replace `YOUR-USERNAME` with your GitHub username.

```powershell
git init
git add .
git commit -m "Initial commit: Cloud DevOps Starter"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cloud-devops-starter.git
git push -u origin main
```

If Git says that `origin` already exists, use:

```powershell
git remote set-url origin https://github.com/YOUR-USERNAME/cloud-devops-starter.git
git push -u origin main
```

Git may ask you to sign in through a browser or credential manager.

## 5. Check the GitHub Actions workflow

1. Open your repository on GitHub.
2. Select the **Actions** tab.
3. Open the **Python CI** workflow.
4. Confirm that the latest run is green.
5. If it fails, open the run and read the failed step's log.

The workflow runs for pushes to `main` and pull requests targeting `main`.

## 6. Suggested screenshots for your project post

Capture screenshots of:
1. The app homepage in your browser.
2. The `/health` JSON response.
3. The successful test output in your terminal.
4. The Docker build/run output, if you used Docker.
5. The green **Python CI** run in GitHub Actions.

Do not include passwords, access tokens, private URLs, or other secrets in screenshots.

## 7. GitHub project description and post

**Repository description:**

> A beginner-friendly DevOps project using Python Flask, Docker, automated unit tests, and GitHub Actions CI.

**Sample LinkedIn/GitHub post:**

> I built a Cloud DevOps Starter project to practice the fundamentals of CI and containerization.
>
> **Tech stack:** Python, Flask, unittest, Docker, Git, GitHub Actions.
>
> The application includes a health-check endpoint, automated tests, a Dockerfile, and a GitHub Actions workflow that runs tests on pushes and pull requests.
>
> This project helped me understand how application code, testing, containers, and CI fit into a practical workflow.
>
> **Next step:** extend the pipeline with container publishing and deployment to a cloud environment.
>
> #DevOps #Docker #Python #GitHubActions #CloudComputing #LearningByBuilding

## Troubleshooting

- **`python` is not recognized:** try `py --version`; install Python from the official Python website if needed.
- **`git` is not recognized:** install Git for Windows, then reopen the terminal.
- **Port 5000 is already in use:** stop the other process using that port, or change the port in `app.py`.
- **Docker command fails:** start Docker Desktop and wait until its engine is running.
- **GitHub Actions fails:** open the workflow run and inspect the first failed step.

## Future improvements

- Publish the Docker image to GitHub Container Registry.
- Add linting with Ruff.
- Deploy the container to AWS.
- Add monitoring and structured application logs.
- Add a deployment workflow after the CI pipeline is reliable.

## License

This project is provided for learning and portfolio use. Add a license file if you want to formally specify reuse permissions.
