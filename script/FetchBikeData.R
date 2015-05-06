# Ignore loading messages to avoid sending mail from linux crontab.
suppressPackageStartupMessages(library(RCurl))
suppressPackageStartupMessages(library(stringr))
suppressPackageStartupMessages(library(rjson))
suppressPackageStartupMessages(library(XML))
suppressPackageStartupMessages(library(plyr))

# If use cmd "Rscript" to call this R file, the working directory will be
# ".../TaiwanCityBikePrediction/scipt", which is incorrect, so add this to
# reset working directory.
setwd(gsub("script", "", getwd()))

# Youbike crawler
# There are only 4 cities have YouBike. 
ubikeUrl <- "http://taipei.youbike.com.tw/cht/f12.php"
location <- c("taipei", "ntpc", "taichung", "chcg")

# The columns, "status", "available_img" and "empty_img", will be removed.
colNames <- c('id', 'name', 'district', 'address', 'total', 
              'available', 'empty', 'lat', 'lon', 'time', 'status', 
              'available_img', 'empty_img')
for(loc in location) {
    crawlUrl <- paste(ubikeUrl, "?loc=", loc, sep = "")
    htmlSource = getURL(crawlUrl, .encoding = 'utf-8')
    encodedJson = str_match(htmlSource, "\\w*='(.*)';\\w*=JSON.parse")[2]
    json = URLdecode(encodedJson)
    jsonData = fromJSON(json)
    newData <- data.frame(matrix(unlist(jsonData), nrow = length(jsonData), 
                                 byrow = T))
    colnames(newData) <- colNames
    dataPath = strftime(Sys.time(), paste('data/', loc, '/%Y%m%d.rda', 
                                          sep = ""))
    dir.create(file.path('data', loc), showWarnings = F)
    if (file.exists(dataPath)) {
        load(dataPath)  
        data = rbind(data, newData[, 1:10])
    } else {
        data = newData[, 1:10]
    }
    save(data, file = dataPath)
}

# CityBike crawler
# Only Kaohsiung
crawlUrl <- "http://www.c-bike.com.tw/xml/stationlistopendata.aspx"
location <- "kaohsiung"
xmlData <- suppressWarnings(readLines(crawlUrl))
testList <- xmlToList(xmlData)$BIKEStation

# StationNum1 is the number of available bikes.
# StationNum2 is the number of empty bike racks.
tagNames <- c("StationID", "StationName", "StationAddress", "StationLat", 
              "StationLon", "StationNums1", "StationNums2")
colNames <- c("id", "name", "address", "total", "available", "empty", "lat", 
              "lon", "time")
newData <- ldply(testList, 
                 function(x) { 
                     data.frame(x[tagNames], as.numeric(x["StationNums1"]) + 
                                    as.numeric(x["StationNums2"]), 
                                format(Sys.time(), "%Y%m%d%H%M%S"))
                     }
                 )[, -1]
newData <- newData[, c(1:3, 8, 6, 7, 4, 5, 9)]
colnames(newData) <- colNames
newData <- newData[order(as.numeric(as.character(newData$id))),]
rownames(newData) <- NULL
dataPath = strftime(Sys.time(), paste('data/', location, '/%Y%m%d.rda', 
                                      sep = ""))
dir.create(file.path('data', location), showWarnings = F)
if (file.exists(dataPath)) {
    load(dataPath)  
    data = rbind(data, newData)
} else {
    data = newData
}
save(data, file = dataPath)