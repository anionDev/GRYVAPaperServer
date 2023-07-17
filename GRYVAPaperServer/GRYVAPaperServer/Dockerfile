FROM openjdk:21-jdk

ARG TargetEnvironmentType
ARG Version="0.1.7"
LABEL maintainer "marius.goecke@gmail.com"
LABEL description="GRYVAPaperServer is a docker-image for simply running a Paper-server in a docker-container."
LABEL targetEnvironmentType="$TargetEnvironmentType"
LABEL version="$Version"

RUN mkdir /Workspace \
    && mkdir /Workspace/Application \
    && mkdir /Workspace/Configuration \
    && mkdir /Workspace/Data \
    && useradd --base-dir /Workspace --home /Workspace user

# TODO redirect logs and crash-reports to /Workspace/Logs-folder

COPY ./GRYVAPaperServer/EntryPointScript.sh /Workspace/Application/EntryPointScript.sh
COPY ./Other/Resources/PaperServer/PaperServer.jar /Workspace/Application/PaperServer.jar

RUN chown -R user:user /Workspace \
    && chmod -R 700 /Workspace

USER user
WORKDIR /Workspace/Configuration

ENTRYPOINT ["/Workspace/Application/EntryPointScript.sh"]
