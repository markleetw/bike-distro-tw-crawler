suppressPackageStartupMessages(library(RCurl))
suppressPackageStartupMessages(library(stringr))
suppressPackageStartupMessages(library(rjson))

setwd(gsub("script", "", getwd()))

ubikeUrl <- "http://taipei.youbike.com.tw/cht/f12.php"
location <- c("taipei", "ntpc", "taichung", "chcg")

for(loc in location) {
    crawlUrl <- paste(ubikeUrl, "?loc=", loc, sep = "")
    htmlSource = getURL(crawlUrl, .encoding = 'utf-8')
    encodedJson = str_match(htmlSource, "\\w*='(.*)';\\w*=JSON.parse")[2]
    json = URLdecode(encodedJson)
    jsonData = fromJSON(json)
    newData <- data.frame(matrix(unlist(jsonData), nrow = length(jsonData), 
                                 byrow = T))
    colnames(newData) <- c('id', 'name', 'district', 'address', 'total', 
                           'available', 'empty', 'lat', 'lon', 'time', 'status', 
                           'available_img', 'empty_img')
    dataPath = strftime(Sys.time(), paste('data/', loc, '/data-%Y%m%d.rda', 
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
