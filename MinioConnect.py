import streamlit as st
from minio import Minio
from minio.error import ResponseError

# Initialize Minio client
client = Minio(
    "minio_server_url",
    access_key="your_access_key",
    secret_key="your_secret_key",
    secure=False  # Set to True for secure (HTTPS) access
)

# List all the buckets in the Minio server
st.write("### Buckets:")
try:
    buckets = client.list_buckets()
    for bucket in buckets:
        st.write(f"- {bucket.name}")
except ResponseError as err:
    st.error(f"Minio error occurred: {err}")

# List all the objects in a bucket
bucket_name = st.text_input("Enter bucket name:")
if bucket_name:
    st.write(f"### Objects in bucket {bucket_name}:")
    try:
        objects = client.list_objects(bucket_name)
        for obj in objects:
            st.write(f"- {obj.object_name}")
    except ResponseError as err:
        st.error(f"Minio error occurred: {err}")

