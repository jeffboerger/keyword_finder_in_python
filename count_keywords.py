from collections import Counter
import csv

# Read the job descriptions from a text file
with open("many_job_descriptions.txt", "r", encoding="utf-8") as file:
    job_descriptions = (
        file.read().lower()
    )  # Convert text to lowercase for case-insensitive comparison

# List of keywords to search for
with open("unique_keyword_list.csv", newline="") as f:
    reader = csv.reader(f)
    keywords = [row[0].lower() for row in reader]

# Create a counter to store keyword counts
keyword_counts = Counter()

# Count occurrences of each keyword in the job descriptions
for keyword in keywords:
    count = job_descriptions.count(
        keyword.lower()
    )  # Make the comparison case-insensitive
    if count > 0:
        keyword_counts[keyword] = count

# Sort the keyword counts by count in descending order
sorted_keyword_counts = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

# Write the sorted results to a new text file and print each keyword with its count
with open("keyword_counts.txt", "w", encoding="utf-8") as output_file:
    for keyword, count in sorted_keyword_counts:
        output_file.write(f"{keyword}: {count}\n")
        print(f"{keyword}: {count}")

print("\nKeyword counts have been written to 'keyword_counts.txt'.")
