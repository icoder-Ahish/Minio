import streamlit as st
import boto3
import pandas as pd
from botocore.client import Config

# Initialize S3 client
s3 = boto3.client('s3',
                  endpoint_url='http://192.168.29.20:9000',
                  # endpoint_url='http://10.0.1.95:9000',
                  aws_access_key_id='minioadmin',
                  aws_secret_access_key='minioadmin',
                  config=Config(signature_version='s3v4'),
                  )

# Get bucket objects list
bucket_name = 'streamlit'
file_name = 'data.csv'

response = s3.get_object(Bucket=bucket_name, Key=file_name)
df = pd.read_csv(response["Body"])

# Display DataFrame in Streamlit app
st.write(df)

# Download the file contents as a string
# file_contents = s3.get_object(Bucket=bucket_name, Key=file_name)['Body'].read().decode('utf-8')
#
# # Display the file contents in Streamlit
# st.write(file_contents)


# bucket_objects = s3.list_objects(Bucket=bucket_name)

# # Display bucket objects list
# for obj in bucket_objects['Contents']:
#     st.write(obj['Key'])
