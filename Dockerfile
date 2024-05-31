# Base image
FROM python:3.12.2

# Working directory
WORKDIR /TallerRW

COPY requirements.txt requirements.txt
# Copy requirements file and install dependencies
RUN echo $"La ruta del archivo es: {pwd}"

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the server port
EXPOSE 8000

# Command to start the server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
