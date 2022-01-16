FROM debian:stable-slim

ARG EnvironmentStage

RUN mkdir /Workspace
WORKDIR /Workspace

RUN apt update
RUN apt install -y git openjdk-17-jre-headless wget iputils-ping

RUN git clone --single-branch --branch main git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ./ScriptCollection/Other

RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Debian/Common/CreateUser.sh "user" "/userhome" "false" "" "false" "false"

RUN mkdir /Workspace/Program
RUN mkdir /Workspace/Program/App
RUN mkdir /Workspace/Shared
RUN mkdir /Workspace/Shared/Data
RUN mkdir /Workspace/Shared/Configuration
RUN mkdir /Workspace/Shared/Logs
# TODO redirect logs and crash-reports to log-folder

RUN wget https://papermc.io/api/v2/projects/paper/versions/1.18.1/builds/132/downloads/paper-1.18.1-132.jar --no-verbose --output-document /Workspace/Program/App/server.jar

COPY ./EntryPointScript.sh /Workspace/Program/App/EntryPointScript.sh
RUN chmod +x /Workspace/Program/App/EntryPointScript.sh

RUN chown -R user /Workspace

RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Debian/Common/ConfigureSystem.sh "$EnvironmentStage" "/Workspace/ScriptCollection" "openjdk-17-jre-headless" "/Workspace/ScriptCollection"

WORKDIR /Workspace/Shared/Configuration
USER user

ENTRYPOINT ["/Workspace/Program/App/EntryPointScript.sh"]
