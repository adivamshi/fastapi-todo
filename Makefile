# Build the Docker image
build:
	docker build -t fastapi-server .

# Run the Docker container
run:
	docker run -d -p 8000:8000 fastapi-server

# Stop the Docker container
stop:
	docker stop $$(docker ps -q --filter ancestor=fastapi-server)

# Remove the Docker container
clean:
	docker rm $$(docker ps -aq --filter ancestor=fastapi-server)

# Clean up Docker resources (containers and images)
prune:
	docker system prune --all --force

# Run the test cases
test:
	docker run -v $$(pwd):/app fastapi-server python -m unittest test_server.py

# Set up virtual environment and install dependencies
venv_setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

# Run the FastAPI server
venv_run:
	venv/bin/python server.py

# Run the test cases
venv_test:
	venv/bin/python -m unittest test_server.py

# Clean up virtual environment
venv_clean:
	rm -rf venv
