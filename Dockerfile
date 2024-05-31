FROM python:3.12.2
# Set the working directory in the container
WORKDIR /TallerRW

# Copy the application files into the working directory
COPY . .
# Install the application dependencies
RUN pip install -r requirements.txt



# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
