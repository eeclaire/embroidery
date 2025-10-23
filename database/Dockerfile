FROM postgres
ENV POSTGRES_DB embroidery
ENV POSTGRES_PASSWORD docker
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432