library(RCurl)
url <- "http://taipei.youbike.com.tw/cht/f12.php"
htmlSource = getURL(url, .encoding = 'utf-8')
library(stringr)
encodedJson = str_match(htmlSource, "*/\r\n\t\\w*='(.*)';\\w*=JSON.parse")[2]
json = URLdecode(encodedJson)
library(rjson)
jsonData = fromJSON(json)
newData <- data.frame(matrix(unlist(jsonData), nrow=length(jsonData), byrow=T))
colnames(newData) <- c('id', 'name', 'district', 'address', 'total', 
                       'available', 'empty', 'lat', 'lon', 'time', 'status', 
                       'available_img', 'empty_img')
dataPath = strftime(Sys.time(), 'data-%Y%m%d.rda')
if (file.exists(dataPath)) {
  load(dataPath)  
  data = rbind(data, newData)
} else {
  data = newData
}
save(data, file=dataPath)
