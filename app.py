from pathlib import Path
import streamlit as st
from PIL import Image

current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir/"styles"/"main.css"
resume_file=current_dir/"assets"/"chandu_resume.pdf"
profile_pic=current_dir/"assets"/"profile-pic.png"
PAGE_TITLE="Digial CV | Chandrika Amalakanti"
PAGE_ICON=": wave"
NAME="Chandrika Amalakanti"
DESCRIPTION="""
Final Year Computer Science Student |'PICSL' club Joint Secretatry | SIH 2022 GRAND FINALIST
 
"""
EMAIL="chandrika.amalakanti2003@gmail.com"
SOCIAL_MEDIA={
    "LinkedIn":"https://www.linkedin.com/in/chandrikaamalakanti0708",
    "GitHub": "https://github.com/chandu70",
    "PHONE NUMBER":"7032816323"
}
PROJECTS={
    "Student data analysis and performance visualizer application":"",
    "Personal assistant":"https://github.com/chandu70/Personal-Assistant.git",
    "Phone number location detector":"https://github.com/chandu70/NumberLocation.git"
}
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

st.title("Hello There")
with open(css_file) as f:
     st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
    profile_pic=Image.open(profile_pic)
col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",

    )
st.write("📫",EMAIL)
st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
st.write("#")
st.subheader("Experience and Qualifications")
st.write(
    """
    1)Intern at Demy Software   Solutions
    Learned data structures and algorithms ,Web development
    
    2)Intern at One Stop AI: Learned basics of  cyber Security fundamentals
    
    3)Intern at Let’s Grow More:
    Developed basic applications using Html,CSS,ReactJs
    
    """
)
st.write("#")
st.subheader("Skills")
st.write("""
1)HTML

2)JAVASCRIPT

3)BIG DATA  TECHNOLOGIES

4)WORKING WITH DIFFERENT PYTHON FRAMEWORKS

5)SQL
""")
st.write("#")
st.subheader("Projects and Accomplishments")
st.write("---")
for project,link in PROJECTS.items():
    st.write(f"[{project}]({link})")





