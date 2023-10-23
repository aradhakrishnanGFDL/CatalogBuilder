FROM continuumio/miniconda3

WORKDIR /app

COPY . catalogbuilder
# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml --name catalogbuilder

# Make RUN commands use the new environment:
RUN echo "conda activate catalogbuilder" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# The code to run when container is started:
ENTRYPOINT ["./entrypoint.sh"]

