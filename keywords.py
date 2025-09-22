import csv

# Adding list of keywords into a list
with open("unique_keyword_list.csv", newline="") as f:
    reader = csv.reader(f)
    keyword_list = [row[0] for row in reader]

# opening the files needed for the comparision
job_description = open("job_desc.txt", "r").read()
resume = open("resume.txt", "r").read()

# print(job_description)
# print(resume)

# List to hold matched keywords
job_description_keywords = []

# Finding Job Description Keywords
for keyword in keyword_list:
    if keyword in job_description:
        job_description_keywords.append(keyword)

# List to hold matched keywords
resume_matched_keywords = []

# Finding Resume Keywords
for keyword in keyword_list:
    if keyword in resume:
        resume_matched_keywords.append(keyword)


# Keywords in job description AND resume
keywords_in_both = list(set(job_description_keywords) & set(resume_matched_keywords))

# Keywords in job description AND NOT in resume
keywords_to_add_to_resume = list(
    set(job_description_keywords) - set(resume_matched_keywords)
)

# Keywords in resume AND NOT in job description
keywords_resume_only = list(
    set(resume_matched_keywords) - set(job_description_keywords)
)


# Sorting the lists
job_description_keywords = sorted(job_description_keywords)
resume_matched_keywords = sorted(resume_matched_keywords)
keywords_in_both = sorted(keywords_in_both)
keywords_to_add_to_resume = sorted(keywords_to_add_to_resume)
keywords_resume_only = sorted(keywords_resume_only)


# Create a function to write all the lists to a file
def writing_func(filename, string, keyword_list):
    with open(filename, "a") as file:
        file.write(string + ": \n")
        file.write(str(len(keyword_list)))
        file.write("\n\n")
        for keyword in keyword_list:
            file.write(keyword + "\n")
        file.write("\n\n")


# Giving the resume a score
percentage = str(len(keywords_in_both) / len(job_description_keywords) * 100)

get_to_70 = (len(job_description_keywords) * 0.7) - len(keywords_in_both)

# Creating a new REPORT file, and Adding the Percentage score to the top
file = open("Report.txt", "w")
file.write("Resume Score with this Job Description:\n\n")
file.write(percentage)
file.write("%\n\n")
file.write("Add ")
file.write(str(get_to_70))
file.write(" to get to 70%\n\n")
file.close()

# Writing all the lists to a file called REPORT.TXT
writing_func(
    "REPORT.txt",
    "Keywords to Add to Resume ERGO Keywords in Job Description ONLY",
    keywords_to_add_to_resume,
)
writing_func(
    "REPORT.txt", "Keywords in Both Job Description AND Resume", keywords_in_both
)
writing_func("REPORT.txt", "Keywords in Job Description", job_description_keywords)
writing_func("REPORT.txt", "Keywords in Resume", resume_matched_keywords)
writing_func(
    "REPORT.txt",
    "Keywords in Resume ONLY ERGO Keywords not in Job Description",
    keywords_resume_only,
)
