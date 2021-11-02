## YouTube Practice


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from pandas import DataFrame

import folium
from folium import plugins

%matplotlib inline

```

## Reading Data from a Database w/o header


```python
import requests
import secrets

url = 'https://api.covid19api.com/dayone/country/south-africa'

r = requests.get(url)

r.status_code

```




    200




```python
data = r.json()
```


```python
from pandas import DataFrame
df = DataFrame(data)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Country</th>
      <th>CountryCode</th>
      <th>Province</th>
      <th>City</th>
      <th>CityCode</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>603</th>
      <td>019d03f4-b8c8-4580-b010-ff1dd9707052</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2921589</td>
      <td>89151</td>
      <td>0</td>
      <td>2832438</td>
      <td>2021-10-29T00:00:00Z</td>
    </tr>
    <tr>
      <th>604</th>
      <td>a08b41e8-80f3-4d50-bbc3-ae615757da66</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2921886</td>
      <td>89163</td>
      <td>0</td>
      <td>2832723</td>
      <td>2021-10-30T00:00:00Z</td>
    </tr>
    <tr>
      <th>605</th>
      <td>8dc0e271-f619-43cc-a2c2-6918e2be1c65</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2922116</td>
      <td>89177</td>
      <td>0</td>
      <td>2832939</td>
      <td>2021-10-31T00:00:00Z</td>
    </tr>
    <tr>
      <th>606</th>
      <td>7d28a70d-d331-4a99-96ac-17953877ebe7</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2922222</td>
      <td>89179</td>
      <td>0</td>
      <td>2833043</td>
      <td>2021-11-01T00:00:00Z</td>
    </tr>
    <tr>
      <th>607</th>
      <td>212cfe09-cb24-441a-988b-2826e5161a17</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2922222</td>
      <td>89179</td>
      <td>0</td>
      <td>2833043</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
  </tbody>
</table>
</div>



### Reading from API with Header


```python
url = "https://api.covid19api.com/dayone/country/south-africa"
payload={}
headers = {
    'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'
}
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
df = DataFrame(data)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Country</th>
      <th>CountryCode</th>
      <th>Province</th>
      <th>City</th>
      <th>CityCode</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>603</th>
      <td>019d03f4-b8c8-4580-b010-ff1dd9707052</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2921589</td>
      <td>89151</td>
      <td>0</td>
      <td>2832438</td>
      <td>2021-10-29T00:00:00Z</td>
    </tr>
    <tr>
      <th>604</th>
      <td>a08b41e8-80f3-4d50-bbc3-ae615757da66</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2921886</td>
      <td>89163</td>
      <td>0</td>
      <td>2832723</td>
      <td>2021-10-30T00:00:00Z</td>
    </tr>
    <tr>
      <th>605</th>
      <td>8dc0e271-f619-43cc-a2c2-6918e2be1c65</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2922116</td>
      <td>89177</td>
      <td>0</td>
      <td>2832939</td>
      <td>2021-10-31T00:00:00Z</td>
    </tr>
    <tr>
      <th>606</th>
      <td>7d28a70d-d331-4a99-96ac-17953877ebe7</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2922222</td>
      <td>89179</td>
      <td>0</td>
      <td>2833043</td>
      <td>2021-11-01T00:00:00Z</td>
    </tr>
    <tr>
      <th>607</th>
      <td>212cfe09-cb24-441a-988b-2826e5161a17</td>
      <td>South Africa</td>
      <td>ZA</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-30.56</td>
      <td>22.94</td>
      <td>2922222</td>
      <td>89179</td>
      <td>0</td>
      <td>2833043</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
  </tbody>
</table>
</div>




```python
url = "https://api.covid19api.com/dayone/country/philippines"
payload={}
headers = {
    'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'
}
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
df = DataFrame(data)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Country</th>
      <th>CountryCode</th>
      <th>Province</th>
      <th>City</th>
      <th>CityCode</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>638</th>
      <td>dc80184f-3bcf-4500-9cef-e541c00152c5</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2779943</td>
      <td>42621</td>
      <td>0</td>
      <td>2737322</td>
      <td>2021-10-29T00:00:00Z</td>
    </tr>
    <tr>
      <th>639</th>
      <td>bc489855-59ea-4e1f-b292-6df106bc4ceb</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2783896</td>
      <td>43044</td>
      <td>0</td>
      <td>2740852</td>
      <td>2021-10-30T00:00:00Z</td>
    </tr>
    <tr>
      <th>640</th>
      <td>41cbb455-c858-4500-ab59-9cd350e27021</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2787276</td>
      <td>43172</td>
      <td>0</td>
      <td>2744104</td>
      <td>2021-10-31T00:00:00Z</td>
    </tr>
    <tr>
      <th>641</th>
      <td>91d4b7e4-9c07-4c06-90e4-cb9e8f00979a</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2790375</td>
      <td>43276</td>
      <td>0</td>
      <td>2747099</td>
      <td>2021-11-01T00:00:00Z</td>
    </tr>
    <tr>
      <th>642</th>
      <td>f29d94ee-772c-4ddf-8f28-00738b83217d</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2790375</td>
      <td>43276</td>
      <td>0</td>
      <td>2747099</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
  </tbody>
