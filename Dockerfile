# build the image based on python:3.8-slim-buster image
FROM python:3.8-slim-buster

LABEL Description="APP flask"

# the work directory inside the container
WORKDIR /app

# copy the project artefects into the container under the root directory
COPY . .

#update pip and install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# the command to run once we run the container 
ENTRYPOINT ["./entrypoint.sh"]