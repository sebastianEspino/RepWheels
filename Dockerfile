FROM python:3.10.12


# Copy the application files into the working directory
COPY . /TallerRW

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

