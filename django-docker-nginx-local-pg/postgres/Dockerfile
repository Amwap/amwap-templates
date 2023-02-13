FROM postgres:14

COPY ./postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
# RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
#     && rm -r /usr/local/bin/maintenance