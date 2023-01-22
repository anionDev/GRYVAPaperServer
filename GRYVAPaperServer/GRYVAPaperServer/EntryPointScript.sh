#!/bin/bash
echo "start server"
whoami

if [ ! -f /Workspace/Configuration/.gitignore ]; then
    touch /Workspace/Configuration/.gitignore
    echo "cache" >> /Workspace/Configuration/.gitignore
    echo "libraries" >> /Workspace/Configuration/.gitignore
    echo "versions" >> /Workspace/Configuration/.gitignore
fi

command="java -jar /Workspace/Application/PaperServer.jar --nogui --universe /Workspace/Data"
#command="java -Xms$java_xms -Xmx$java_xmx -jar /Workspace/Application/PaperServer.jar --nogui --universe /Workspace/Data"

echo "Run '$command'..."
bash -c "$command"
