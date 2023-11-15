FROM continuumio/miniconda3

WORKDIR /app

COPY . /app/catalogbuilder
COPY entrypoint.sh /app/

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml --name catalogbuilder

ENV PATH="${PATH}:/app/catalogbuilder"

# Make RUN commands use the new environment:
RUN echo "conda activate catalogbuilder" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

CMD ["/bin/bash"]

