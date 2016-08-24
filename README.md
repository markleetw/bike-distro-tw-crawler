## Introduction

Rewrite crawler of [bike-distro-tw](https://github.com/marksylee/bike-distro-tw) in Python.

User can easily fetch data from all Taiwan public bike system, including YouBike (Taipei, New Taipei City, Taichung, Changhua County, Taoyuan City, HsinChu City) and CityBike (Kaohsiung).

## Installation

- Download and install the latest [Python 2](https://www.python.org/downloads/).
- Install required packages:
  - `pip install -r requirement.txt`

## How To Use

run `python scripts/fetch_data.py` and get *df.cvs* file

## Data amount of per fetch cycle:
* ####YouBike:
    1. Taipei: *255* stations
    2. NTPC (New Taipei City): *303* stations
    3. Taichung: *99* stations
    4. chcg (Changhua County Government): *68* stations
    5. tycg (Taoyuan City Government): *34* stations
    6. hccg (HsinChu City Government): *15* stations

* ####CityBike:
    1. kaohsiung: *184* stations

