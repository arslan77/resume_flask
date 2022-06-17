docker stop flask_test
docker delete flask_test
docker build -t flask_test:v1 .
docker run -p 8888:5000 -d --name flask_test flask_test:v1