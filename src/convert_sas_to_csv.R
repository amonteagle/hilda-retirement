library(haven)

# Function to convert SAS files into csv
convert_all_sas_to_csv <- function(input_dir, output_dir, row_names = TRUE) {
  
  # List all .sas7bdat files in the input directory
  sas_files <- list.files(path = input_dir, pattern = "\\.sas7bdat$", full.names = TRUE)
  
  # Ensure output directory exists
  if (!dir.exists(output_dir)) {
    dir.create(output_dir, recursive = TRUE)
  }
  
  for (file_path in sas_files) {
    # Extract filename only
    file_name <- basename(file_path)
    
    # Read SAS file
    data <- read_sas(file_path)
    
    # Construct CSV filename
    csv_name <- sub("\\.sas7bdat$", ".csv", file_name)
    output_file <- file.path(output_dir, csv_name)
    
    # Write CSV
    write.csv(data, file = output_file, row.names = row_names)
    
    cat("✔ Converted:", file_name, "→", csv_name, "\n")
  }
}


# Define your input and output paths
input_path <- "your-input-folder"
output_path <- "your-output-folder"

convert_all_sas_to_csv(input_path, output_path)

