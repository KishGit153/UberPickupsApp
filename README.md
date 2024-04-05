# UberPickupsApp

***

## App Description

> This app is an UberPickup app seeing where and how often deliveries are made in specific areas. 
> I  have used streamlit to perform this as a complete beginner.
> Click on the link below to access the app :)

[UberPickUps App](https://kishgit153-uberpickupsapp-uber-pickups-aw5sj5.streamlit.app/ "Google Search")

---
---

## Requiremnts Text File 

> - streamlit
> - pandas
> - numpy

***
***

## Code
--- 

```
st.title("Uber Pickups in NYC")

st.text("This is your hub where you can see where your food is and when it is being collected live")

st.subheader("**Our Pickups**")
st.markdown("---")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)
st.markdown("---")

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


```