# streamlit-pd-101

## Use ollama on wsl

If you have issue ollama use only CPU to process LLM

In easy way you can use docker-compose for enable GPU

1. run docker-compose.yaml below

    ```yaml docker-compose.yaml
    version: '3.9'

    networks:
    net:
        driver: bridge

    services:
    ollama:
        volumes:
        - ollama:/root/.ollama
        container_name: ollama
        pull_policy: always
        tty: true
        restart: unless-stopped
        image: ollama/ollama:latest
        ports:
        - 11434:11434
        # command: ollama run llama2
        deploy:
        resources:
            reservations:
            devices:
                - driver: nvidia
                count: 1
                capabilities: [gpu]
        environment:
        - OLLAMA_DEBUG="1"
        - gpus=all

    volumes:
    ollama:
        driver: local
    ```
2. shell to container

    ```shell
    docker exec -it ollama /bin/bash
    ```
3. pull mistral LLM model

    ```shell
    ollama pull mistral
    ```
