# fluentd/Dockerfile

FROM fluent/fluentd:v1.16-debian-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.3.0"]
RUN ["gem", "install", "fluent-plugin-grok-parser", "--no-document"]
USER fluent


