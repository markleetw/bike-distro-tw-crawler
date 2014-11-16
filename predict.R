library(forecast)
library('plyr')

source('preprocess-data.R')

datePattern = '%Y%m%d'
dataInWeekdays = data[data$time >= strptime('20141103', datePattern) 
  & data$time < strptime('20141108', datePattern),]

ids = levels(data$id)
ids = ids[ids != '0180']
frequency = 60 * 24

predictionByStationId = list()
for(id in ids){  
  print(id)
  #time series
  xData = dataInWeekdays[dataInWeekdays$id == id,]
  ind_size = length(xData$id)
  five_day_ind = 1:ind_size
  xData.ts = ts(xData$ratio, start=1, frequency=frequency)
  fit = stl(xData.ts, 'periodic')
  #prediction
  pred = as.numeric(forecast(fit, h=frequency)$mean)
  header = xData[1,]
  predictionByStationId[[as.character(id]] = list(
    id=header$id,
    name=header$name,
    district=header$district,
    address=header$address,
    lat=header$lat,
    lon=header$lon,
    ratios=pred
  )
}
save(predictionByStationId, file='predictionByStationId.rda')