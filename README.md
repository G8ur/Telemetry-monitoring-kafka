Distributed Event-Driven Architecture with API Telemetry
This repository demonstrates a fully automated, asynchronous microservices pipeline equipped with zero-code API intelligence. It showcases how decoupled services communicate via a message broker, and how distributed tracing automatically tracks an event's lifecycle from an initial HTTP request down to a backend worker.

🏗️ Architecture & Tech Stack
Producer API (Python / FastAPI): A web server that receives incoming HTTP requests and publishes them as asynchronous events.

Message Broker (Redpanda): A lightweight, Kafka-compatible event streaming platform that queues the messages.

Consumer Worker (Python): A backend service that continuously listens to the broker and processes events as they arrive.

API Intelligence (OpenTelemetry & Jaeger): OpenTelemetry automatically injects tracing IDs into the HTTP and Kafka headers. Jaeger provides a visual observability dashboard to track the exact millisecond breakdown of the data flow.

Infrastructure: Orchestrated entirely via Docker Compose for a local, one-click deployment.

📋 Prerequisites
To run this project locally, you only need to have the following installed on your machine:

Docker

Docker Compose

🚀 Setup & Installation
1. Clone the repository


```git clone https://github.com/G8ur/Telemetry-monitoring-kafka.git```  
```cd eda-telemetry-project```

2. Start the infrastructure
Run the following command to download the required images, build the APIs, and spin up the private network:



```docker-compose up --build -d```

Note: The -d flag runs the containers in the background. You can run docker ps to verify that redpanda, jaeger, producer, and consumer are running.

🧪 How to Use the Tool
Once the containers are running, you can interact with the system and visualize the event flow.

Step 1: Trigger an Event
-> Open your web browser and navigate to the Producer API's Swagger documentation: http://localhost:8000/docs

-> Click on the POST /orders/ endpoint to expand it.

-> Click "Try it out".

-> Enter sample data (e.g., order_id: 101, item: "Wireless Keyboard") and click Execute.

-> The API will return a success message indicating the event was published to Redpanda.

Step 2: View the Consumer Logs (Optional)
To verify the consumer successfully received and processed the event in the background, check the container logs:

```docker logs consumer```

You should see a success message containing your event data.

Step 3: Visualize the API Intelligence
This is where the observability comes in. We will track the exact journey of the event you just created.

-> Open the Jaeger UI at: http://localhost:16686

-> Under the Service dropdown on the left sidebar, select producer-api.

-> Click the Find Traces button.

-> Click on the most recent trace in the results.

You will now see a visual waterfall chart proving the end-to-end data flow. It will show the exact latency of the FastAPI request, the time taken to publish the message to Redpanda, and the time taken for the Consumer worker to pull and process that exact message.

🧹 Cleanup
To stop the pipeline and remove the containers, networks, and volumes, run:


```docker-compose down```
