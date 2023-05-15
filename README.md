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

Once it finished, make sure minikube is running with knative profile activated (if you have setup it before, you just need to start minikube with `minikube start -p profile`) and type

```
minikube image load dev.local/test -p knative
```
to load the image from your local docker into minikube registry

Now run that image as a knative service called test

```
kn service create test --image=dev.local/test --pull-policy=IfNotPresent
```

### Compile and Deploy Knative function receiver

Open a terminal, go to test directory and type

```
kn func build
```

Once it finished, make sure minikube is running with knative profile activated (if you have setup it before, you just need to start minikube with `minikube start -p profile`) and type

```
minikube image load dev.local/receiver -p knative
```
to load the image from your local docker into minikube registry

Now run that image as a knative service called receiver

```
kn service create receiver --image=dev.local/receiver --pull-policy=IfNotPresent
```

### Run Serverless Workflow

Open a terminal, go to workflow diretory and run
```
mvn clean package
```

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
