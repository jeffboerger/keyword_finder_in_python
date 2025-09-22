# Resume Keyword Matcher

A simple Python program that analyzes a job description and your resume against a list of action keywords. It generates a report showing how well your resume aligns with the job description.

---

## How It Works
1. Takes a job description from `job_desc.txt`  
2. Takes your resume from `resume.txt`  
3. Compares both against a predefined list of **action keywords**  
4. Outputs the results to `Report.txt`  

---

## Setup
- Place `keywords.py`, `job_desc.txt`, and `resume.txt` in the same directory.  
- Ensure you have **Python 3.x** installed.  

---

## Usage
1. **Create Job Description File**  
   Copy and paste the job posting into a text file named `job_desc.txt`.  

2. **Create Resume File**  
   Copy and paste your current resume into a text file named `resume.txt`.  

3. **Run the Script**  
   ```bash
   python keywords.py
