# A Simple Hello World Python Demo with bash

git clone https://github.com/jeffmlpsi/helloworld-demo-python.git
or
git clone git@github.com:jeffmlpsi/helloworld-demo-python.git

## Python Code

This code defines a handler that responds to GET requests with the specified text and starts an HTTP server listening on port 8080. When you run the script, you can access the server at http://localhost:8080 and see the same message as the Python program.

Those commands will start a http server listening on port `8080` 
and if your request `http://localhost:8080` you'll see the following output: 
```shell
❯ curl http://localhost:8080
Output of df -h from running a bash command 
          ##         .
    ## ## ##        ==
 ## ## ## ## ##    ===
/"""""""""""""""""\___/ ===
{                       /  ===-
\______ O           __/
 \    \         __/
  \____\_______/


Hello from Docker!

```

 ## Running the container service

 ```
./run.sh
 ```
 
## Stopping and Removing the container

```
./stop.sh
```
