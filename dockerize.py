import os

# Create the Dockerfile
dockerfile_content = '''
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
'''

with open('Dockerfile', 'w') as dockerfile:
    dockerfile.write(dockerfile_content.strip())

# Create the requirements.txt file
requirements = ['requests']  # Add any additional dependencies
with open('requirements.txt', 'w') as requirements_file:
    requirements_file.write('\n'.join(requirements))

# Build the Docker image
image_name = 'your_image_name'  # Specify your desired image name
os.system(f'docker build -t {image_name} .')

# Run the Docker container
os.system(f'docker run {image_name}')
