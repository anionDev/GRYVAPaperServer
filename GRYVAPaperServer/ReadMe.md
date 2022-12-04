# GRYVAPaperServer

## Development-state

![Development-state](https://img.shields.io/badge/development--state-maintenance%20updates%20only-green)

The underlying [Paper](https://papermc.io)-server will be developed actively.

## Purpose

[GRYVAPaperServer](https://projects.aniondev.de/PublicProjects/GRYVAImages/GRYVAPaperServer) is a docker-image for simply running a [Paper](https://papermc.io)-server in a docker-container.

The latest-release contains Paper v1.19.2.

## Usage

### Volumes

Using volumes is not required. There are 2 optional volumes:

- `/Workspace/Shared/Configuration`
- `/Workspace/Shared/Data`
- `/Workspace/Shared/Logs`

The path in the container for this log-folder is `/var/log/tor`.

### Environment-variables

The following environment-variables are available:

- `java_xms`
- `java_xmx`

None of these environment-variables are required.

### Example

See [`docker-compose.example.yml`](https://projects.aniondev.de/PublicProjects/GRYVAImages/GRYVAPaperServer/-/blob/main/GRYVAPaperServer/Other/Reference/ReferenceContent/Examples/docker-compose.example.yml) for an example how to use this image.

## Development

### Branching-system

This repository applies the [GitFlowSimplified](https://projects.aniondev.de/PublicProjects/Common/ProjectTemplates/-/blob/main/Conventions/BranchingSystem/GitFlowSimplified/GitFlowSimplified.md)-branching-system.

### Repository-structure

This repository applies the [CommonProjectStructure](https://projects.aniondev.de/PublicProjects/Common/ProjectTemplates/-/blob/main/Conventions/RepositoryStructure/CommonProjectStructure/CommonProjectStructure.md)-repository-structure.

## License

See [License.txt](https://projects.aniondev.de/PublicProjects/GRYVAImages/GRYVAPaperServer/-/raw/main/License.txt) for license-information.