</table>
</div>



### Function to Generate Latest Active Cases per Country



```python
def countryData(country):
    url1 = "https://api.covid19api.com/dayone/country/"
    country = country
    url = url1+country
    payload={}
    headers = {'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    df = DataFrame(data)
    return df.tail(1)
```


```python
data = countryData("philippines")
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Country</th>
      <th>CountryCode</th>
      <th>Province</th>
      <th>City</th>
      <th>CityCode</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>642</th>
      <td>f29d94ee-772c-4ddf-8f28-00738b83217d</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2790375</td>
      <td>43276</td>
      <td>0</td>
      <td>2747099</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
  </tbody>
</table>
</div>



### Summary of All Countries


```python
url = "https://api.covid19api.com/countries"
payload={}
headers = {
    'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'
}
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
df = DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Slug</th>
      <th>ISO2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bhutan</td>
      <td>bhutan</td>
      <td>BT</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fiji</td>
      <td>fiji</td>
      <td>FJ</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cayman Islands</td>
      <td>cayman-islands</td>
      <td>KY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>China</td>
      <td>china</td>
      <td>CN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Micronesia, Federated States of</td>
      <td>micronesia</td>
      <td>FM</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>243</th>
      <td>Namibia</td>
      <td>namibia</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>244</th>
      <td>South Sudan</td>
      <td>south-sudan</td>
      <td>SS</td>
    </tr>
    <tr>
      <th>245</th>
      <td>Bulgaria</td>
      <td>bulgaria</td>
      <td>BG</td>
    </tr>
    <tr>
      <th>246</th>
      <td>Gibraltar</td>
      <td>gibraltar</td>
      <td>GI</td>
    </tr>
    <tr>
      <th>247</th>
      <td>Morocco</td>
      <td>morocco</td>
      <td>MA</td>
    </tr>
  </tbody>
</table>
<p>248 rows × 3 columns</p>
</div>




```python
df.to_csv('country.csv')
```

### Latest Per Asian Country


```python
seCountries = ["brunei","myanmar","cambodia","timor-leste","indonesia","malaysia", 
               "philippines","singapore","thailand","vietnam"]
```


```python
def latestCountry(country):
    url1 = "https://api.covid19api.com/dayone/country/"
    country = country
    url = url1+country
    payload={}
    headers = {'X-Access-Token': 'a3c98472-2928-4752-9d71-083ce072213c'}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    df = DataFrame(data)
    return df.tail(1)
```


```python
dataSE = []

for country in seCountries:
    df = latestCountry(country)
    columns = list(df)
    values = df.iloc[0]
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    dataSE.append(a_dictionary)
```


