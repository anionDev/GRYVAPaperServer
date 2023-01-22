FROM openjdk:21-jdk

ARG TargetEnvironmentType
ARG Version="0.1.2"
LABEL maintainer "marius.goecke@gmail.com"
LABEL version="$Version"
LABEL description="GRYVAPaperServer is a docker-image for simply running a Paper-server in a docker-container."

RUN mkdir /Workspace \
    && mkdir /Workspace/Application \
    && mkdir /Workspace/Configuration \
    && mkdir /Workspace/Data

WORKDIR /Workspace/Configuration

# TODO redirect logs and crash-reports to /Workspace/Logs-folder

COPY ./GRYVAPaperServer/EntryPointScript.sh /Workspace/Application/EntryPointScript.sh
COPY ./Other/Resources/PaperServer/PaperServer.jar /Workspace/Application/PaperServer.jar

RUN chmod 500 /Workspace/Application/EntryPointScript.sh
# && chown -R user /Workspace

# USER user

ENTRYPOINT ["/Workspace/Application/EntryPointScript.sh"]
