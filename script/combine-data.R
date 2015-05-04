dataDirPath = './data'
if (exists('totalData')) {
  remove(totalData)
}
library(stringr)
for (file in list.files(dataDirPath, full.names = T, 
                        pattern = '^data-\\d{8}\\.rda$')) {
  load(file)
  if (exists('totalData')) {
    totalData = rbind(totalData, data)
  } else {
    totalData = data;
  }
  remove(data)
}
data = totalData
remove(totalData)
save(data, file=paste0(dataDirPath, '/data.rda'))