```python

dataSE = DataFrame(dataSE).sort_values('Country')
dataSE
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Country</th>
      <th>CountryCode</th>
      <th>Province</th>
      <th>City</th>
      <th>CityCode</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>dfaca950-73b8-4df4-9842-432348675b59</td>
      <td>Brunei Darussalam</td>
      <td>BN</td>
      <td></td>
      <td></td>
      <td></td>
      <td>4.54</td>
      <td>114.73</td>
      <td>13246</td>
      <td>89</td>
      <td>0</td>
      <td>13157</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>2</th>
      <td>77a7ae46-8a39-4cee-bd82-5e75d9d7a9fa</td>
      <td>Cambodia</td>
      <td>KH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.57</td>
      <td>104.99</td>
      <td>118613</td>
      <td>2794</td>
      <td>0</td>
      <td>115819</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c6c4745f-1e47-4b14-a7f8-024067fe0bb9</td>
      <td>Indonesia</td>
      <td>ID</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.79</td>
      <td>113.92</td>
      <td>4244761</td>
      <td>143423</td>
      <td>0</td>
      <td>4101338</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ef69aece-f0a7-4742-b695-8af784c41e08</td>
      <td>Malaysia</td>
      <td>MY</td>
      <td></td>
      <td></td>
      <td></td>
      <td>4.21</td>
      <td>101.98</td>
      <td>2476268</td>
      <td>28975</td>
      <td>0</td>
      <td>2447293</td>
      <td>2021-11-01T00:00:00Z</td>
    </tr>
    <tr>
      <th>1</th>
      <td>e7a58b63-027d-4f87-b723-269c4b24ee78</td>
      <td>Myanmar</td>
      <td>MM</td>
      <td></td>
      <td></td>
      <td></td>
      <td>21.91</td>
      <td>95.96</td>
      <td>500950</td>
      <td>18714</td>
      <td>0</td>
      <td>482236</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f29d94ee-772c-4ddf-8f28-00738b83217d</td>
      <td>Philippines</td>
      <td>PH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>12.88</td>
      <td>121.77</td>
      <td>2790375</td>
      <td>43276</td>
      <td>0</td>
      <td>2747099</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d4df3f63-cd83-405f-8b9e-69e9a69aeeaf</td>
      <td>Singapore</td>
      <td>SG</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.35</td>
      <td>103.82</td>
      <td>200844</td>
      <td>421</td>
      <td>0</td>
      <td>200423</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>8</th>
      <td>b7448370-1c77-4ede-8777-adf7b579aca7</td>
      <td>Thailand</td>
      <td>TH</td>
      <td></td>
      <td></td>
      <td></td>
      <td>15.87</td>
      <td>100.99</td>
      <td>1920189</td>
      <td>19260</td>
      <td>0</td>
      <td>1900929</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4de47d32-b09d-4192-b741-d2dc890ddfff</td>
      <td>Timor-Leste</td>
      <td>TL</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-8.87</td>
      <td>125.73</td>
      <td>19790</td>
      <td>122</td>
      <td>0</td>
      <td>19668</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
    <tr>
      <th>9</th>
      <td>04cc8abb-d404-4808-b95e-71cdd814f19f</td>
      <td>Viet Nam</td>
      <td>VN</td>
      <td></td>
      <td></td>
      <td></td>
      <td>14.06</td>
      <td>108.28</td>
      <td>926720</td>
      <td>22135</td>
      <td>0</td>
      <td>904585</td>
      <td>2021-11-02T00:00:00Z</td>
    </tr>
  </tbody>
</table>
</div>




```python
#how to select columns and highlight dataframe using gradient background
dataFilter = dataSE[['Country','Confirmed','Deaths', 'Active']].sort_values('Confirmed', ascending=False).reset_index(drop=True)
dataFilter.style.background_gradient(cmap='Reds')

