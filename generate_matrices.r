# Create a matrix of floats and save to RData
floatmatrix <- matrix(rnorm(1000000), nrow=1000)
save(floatmatrix, file='floatmatrix.RData')

# Convert floatmatrix to a matrix of ints and save to RData
intmatrix <- floatmatrix*1000
mode(intmatrix) <- "integer"
save(intmatrix, file='intmatrix.RData')
