# Base image
FROM python:3.10.12

# Working directory
WORKDIR /TallerRW

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the server port
EXPOSE 8000

# Command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]