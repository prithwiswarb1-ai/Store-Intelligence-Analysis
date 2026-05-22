import streamlit as st
import requests
import time

API_URL = "http://api:8000"
#API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st.title("Store Intelligence Dashboard")

placeholder = st.empty()

while True:

    try:

        metrics_response = requests.get(
            f"{API_URL}/stores/STORE_BLR_001/metrics"
        )

        anomalies_response = requests.get(
            f"{API_URL}/stores/STORE_BLR_001/anomalies"
        )

        funnel_response = requests.get(
            f"{API_URL}/stores/STORE_BLR_001/funnel"
        )

        metrics = metrics_response.json()
        anomalies = anomalies_response.json()
        funnel = funnel_response.json()

        with placeholder.container():

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Unique Visitors",
                metrics["unique_visitors"]
            )

            col2.metric(
                "Conversion Rate",
                metrics["conversion_rate"]
            )

            col3.metric(
                "Average Dwell",
                metrics["avg_dwell_ms"]
            )

            st.subheader("Funnel")

            st.json(funnel)

            st.subheader("Anomalies")

            st.json(anomalies)

        time.sleep(5)

    except Exception as e:

        st.error(str(e))

        time.sleep(5)