```




<style  type="text/css" >
#T_aab74_row0_col1,#T_aab74_row0_col2,#T_aab74_row0_col3{
            background-color:  #67000d;
            color:  #f1f1f1;
        }#T_aab74_row1_col1{
            background-color:  #e53228;
            color:  #f1f1f1;
        }#T_aab74_row1_col2{
            background-color:  #fcaa8d;
            color:  #000000;
        }#T_aab74_row1_col3{
            background-color:  #e22e27;
            color:  #f1f1f1;
        }#T_aab74_row2_col1{
            background-color:  #f34a36;
            color:  #000000;
        }#T_aab74_row2_col2{
            background-color:  #fdcab5;
            color:  #000000;
        }#T_aab74_row2_col3{
            background-color:  #f24633;
            color:  #000000;
        }#T_aab74_row3_col1{
            background-color:  #fb7a5a;
            color:  #000000;
        }#T_aab74_row3_col2{
            background-color:  #fedecf;
            color:  #000000;
        }#T_aab74_row3_col3{
            background-color:  #fb7656;
            color:  #000000;
        }#T_aab74_row4_col1,#T_aab74_row4_col3{
            background-color:  #fdc5ae;
            color:  #000000;
        }#T_aab74_row4_col2{
            background-color:  #fed8c7;
            color:  #000000;
        }#T_aab74_row5_col1,#T_aab74_row5_col3{
            background-color:  #fee2d5;
            color:  #000000;
        }#T_aab74_row5_col2{
            background-color:  #fedfd0;
            color:  #000000;
        }#T_aab74_row6_col1,#T_aab74_row6_col3{
            background-color:  #ffeee6;
            color:  #000000;
        }#T_aab74_row6_col2,#T_aab74_row8_col1,#T_aab74_row8_col2,#T_aab74_row8_col3,#T_aab74_row9_col1,#T_aab74_row9_col2,#T_aab74_row9_col3{
            background-color:  #fff5f0;
            color:  #000000;
        }#T_aab74_row7_col1,#T_aab74_row7_col3{
            background-color:  #fff1ea;
            color:  #000000;
        }#T_aab74_row7_col2{
            background-color:  #fff2ec;
            color:  #000000;
        }</style><table id="T_aab74_" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Country</th>        <th class="col_heading level0 col1" >Confirmed</th>        <th class="col_heading level0 col2" >Deaths</th>        <th class="col_heading level0 col3" >Active</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_aab74_level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_aab74_row0_col0" class="data row0 col0" >Indonesia</td>
                        <td id="T_aab74_row0_col1" class="data row0 col1" >4244761</td>
                        <td id="T_aab74_row0_col2" class="data row0 col2" >143423</td>
                        <td id="T_aab74_row0_col3" class="data row0 col3" >4101338</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_aab74_row1_col0" class="data row1 col0" >Philippines</td>
                        <td id="T_aab74_row1_col1" class="data row1 col1" >2790375</td>
                        <td id="T_aab74_row1_col2" class="data row1 col2" >43276</td>
                        <td id="T_aab74_row1_col3" class="data row1 col3" >2747099</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_aab74_row2_col0" class="data row2 col0" >Malaysia</td>
                        <td id="T_aab74_row2_col1" class="data row2 col1" >2476268</td>
                        <td id="T_aab74_row2_col2" class="data row2 col2" >28975</td>
                        <td id="T_aab74_row2_col3" class="data row2 col3" >2447293</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_aab74_row3_col0" class="data row3 col0" >Thailand</td>
                        <td id="T_aab74_row3_col1" class="data row3 col1" >1920189</td>
                        <td id="T_aab74_row3_col2" class="data row3 col2" >19260</td>
                        <td id="T_aab74_row3_col3" class="data row3 col3" >1900929</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_aab74_row4_col0" class="data row4 col0" >Viet Nam</td>
                        <td id="T_aab74_row4_col1" class="data row4 col1" >926720</td>
                        <td id="T_aab74_row4_col2" class="data row4 col2" >22135</td>
                        <td id="T_aab74_row4_col3" class="data row4 col3" >904585</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_aab74_row5_col0" class="data row5 col0" >Myanmar</td>
                        <td id="T_aab74_row5_col1" class="data row5 col1" >500950</td>
                        <td id="T_aab74_row5_col2" class="data row5 col2" >18714</td>
                        <td id="T_aab74_row5_col3" class="data row5 col3" >482236</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_aab74_row6_col0" class="data row6 col0" >Singapore</td>
                        <td id="T_aab74_row6_col1" class="data row6 col1" >200844</td>
                        <td id="T_aab74_row6_col2" class="data row6 col2" >421</td>
                        <td id="T_aab74_row6_col3" class="data row6 col3" >200423</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row7" class="row_heading level0 row7" >7</th>
                        <td id="T_aab74_row7_col0" class="data row7 col0" >Cambodia</td>
                        <td id="T_aab74_row7_col1" class="data row7 col1" >118613</td>
                        <td id="T_aab74_row7_col2" class="data row7 col2" >2794</td>
                        <td id="T_aab74_row7_col3" class="data row7 col3" >115819</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row8" class="row_heading level0 row8" >8</th>
                        <td id="T_aab74_row8_col0" class="data row8 col0" >Timor-Leste</td>
                        <td id="T_aab74_row8_col1" class="data row8 col1" >19790</td>
                        <td id="T_aab74_row8_col2" class="data row8 col2" >122</td>
                        <td id="T_aab74_row8_col3" class="data row8 col3" >19668</td>
            </tr>
            <tr>
                        <th id="T_aab74_level0_row9" class="row_heading level0 row9" >9</th>
                        <td id="T_aab74_row9_col0" class="data row9 col0" >Brunei Darussalam</td>
                        <td id="T_aab74_row9_col1" class="data row9 col1" >13246</td>
                        <td id="T_aab74_row9_col2" class="data row9 col2" >89</td>
                        <td id="T_aab74_row9_col3" class="data row9 col3" >13157</td>
            </tr>
    </tbody></table>




```python
map = folium.Map(location=[15,100], zoom_start=4, tiles='Stamenterrain')

