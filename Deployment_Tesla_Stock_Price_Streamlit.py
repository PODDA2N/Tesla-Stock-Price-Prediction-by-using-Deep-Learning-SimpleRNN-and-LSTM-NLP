#!/usr/bin/env python
# coding: utf-8

# # Deployment of Tesla Stock Price Prediction using Streamlit

# In[ ]:


import streamlit as st
import joblib


# #### Streamlit Title

# In[ ]:


st.title(
    "Tesla Stock Price Prediction"
)

st.write(
    "LSTM-based Tesla Stock Forecasting"
)


# #### Upload Tesla Dataset

# In[ ]:


uploaded_file = st.file_uploader(
    "TSLA",
    type=["csv"]
)


# #### Read Dataset

# In[ ]:


if uploaded_file:

    data = pd.read_csv(
        uploaded_file
    )

    st.write(
        "Dataset Preview"
    )

    st.dataframe(
        data.head()
    )


# #### Data Visualization

# In[ ]:


fig, ax = plt.subplots(
    figsize=(10,5)
)

ax.plot(
    data["Adj Close"]
)

ax.set_title(
    "Tesla Adjusted Close Price"
)

st.pyplot(fig)


# #### Volume Trend

# In[ ]:


fig, ax = plt.subplots(
    figsize=(10,5)
)

ax.plot(
    data["Volume"]
)

ax.set_title(
    "Trading Volume"
)

st.pyplot(fig)


# #### Preprocessing

# In[ ]:


features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]

X = data[features]

X_scaled = feature_scaler.transform(X)


# #### Create Sequences

# In[ ]:


window_size = 60

X_test = []


# In[ ]:


for i in range(
    window_size,
    len(X_scaled)
):

    X_test.append(
        X_scaled[
            i-window_size:i
        ]
    )

X_test = np.array(
    X_test
)


# #### Predict

# In[ ]:


predictions = model.predict(
    X_test
)


# In[ ]:


predictions = (
    target_scaler
    .inverse_transform(
        predictions
    )
)


# #### Actual Values

# In[ ]:


actual = data[
    ["Adj Close"]
].values[
    window_size:
]


# #### Compare Actual vs Predicted

# In[ ]:


fig, ax = plt.subplots(
    figsize=(12,6)
)

ax.plot(
    actual,
    label="Actual"
)

ax.plot(
    predictions,
    label="Predicted"
)

ax.legend()

ax.set_title(
    "Actual vs Predicted Tesla Prices"
)

st.pyplot(fig)


# #### Calculate MSE

# In[ ]:


from sklearn.metrics import (
    mean_squared_error
)

mse = mean_squared_error(
    actual,
    predictions
)

st.metric(
    "Mean Squared Error",
    round(mse,4)
)


# #### Display Prediction Table

# In[ ]:


result_data = pd.DataFrame({

    "Actual":
    actual.flatten(),

    "Predicted":
    predictions.flatten()

})

st.dataframe(
    result_data.tail(20)
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




