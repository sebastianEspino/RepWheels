FROM python:3.10.12

# Set the working directory in the container
WORKDIR /TallerRW

# Copy the application files into the working directory
COPY . /TallerRW

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


