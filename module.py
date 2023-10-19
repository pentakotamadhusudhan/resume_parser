from pyresparser import ResumeParser
pdf = r"C:\Users\User\Documents\madhu resume v 3.10.2023.pdf"
# Replace 'your_resume.pdf' with the path to your resume file
data = ResumeParser(pdf).get_extracted_data()

# Access the extracted information
print("Name:", data.get('name', 'Not found'))
print("Email:", data.get('email', 'Not found'))
print("Phone:", data.get('mobile_number', 'Not found'))
print("Skills:", data.get('skills', 'Not found'))
print("Education:", data.get('degree', 'Not found'))
print("Experience:", data.get('experience', 'Not found'))
