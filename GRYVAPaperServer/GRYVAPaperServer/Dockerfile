FROM debian:stable-slim

LABEL maintainer "marius.goecke@gmail.com"
LABEL version="$Version"
LABEL description="GRYVAPaperServer is a docker-image for simply running a Paper-server in a docker-container."
ARG TargetEnvironmentType
ARG Version="0.1.2"

RUN mkdir /Workspace
WORKDIR /Workspace

RUN apt update
RUN apt install -y git openjdk-17-jre-headless wget
#RUN apt install -y git openjdk-19-jre-headless wget

RUN git clone --single-branch --branch main https://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ./ScriptCollection/Other/OtherScripts

RUN /Workspace/ScriptCollection/Other/OtherScripts/ServerMaintenance/Debian/Common/CreateUser.sh "user" "/userhome" "false" "" "false" "false"

RUN mkdir /Workspace/Program
RUN mkdir /Workspace/Configuration
RUN mkdir /Workspace/Logs
# TODO redirect logs and crash-reports to log-folder

RUN wget https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/333/downloads/paper-1.19.3-333.jar --no-verbose --output-document /Workspace/Program/server.jar

COPY ./EntryPointScript.sh /Workspace/Program/EntryPointScript.sh
RUN chmod +x /Workspace/Program/EntryPointScript.sh

RUN chown -R user /Workspace

RUN /Workspace/ScriptCollection/Other/OtherScripts/ServerMaintenance/Debian/Common/ConfigureSystem.sh "$TargetEnvironmentType" "/Workspace/ScriptCollection" "openjdk-17-jre-headless" "/Workspace/ScriptCollection"
#RUN /Workspace/ScriptCollection/Other/OtherScripts/ServerMaintenance/Debian/Common/ConfigureSystem.sh "$TargetEnvironmentType" "/Workspace/ScriptCollection" "openjdk-19-jre-headless" "/Workspace/ScriptCollection"

WORKDIR /Workspace/Configuration
USER user

ENTRYPOINT ["/Workspace/Program/EntryPointScript.sh"]
