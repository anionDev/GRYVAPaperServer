#!/bin/bash

if [ ! -f /Workspace/Shared/Configuration/.gitignore ]; then
    touch /Workspace/Shared/Configuration/.gitignore
    echo "cache" >> /Workspace/Shared/Configuration/.gitignore
    echo "libraries" >> /Workspace/Shared/Configuration/.gitignore
    echo "versions" >> /Workspace/Shared/Configuration/.gitignore
fi

command="java -Xms$java_xms -Xmx$java_xmx -jar /Workspace/Program/App/server.jar --nogui --universe /Workspace/Shared/Data"

echo run "$command"
bash -c "$command"
