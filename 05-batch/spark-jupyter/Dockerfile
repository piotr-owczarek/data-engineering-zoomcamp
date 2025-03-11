# Use Jupyter PySpark Notebook as base
FROM jupyter/pyspark-notebook:latest

# Set environment variables for Spark
ENV SPARK_HOME=/usr/local/spark
ENV HADOOP_CONF_DIR=$SPARK_HOME/conf
ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"

# Install Google Cloud Storage Connector
RUN mkdir -p $SPARK_HOME/jars
ADD https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar $SPARK_HOME/jars/

# Expose Spark UI and Jupyter ports
EXPOSE 4040 8888

# Start Jupyter Notebook with desired settings
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.allow_origin='*'", "--NotebookApp.ip='0.0.0.0'", "--NotebookApp.port=8888"]
