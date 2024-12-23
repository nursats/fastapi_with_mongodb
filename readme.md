```markdown
# Messages API

This project implements an asynchronous RESTful API for handling messages. It provides functionality for creating, reading, updating, and deleting messages, while integrating MongoDB for data storage and RabbitMQ for message queuing.

## Features

- **POST /api/messages**: Create a new message and store it in MongoDB. The server generates an `id` and `publish_timestamp`.
- **GET /api/messages/{id}**: Fetch a specific message by its `id`.
- **GET /api/messages**: Fetch a list of messages between two users based on `from_user_id` and `to_user_id`. The messages are returned sorted by the `publish_timestamp` in descending order.
- **PUT /api/messages/{id}**: Update an existing message, keeping the original `publish_timestamp` and adding a new `edit_timestamp`.
- **DELETE /api/messages/{id}**: Delete a message by its `id`.
- **WebSocket**: Establish a WebSocket connection to receive random messages from the database every second.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **MongoDB**: NoSQL database for storing message data.
- **RabbitMQ**: Message broker for queueing and broadcasting messages.
- **aio_pika**: Python library for interacting with RabbitMQ asynchronously.
- **Motor**: Asynchronous MongoDB driver for Python.

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.7+
- Docker (for running RabbitMQ locally)
- MongoDB server (or use a hosted instance)
- RabbitMQ server (or use Docker to run RabbitMQ)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-directory>
```

### 2. Install Dependencies

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install required Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run MongoDB and RabbitMQ Locally (Optional)

If you don’t have a MongoDB or RabbitMQ server running, you can use Docker to run them locally.

#### Running MongoDB (if not already set up):

```bash
docker run -d --name mongodb -p 27017:27017 mongo:latest
```

#### Running RabbitMQ with Management Plugin:

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

- RabbitMQ Management UI is available at `http://localhost:15672/` with default credentials:
  - Username: `guest`
  - Password: `guest`

### 4. Set Environment Variables (Optional)

If you’re using a hosted MongoDB or RabbitMQ, ensure the appropriate connection strings are set in your environment variables.

```bash
export MONGO_URI="mongodb://localhost:27017"
```

### 5. Run the Application

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

The API will be accessible at `http://localhost:8000`.

### 6. Access the WebSocket

To connect to the WebSocket, navigate to:

```
ws://localhost:8000/api/chat
```

The WebSocket will send a random message from the database every second.

