###Introduction
The goal of the original project [`taipei-city-bike-prediction`](https://github.com/hsu-yc/taipei-city-bike-prediction) is shown below.

> The project aimed to provide a Taipei bike stations overview, to predict the bike availability of a given station at anytime, and to visualize the availability’s trend over a specified period.

In this project, we enhance the function that allows users to fetch data from all Taiwan public bike system, including YouBike (Taipei, New Taipei City, Taichung, Changhua County) and CityBike (kaohsiung). In addition to provide visual analysis and prediction results, we plan to extend some powerful data analysis applications.

###How to fetch data?
The purpose of [`/script/FetchData.R`](https://github.com/marksylee/TaiwanCityBikePrediction/blob/master/script/FetchBikeData.R) is to crawl current station data of Youbike and Citybike websites.

###Create a schedule for fetching data?
* <h4>Linux:</h4>
<p>Setup Linux crontab to execute the fetch script. There is a simple example in [`crontab.txt`](https://github.com/marksylee/TaiwanCityBikePrediction/blob/master/crontab.txt).</p>
* <h4>Windows:</h4>
<p>Edit the batch file [`fetchData.bat`](https://github.com/marksylee/TaiwanCityBikePrediction/blob/master/fetchData.bat) to make it compatible to your system, and setup Schedule Tasks of Windows to execute the batch file.</p>

###Data amount of per fetch cycle:
* ####Youbike:
    1. Taipei: *196* stations
    2. NTPC (New Taipei City): *111* stations
    3. Taichung: *43* stations
    4. chcg (Changhua County Government): *68* stations

* ####Citybike:
    1. kaohsiung: *158* stations
