#!/bin/bash

# Define the path to the content directory
content_dir="./content"

# Get the current date and time in the desired format
current_date_time=$(date +"%m/%d/%Y %H:%M")

# Find the highest log number from existing files in the content directory
log_prefix="mnist-sae("
log_suffix=").md"
latest_log_num=0

for file in "$content_dir"/*"$log_suffix"; do
    if [[ $file == "$content_dir/$log_prefix"* ]]; then
        # Extract the log number from the filename
        log_num=${file#"$content_dir/$log_prefix"}
        log_num=${log_num%"$log_suffix"}
        if [[ $log_num =~ ^[0-9]+$ ]]; then
            if (( log_num > latest_log_num )); then
                latest_log_num=$log_num
            fi
        fi
    fi
done

# Increment the log number for the new file
new_log_num=$((latest_log_num + 1))

# Create the new Markdown file in the content directory
new_file_name="$content_dir/mnist-sae($new_log_num).md"

# Write the header to the new file
{
    echo "Title: MNIST-SAE Log $new_log_num"
    echo "Date: $current_date_time"
    echo "Category: Experiment Logs"
    echo ""
    echo "## Work Done"
    echo ""
    echo "## Confusions"
    echo ""
    echo "## Next Steps"
    echo ""
} > "$new_file_name"

echo "Created file: $new_file_name"
