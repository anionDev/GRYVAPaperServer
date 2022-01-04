# GRYVAPaperServer

## Purpose

Represents a [Paper](https://papermc.io/)-server.

## Version

The Paper-version in the latest image is v1.18.1.

## Usage

### Volumes

Using volumes is recommended to preserve data. The available folder for a volume is:

- `/Workspace/Shared/Configuration`: This folder contains all configurations of the hosted server.
- `/Workspace/Shared/Data`: This folder contains all stored world-data the hosted server.
- `/Workspace/Shared/Logs`: This folder contains all log-files of the hosted server.

### Environment-variables

There are currently no environment-variables available.

### Example

See `docker-compose.example.yml` for an example how to use this image.

### Build image

The image can be built using the following command:

``` sh
docker image build --force-rm --progress plain --build-arg EnvironmentStage=Development --tag gryvapaperserver:latest .
```

The image can also be built using the following command which uses no cache:

``` sh
docker image build --no-cache --pull --force-rm --progress plain --build-arg EnvironmentStage=Development --tag gryvapaperserver:latest .
```

The environment-stage can have the one of the following values:

- `Development`
- `QualityManagement`
- `Productive`

### Test image

The built image can be tested using the following command:

``` sh
docker-compose -f docker-compose.example.yml -p GRYVAPaperServer up --remove-orphans --force-recreate
```

After executing this command the first time your container may terminate and you may see an `eula.txt`-file in the `./Volumes/Configuration`-folder. You have to edit this file accordingly to indicate that you accept the end-user license agreement and execute the command again to run the application. Now the container will remain running and uses your world-data stored in `./Volumes/Data` or creates a new world in this folder if the folder is empty.

## Development

### Branching-system

This repository applies the [GitFlowSimplified](https://projects.aniondev.de/CommonUtilities/Templates/ProjectTemplates/-/blob/main/Templates/Conventions/BranchingSystem/GitFlowSimplified.md)-branching-system.
