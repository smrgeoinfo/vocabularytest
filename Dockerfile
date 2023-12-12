FROM python:3-slim
WORKDIR /app
COPY .github/actions/vocabularies/github_action_main.py .
COPY ./Makefile .
COPY ./tools ./tools
COPY ./src ./src
RUN apt-get update && apt-get install -y make
RUN pip install -r /app/tools/requirements.txt
ENV PYTHONPATH /app
ENTRYPOINT ["/app/github_action_main.py"]

# This is for debugging the Docker image build process, ensures the container stays up
# ENTRYPOINT ["tail", "-f", "/dev/null"]
