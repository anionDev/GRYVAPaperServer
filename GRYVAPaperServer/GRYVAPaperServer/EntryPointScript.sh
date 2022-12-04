#!/bin/bash

if [ ! -f /Workspace/Configuration/.gitignore ]; then
    touch /Workspace/Configuration/.gitignore
    echo "cache" >> /Workspace/Configuration/.gitignore
    echo "libraries" >> /Workspace/Configuration/.gitignore
    echo "versions" >> /Workspace/Configuration/.gitignore
fi

command="java -Xms$java_xms -Xmx$java_xmx -jar /Workspace/Program/server.jar --nogui --universe /Workspace/Data"

echo "Run '$command'..."
bash -c "$command"
