# Load necessary library
if (!requireNamespace("stringi", quietly = TRUE)) {
  install.packages("stringi")
}
library(stringi)

# Function to generate random text
generate_random_text <- function(length) {
  letters <- c(LETTERS, letters, 0:9, strsplit("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~", NULL)[[1]])
  return(paste0(sample(letters, length, replace = TRUE), collapse = ""))
}

# Main function
main <- function() {
  con <- file("test.log", open = "wt")
  on.exit(close(con))
  for (i in 1:100) {  # Generate and log 100 lines of random text
    random_text <- generate_random_text(10)  # Each line has 10 characters
    writeLines(paste(Sys.time(), "-", random_text), con)
  }
}

# Run the main function
main()
