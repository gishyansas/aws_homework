# aws_homework
## CI/CD: Deploy to AWS EC2 via GitHub Actions

### Github -> Settings -> Secrets and variables -> Actions - New Repository Secret

В Settings → Secrets and variables → Actions настроены следующие переменные:

- `AWS_ACCESS_KEY_ID` — IAM user Key
- `AWS_SECRET_ACCESS_KEY` — IAM user Secret key
- `AWS_REGION` — eu-north-1
- `EC2_HOST` — public IP/hostname
- `EC2_USER` — SSH-username
- `EC2_SSH_KEY` — SSH-key.

### Workflow

1. I created .github/workflows/deploy.yml
2. GitHub Actions start workflow `deploy.yml (Remote SSH Command)`.