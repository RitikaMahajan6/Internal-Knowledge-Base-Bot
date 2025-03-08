FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/

# Set the environment variable for Streamlit
ENV STREAMLIT_SERVER_PORT=8501

# Expose the port for Streamlit
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "src/gui/streamlit_app.py"]