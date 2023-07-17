# GRYVAPaperServer

## Development-state

![Development-state](https://img.shields.io/badge/development--state-maintenance%20updates%20only-green)

The underlying [Paper](https://papermc.io)-server will be developed actively.

## Purpose

[GRYVAPaperServer](https://projects.aniondev.de/PublicProjects/GRYVAImages/GRYVAPaperServer) is a docker-image for simply running a [Paper](https://papermc.io)-server in a docker-container.

## Usage

### Volumes

There are 3 volumes-paths:

- `/Workspace/Shared/Configuration`
- `/Workspace/Shared/Data`
- `/Workspace/Shared/Logs`

### Environment-variables

The following environment-variables are available:

- `java_xms`
- `java_xmx`

None of these environment-variables are required.

### Example

See the [minimal example `docker-compose.yml`](https://projects.aniondev.de/PublicProjects/GRYVAImages/GRYVAPaperServer/-/blob/main/GRYVAPaperServer/Other/Examples/MinimalDockerComposeFile/docker-compose.yml) for an example how to use this image.
