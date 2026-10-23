# Health API — Deployment Runbook

## Prerequisites
- Docker Engine or Docker Desktop with Compose
- Project repository available on the deployment host
- Required environment variables configured securely
- Host port 8000 available

## Deploy or update
1. Review the code changes and Git commit.
2. Verify required environment configuration.
3. Validate Compose configuration with `docker compose config --quiet`.
4. Build the application image with `docker compose build`.
5. Start or update services with `docker compose up -d`.
6. Check service status with `docker compose ps`.
7. Test `/health` and `/health/db`.
8. Review application logs for errors.

## Troubleshooting
- Inspect service status and recent logs.
- Check API-to-database hostname and credentials.
- Check whether the published host port is available.
- Confirm MySQL is healthy before diagnosing application-level database errors.
- Never delete database volumes as a routine troubleshooting step.

## Data protection
- Back up MySQL data before risky changes.
- Test restoration from backups.
- Keep secrets out of Git and container images.
- Do not use `docker compose down -v` unless volume deletion is intentional and approved.

## Rollback
- Identify the last known-good application image or Git revision.
- Restore the previous version using the deployment process.
- Verify API health and database connectivity.
- Check logs and record the cause of the incident.

## Post-deployment checks
- API responds successfully.
- Database health check passes.
- Persistent data remains available.
- Logs contain no unexpected errors.
