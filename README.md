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

When using native image compilation, you will also need: 
  - [GraalVm](https://www.graalvm.org/downloads/) 19.3.1+ installed
  - Environment variable GRAALVM_HOME set accordingly
  - Note that GraalVM native image compilation typically requires other packages (glibc-devel, zlib-devel and gcc) to be installed too.  You also need 'native-image' installed in GraalVM (using 'gu install native-image'). Please refer to [GraalVM installation documentation](https://www.graalvm.org/docs/reference-manual/aot-compilation/#prerequisites) for more details.

### Compile and Run in Local Dev Mode

```sh
mvn clean package quarkus:dev
```

### Compile and Run in JVM mode

```sh
mvn clean package 
java -jar target/quarkus-app/quarkus-run.jar
```

or on windows

```sh
mvn clean package
java -jar target\quarkus-app\quarkus-run.jar
```

### Compile and Run using Local Native Image
Note that this requires GRAALVM_HOME to point to a valid GraalVM installation

```sh
mvn clean package -Pnative
```
  
To run the generated native executable, generated in `target/`, execute

```sh
./target/serverless-workflow-knative-python-quarkus-{version}-runner
```

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

Now run that image as a knative service called test

```
kn service create test --image=dev.local/receiver --pull-policy=IfNotPresent
```

### Run Serverless Workflow

To invoke the flow, you need to specify the x and y dimension of the tensor. 

```
curl -X POST -H 'Content-Type:application/json' -H 'Accept:application/json' -d '{"x":3,"y":3}' http://localhost:8080/TensorTest
```
The result is a float number with the sum of the randomly generated matrix.
 
```
{"id":"e80c8f2f-3753-45f0-b477-15812a3fe982","workflowdata":6.1767255663871765}
```
