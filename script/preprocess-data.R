load('data/data.rda')
data$total = as.integer(as.character(data$total))
data$available = as.integer(as.character(data$available))
data$empty = as.integer(as.character(data$empty))
data$time = strptime(data$time, '%Y%m%d%H%M%S')
data$active_total = data$available + data$empty
data$ratio = data$available / data$active_total