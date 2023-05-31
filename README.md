# Kogito Serverless Workflow - Knative Python Example

## Description

This example contains a simple workflow service that illustrate consecutive invocation of two knative python function calls.
The first function  initialize a tensor of the specified size with random content using torch and return its contents.
The second performs an addition of all the element returned by the previous step using numpy library. 

## Installing and Running

### Prerequisites
 
You will need:
  - Java 11+ installed
  - Maven 3.8.6+ installed
  - Docker
  - Minikube
  - Knative CLI

### Compile and Deploy Knative function test

Open a terminal, go to test directory and type

```
kn func build
```

Once it finished, make sure minikube is running with knative profile activated (if you have setup it before, you just need to start minikube with `minikube start -p profile` and configure the tunnel running `minikube tunnel --profile knative`)

Once minikube is running, to load the image from your local docker into minikube registry type in a terminal

```
minikube image load dev.local/test -p knative
```

Now run that image as a knative service called test

```
kn service create test --image=dev.local/test --pull-policy=IfNotPresent
```

### Compile and Deploy Knative function receiver

Open a terminal, go to test directory and type

```
kn func build
```

Once it finished, make sure minikube is running with knative profile activated (if you have setup it before, you just need to start minikube with `minikube start -p profile` and configure the tunnel running `minikube tunnel --profile knative`)

Once minikube is running, to load the image from your local docker into minikube registry type in a terminal

```
minikube image load dev.local/receiver -p knative
```

Now run that image as a knative service called receiver

```
kn service create receiver --image=dev.local/receiver --pull-policy=IfNotPresent
```

### Run Serverless Workflow

Open a terminal, go to workflow directory and run

```
mvn clean package
```

In some terminals, you need to ensure the local image is loaded into minikube by running

`minikube image load dev.local/serverless-workflow-knative-python-quarkus:1.0-SNAPSHOT -p knative`

and update the service accordingly 

`kn service update serverless-workflow-knative-python-quarkus  --image=dev.local/serverless-workflow-knative-python-quarkus:1.0-SNAPSHOT --pull-policy=IfNotPresent` 

Once done, your workflow service should be available in knative, you need to find out the uri

```
 kn service list | grep serverless-workflow-knative-python-quarkus
 ```
The URI of the service  will be the one in the second column
 
To invoke the flow, you need to execute the following REST invocation, replacing the uri by the one resolved in the previous step and specifying the x and y dimension of the tensor. 

```
curl -X POST -H 'Content-Type:application/json' -H 'Accept:application/json' -d '{"x":3,"y":3}' <uri>/TensorTest
```
The result is a float number with the sum of the randomly generated matrix.
 
```
{"id":"e80c8f2f-3753-45f0-b477-15812a3fe982","workflowdata":6.1767255663871765}
```
