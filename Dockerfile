FROM python:3.13

EXPOSE 5000

# Set the working directory inside the container
WORKDIR /app

# is the requirements.txt is not in the container file the run command will not executed because it will not be able to find the txt file 
COPY requirements.txt .

# by default python puts all the created filles from pip install a system level directory (/usr/local/...) and so binding overwrites the files int the working diretory and does not influence them. in the docker course about docker the npm install for node.js is different because default behavior: npm install installs the dependencies listed in package.json into a node_modules directory inside the working directory so the overwrite here cause problem. so in this case i think we use an anonymous volume with longer path -v /app/something

# Separate COPY requirements.txt Before RUN pip install to leverages Docker's layer caching saving time during subsequent builds If requirements.txt does not change,
# Install dependencies The --no-cache-dir flag prevents pip from storing unnecessary cache files. also execute the run command before copy . . to leverage Docker's layer caching
RUN pip install -r requirements.txt --no-cache-dir

# Copy the rest of the application code
COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]


#docker build -t to_do_app .
#docker run -dp 5000:5000 -w /app -v "$(PWD):/app" to_do_app



