# RabbitMQ example
## A very simple example of using RabbitMQ is one sender and one receiver.

1. Make sure you have created a virtual environment and copy the repository:
```bash
git clone https://github.com/Dark16V/RabbitMQ-example.git
```
2. Navigate to the project directory:
```bash
cd ./RabbitMQ-example
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Run Docker Compose for RabbitMQ:
```bash
docker-compose up -d
```
5. Go to http://localhost:15672 and log in to access the admin panel
6. Run the file consumer.py to start listening for messages:
```bash
python ./consumer.py | python3 ./consumer.py
```
7. Then run the file producer.py to send a message:
```bash
python ./producer.py | python3 producer.py
```
Do all of this in different terminals
To stop docker, enter docker-compose down in the terminal:
```bash
docker-compose down
```
