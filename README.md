# Notes API

## CI/CD

The GitHub Actions workflow in `.github/workflows/docker-ci.yml` runs Django
migration checks and tests for pull requests targeting `main` and for pushes to
`main`. The image is built only after the tests pass. Pull requests run the
tests only; pushes to `main` publish the image to GitHub Container Registry
(GHCR) with a commit-SHA tag and, on the default branch, the `latest` tag.

The published image is named `ghcr.io/madi4-cpu/notes-api`. GHCR may create the
package as private by default, so a deployment server must either authenticate
to GHCR or the package must be made public.

## Deploying the image

Deployment is not automated because the hosting platform and server credentials
have not been configured. In a typical deploy step, the target server pulls the
published image by its commit-SHA tag, applies any required database migrations,
and restarts the application with its production environment variables. Using
the SHA tag makes it possible to roll back to a known image; `latest` is useful
for convenience but is mutable.

To automate this step, choose a deployment target and configure its required
GitHub Actions secrets and environment (for example, SSH credentials for a
server or credentials for a hosting provider). The current Dockerfile starts
Django's development server, so replace that command with a production WSGI or
ASGI server before using this image for a production deployment.
