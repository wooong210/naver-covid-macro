Check version of ur chrome and download ChromeDriver at [here](https://sites.google.com/chromium.org/driver/downloads?authuser=0)

put downloaded chromedriver to current directory



### HOW TO USE

1. in [this site](https://m.place.naver.com/rest/vaccine?vaccineFilter=used), find **id** and **vaccineOrganizationCode** in developer tools - network - graphql

2. make .env file

3. 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./test.sh
```
