# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first
COPY requirements.txt .

# Install dependencies from requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt     #No Cache
RUN pip install -r requirements.txt    #With Cache


# Copy the rest of the project files into the container
COPY . .

# Set default command
CMD ["python"]
#CMD ["bash"] 

#% For Using Flask directly from DOCKERFILE (Recommended for deployment)
#EXPOSE 5000
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]


# #The Dockerfile is a text file that contains the instructions to build a Docker image. The Dockerfile is used by the  docker build  command to build the Docker image. 
# #The Dockerfile starts with the  FROM  instruction, which specifies the base image to use. In this case, we are using the official Python image from Docker Hub. 
# #The  WORKDIR  instruction sets the working directory in the container. The  COPY  instruction copies the project files into the container. 
# #The  RUN  instruction installs the dependencies from the  requirements.txt  file. The  CMD  instruction sets the default command to run when the container starts. 




# @ DOCKER IMAGE
# Step 3: Build the Docker Image 
# To build the Docker image, run the following command: 
# ! # docker build -t my-python-app-image .
#OR 
# For no cache
# ! # docker build --no-cache -t my-python-app-image .

# @ DOCKER CONTAINER
# The  docker build  command builds the Docker image using the Dockerfile in the current directory. The  -t  flag is used to tag the image with a name. In this case, we are tagging the image with the name  my-python-app . 
# Step 4: Run the Docker Container 
# To run the Docker container, use the following command: 
# ! # docker run -it my-python-app-image
#OR
# ! # docker run -it --rm -v "C:/path/to/project:/app" my-python-app-image bash
# 

#Jupyter Notebook: To run the Jupyter Notebook server in the container, use the following command:
# ! # docker run -it --rm -p 8888:8888 my-python-app-image jupyter notebook --ip
#OR
# ! # docker run -it --rm -p 8888:8888 -v "C:/path/to/project:/app" my-python-app-image bash
# Then, Run Jupyter Notebook if needed by navigating to the desired directory(just like local machine) and manually executing:
# jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
# Then Copy the URL from the terminal and paste it in the browser to access the Jupyter Notebook.
#OR
# ! # docker run -it --rm -v "C:/path/to/project:/app" -p 8888:8888 -p 5000:5000 my-python-app-image bash
# -p 5000:5000 → Maps port 5000 (default Flask port) to your local machine, allowing you to access the Flask app if you run it inside the container.
# Run the Flask using "python app.py" and access the Flask app using http://localhost:5000 in the browser. (NOT RECOMMENDED FOR DEPLOYMENT)
# For debugging purposes (auto-reload, etc.), you can run the Flask app in container bash using:
# Ensure you're in the right directory
# ! # export FLASK_APP=app.py       # Set the Flask entry point
# ! # export FLASK_ENV=development  # Enable auto-reload & debugging
# ! # flask run --host=0.0.0.0 --port=5000  # Start the Flask development server
#OR
# DEPLOYMENT FRIENDLY Flask App (Mentioned at the top segment of the Dockerfile)







# The  docker run  command starts a new container from the Docker image. The  -it  flag is used to run the container in interactive mode. The name of the Docker image is specified at the end of the command. 
# docker run → Runs a new container.
# -it → Runs the container interactively with a terminal.
# --rm → Automatically removes the container when it stops (to keep things clean).
# -v "C:/path/to/project:/app" → Mounts your local project folder to /app inside the container, so changes persist.
# -p 8888:8888 → Maps port 8888 of the container to port 8888 on your local machine (useful if you run Jupyter).
#my-python-app-image → The name of your Docker image.
#bash → Opens a Bash shell inside the container.


