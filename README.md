###Introduction
The goal of the original project [`taipei-city-bike-prediction`](https://github.com/hsu-yc/taipei-city-bike-prediction) is shown below.

> The project aimed to provide a Taipei bike stations overview, to predict the bike availability of a given station at anytime, and to visualize the availability’s trend over a specified period.

In this project, we enhance the function that allows users to fetch data from all Taiwan public bike system, including YouBike (Taipei, New Taipei City, Taichung, Changhua County) and CityBike (Kaohsiung). In addition to provide visual analysis and prediction results, we plan to extend some powerful data analysis applications.

###How to fetch data?
The purpose of [`/script/FetchData.R`](https://github.com/marksylee/TaiwanCityBikePrediction/blob/master/script/FetchBikeData.R) is to crawl current station data of YouBike and CityBike websites.

###Create a schedule for fetching data.
* <h4>Linux:</h4>
<p>You can use the command "`crontab -e`" to edit configuration and make system execute the fetch script automatically. There is a simple configuration example in [`crontab.txt`](https://github.com/marksylee/TaiwanCityBikePrediction/blob/master/crontab.txt).</p>
* <h4>Windows:</h4>
<p>Edit the batch file [`fetchData.bat`](https://github.com/marksylee/TaiwanCityBikePrediction/blob/master/fetchData.bat) to make it compatible to your system, and setup [Task Scheduler of Windows](http://www.7tutorials.com/how-create-task-basic-task-wizard) to execute the batch file.</p>

###Data amount of per fetch cycle:
* ####YouBike:
    1. Taipei: *196* stations
    2. NTPC (New Taipei City): *204* stations (2015/09/25 Updated)
    3. Taichung: *58* stations (2015/09/25 Updated)
    4. chcg (Changhua County Government): *68* stations

* ####CityBike:
    1. kaohsiung: *158* stations
