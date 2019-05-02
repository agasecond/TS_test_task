FROM joyzoursky/python-chromedriver:3.7-selenium

# set display port to avoid crash
ENV DISPLAY=:99
ARG CACHEBUST=1
RUN git clone https://github.com/agassecond/TS_test_task.git
RUN ["/bin/bash", "-c", "cd /TS_test_task"]
RUN python -m venv /TS_test_task
RUN ["/bin/bash", "-c", "source /TS_test_task/bin/activate"]
WORKDIR /TS_test_task/
RUN pip install -r requirements.txt
ENV PATH /TS_test_task/:$PATH
ENTRYPOINT ["behave"]
CMD ["-h"]