for lat, lon, value, name in zip(dataSE['Lat'],dataSE['Lon'],dataSE['Active'],dataSE['Country']):
    folium.CircleMarker([lat, lon],radius=value*0.8, popup=(str(name).capitalize())).add_to(map)

map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=%3C%21DOCTYPE%20html%3E%0A%3Chead%3E%20%20%20%20%0A%20%20%20%20%3Cmeta%20http-equiv%3D%22content-type%22%20content%3D%22text/html%3B%20charset%3DUTF-8%22%20/%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%3Cscript%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20L_NO_TOUCH%20%3D%20false%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20L_DISABLE_3D%20%3D%20false%3B%0A%20%20%20%20%20%20%20%20%3C/script%3E%0A%20%20%20%20%0A%20%20%20%20%3Cstyle%3Ehtml%2C%20body%20%7Bwidth%3A%20100%25%3Bheight%3A%20100%25%3Bmargin%3A%200%3Bpadding%3A%200%3B%7D%3C/style%3E%0A%20%20%20%20%3Cstyle%3E%23map%20%7Bposition%3Aabsolute%3Btop%3A0%3Bbottom%3A0%3Bright%3A0%3Bleft%3A0%3B%7D%3C/style%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//cdn.jsdelivr.net/npm/leaflet%401.6.0/dist/leaflet.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//code.jquery.com/jquery-1.12.4.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js%22%3E%3C/script%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdn.jsdelivr.net/npm/leaflet%401.6.0/dist/leaflet.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css%22/%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cmeta%20name%3D%22viewport%22%20content%3D%22width%3Ddevice-width%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20initial-scale%3D1.0%2C%20maximum-scale%3D1.0%2C%20user-scalable%3Dno%22%20/%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cstyle%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23map_4acac45fce1b491eb3785e4b4e33187c%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20position%3A%20relative%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20width%3A%20100.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20height%3A%20100.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%3A%200.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20top%3A%200.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C/style%3E%0A%20%20%20%20%20%20%20%20%0A%3C/head%3E%0A%3Cbody%3E%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22folium-map%22%20id%3D%22map_4acac45fce1b491eb3785e4b4e33187c%22%20%3E%3C/div%3E%0A%20%20%20%20%20%20%20%20%0A%3C/body%3E%0A%3Cscript%3E%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20map_4acac45fce1b491eb3785e4b4e33187c%20%3D%20L.map%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22map_4acac45fce1b491eb3785e4b4e33187c%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20center%3A%20%5B15.0%2C%20100.0%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20crs%3A%20L.CRS.EPSG3857%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20zoom%3A%204%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20zoomControl%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20preferCanvas%3A%20false%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20tile_layer_963039c285e641d483a6dc17e29acfe2%20%3D%20L.tileLayer%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22https%3A//stamen-tiles-%7Bs%7D.a.ssl.fastly.net/terrain/%7Bz%7D/%7Bx%7D/%7By%7D.jpg%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22attribution%22%3A%20%22Map%20tiles%20by%20%5Cu003ca%20href%3D%5C%22http%3A//stamen.com%5C%22%5Cu003eStamen%20Design%5Cu003c/a%5Cu003e%2C%20under%20%5Cu003ca%20href%3D%5C%22http%3A//creativecommons.org/licenses/by/3.0%5C%22%5Cu003eCC%20BY%203.0%5Cu003c/a%5Cu003e.%20Data%20by%20%5Cu0026copy%3B%20%5Cu003ca%20href%3D%5C%22http%3A//openstreetmap.org%5C%22%5Cu003eOpenStreetMap%5Cu003c/a%5Cu003e%2C%20under%20%5Cu003ca%20href%3D%5C%22http%3A//creativecommons.org/licenses/by-sa/3.0%5C%22%5Cu003eCC%20BY%20SA%5Cu003c/a%5Cu003e.%22%2C%20%22detectRetina%22%3A%20false%2C%20%22maxNativeZoom%22%3A%2018%2C%20%22maxZoom%22%3A%2018%2C%20%22minZoom%22%3A%200%2C%20%22noWrap%22%3A%20false%2C%20%22opacity%22%3A%201%2C%20%22subdomains%22%3A%20%22abc%22%2C%20%22tms%22%3A%20false%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_4bc14196f9db40f2ad50b27abb86437c%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B4.54%2C%20114.73%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%2010525.6%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_85df3bf77403471f93aa5e78009d6621%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_9e60636117d542eea6bb9a8cb81c9dec%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_9e60636117d542eea6bb9a8cb81c9dec%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBrunei%20darussalam%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_85df3bf77403471f93aa5e78009d6621.setContent%28html_9e60636117d542eea6bb9a8cb81c9dec%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_4bc14196f9db40f2ad50b27abb86437c.bindPopup%28popup_85df3bf77403471f93aa5e78009d6621%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_57eb24ae7d494a09b5a8913e3ece35c5%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B12.57%2C%20104.99%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%2092655.20000000001%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_7261f38243144f159faef939a56f6267%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_874f68aa674f41ef85a941a116816f90%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_874f68aa674f41ef85a941a116816f90%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECambodia%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_7261f38243144f159faef939a56f6267.setContent%28html_874f68aa674f41ef85a941a116816f90%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_57eb24ae7d494a09b5a8913e3ece35c5.bindPopup%28popup_7261f38243144f159faef939a56f6267%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_bea20bd3c0eb4942a2c3eff47718b963%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B-0.79%2C%20113.92%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%203281070.4000000004%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_2947e2bced31444796f0b37706e44b33%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_85cf4fc66d85441db2d7b2c979282fe9%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_85cf4fc66d85441db2d7b2c979282fe9%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EIndonesia%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_2947e2bced31444796f0b37706e44b33.setContent%28html_85cf4fc66d85441db2d7b2c979282fe9%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_bea20bd3c0eb4942a2c3eff47718b963.bindPopup%28popup_2947e2bced31444796f0b37706e44b33%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_612d8bcfe30d4515ab1ee5caba1e00ad%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B4.21%2C%20101.98%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%201957834.4000000001%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_0fd6bb2493d74a25bcf52b6bae085ae9%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_01215dceaa134cf1a3f2f4be87154d11%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_01215dceaa134cf1a3f2f4be87154d11%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMalaysia%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_0fd6bb2493d74a25bcf52b6bae085ae9.setContent%28html_01215dceaa134cf1a3f2f4be87154d11%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_612d8bcfe30d4515ab1ee5caba1e00ad.bindPopup%28popup_0fd6bb2493d74a25bcf52b6bae085ae9%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_b7d4a8950a824c48b41f01ae103a9c9d%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B21.91%2C%2095.96%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%20385788.80000000005%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_7a9711a8cd91406a8bc51950e2c6e6be%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_5d7a026309564505beb7854cbaf6c17b%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_5d7a026309564505beb7854cbaf6c17b%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMyanmar%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_7a9711a8cd91406a8bc51950e2c6e6be.setContent%28html_5d7a026309564505beb7854cbaf6c17b%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_b7d4a8950a824c48b41f01ae103a9c9d.bindPopup%28popup_7a9711a8cd91406a8bc51950e2c6e6be%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_c598d4c3f15a442c8c858a21452c2fa9%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B12.88%2C%20121.77%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%202197679.2%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_029fe034df1740f9ad10f3d5d84d0325%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_95a7bb4ec60b4450945df1b03b93c467%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_95a7bb4ec60b4450945df1b03b93c467%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EPhilippines%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_029fe034df1740f9ad10f3d5d84d0325.setContent%28html_95a7bb4ec60b4450945df1b03b93c467%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_c598d4c3f15a442c8c858a21452c2fa9.bindPopup%28popup_029fe034df1740f9ad10f3d5d84d0325%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_cad55c0ff1f54544b76b43d0b585ef07%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B1.35%2C%20103.82%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%20160338.40000000002%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_16fcfee0c127487ba9e74208666c384a%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_1e5fc86de52c4598b4d63f008ad07a01%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_1e5fc86de52c4598b4d63f008ad07a01%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ESingapore%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_16fcfee0c127487ba9e74208666c384a.setContent%28html_1e5fc86de52c4598b4d63f008ad07a01%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_cad55c0ff1f54544b76b43d0b585ef07.bindPopup%28popup_16fcfee0c127487ba9e74208666c384a%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_a157162ae0a443989cbc307113448eb7%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B15.87%2C%20100.99%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%201520743.2000000002%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_6250a700db7d49c3a5c116037ca5a304%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_a57e7fc48461475c995167795b2d1762%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_a57e7fc48461475c995167795b2d1762%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EThailand%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_6250a700db7d49c3a5c116037ca5a304.setContent%28html_a57e7fc48461475c995167795b2d1762%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_a157162ae0a443989cbc307113448eb7.bindPopup%28popup_6250a700db7d49c3a5c116037ca5a304%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_053086206bfa4293b5510c5eaa588d38%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B-8.87%2C%20125.73%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%2015734.400000000001%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_b8233ecfa9cb45d9bf9230ca6e8eb0e1%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_544c59a67e434be1aa132a6ebbe31b36%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_544c59a67e434be1aa132a6ebbe31b36%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ETimor-leste%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_b8233ecfa9cb45d9bf9230ca6e8eb0e1.setContent%28html_544c59a67e434be1aa132a6ebbe31b36%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_053086206bfa4293b5510c5eaa588d38.bindPopup%28popup_b8233ecfa9cb45d9bf9230ca6e8eb0e1%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_81c3fe912888472bade8a66dd293bcf4%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B14.06%2C%20108.28%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%22bubblingMouseEvents%22%3A%20true%2C%20%22color%22%3A%20%22%233388ff%22%2C%20%22dashArray%22%3A%20null%2C%20%22dashOffset%22%3A%20null%2C%20%22fill%22%3A%20false%2C%20%22fillColor%22%3A%20%22%233388ff%22%2C%20%22fillOpacity%22%3A%200.2%2C%20%22fillRule%22%3A%20%22evenodd%22%2C%20%22lineCap%22%3A%20%22round%22%2C%20%22lineJoin%22%3A%20%22round%22%2C%20%22opacity%22%3A%201.0%2C%20%22radius%22%3A%20723668.0%2C%20%22stroke%22%3A%20true%2C%20%22weight%22%3A%203%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_4acac45fce1b491eb3785e4b4e33187c%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20var%20popup_272f515c31c4467aa24d93c5ebe776fe%20%3D%20L.popup%28%7B%22maxWidth%22%3A%20%22100%25%22%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20html_214463801bc24beea83b6c0e471979e4%20%3D%20%24%28%60%3Cdiv%20id%3D%22html_214463801bc24beea83b6c0e471979e4%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EViet%20nam%3C/div%3E%60%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20popup_272f515c31c4467aa24d93c5ebe776fe.setContent%28html_214463801bc24beea83b6c0e471979e4%29%3B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20circle_marker_81c3fe912888472bade8a66dd293bcf4.bindPopup%28popup_272f515c31c4467aa24d93c5ebe776fe%29%0A%20%20%20%20%20%20%20%20%3B%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%3C/script%3E onload="this.contentDocument.open();this.contentDocument.write(    decodeURIComponent(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python

```
