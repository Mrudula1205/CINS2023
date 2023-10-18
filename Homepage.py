import streamlit as lit


cnis= "CNISLogo.png"
bits="bits-logo.png"
img_1 = "ESL_logo.png"
img_2 = "MTC logo.png"
icon = "icon.jpg"

lit.set_page_config(
    page_title="CINS 2023",
    page_icon=cnis,
)

pages = {
    "CINS 2023": "Welcome To CINS 2023",
    "Day 1 - 18th October": "Day 1 - 18th October",
    "Day 2 - 19th October": "Day 2 - 19th October",
    "Day 3 - 20th October": "Day 3 - 20th October",
    "MTC ESL GenAI Global Summit": "MTC ESL GenAI Global Summit",
}

for page_name, page_title in pages.items():
    if lit.sidebar.button(page_title, key=page_name):
        lit.session_state.page = page_name

page = getattr(lit.session_state, "page", list(pages.keys())[0])

lit.title(pages[page])

if page == "CINS 2023":
    lit.write("")
    lit.image([cnis,bits], use_column_width=False, width=150)
    lit.write("CINS 2023 is the first international conference which is aimed to address the recent developments in the field of computing, intelligence techniques and networks over the globe. The theme of the event is “Seamless Computing for Next Generation”. The aim of conference is to bring together the academia, industry, and forums working in areas of computing, intelligent techniques and networks. The conference will help to promote and explore innovative and ambitious ideas, trends and future challenges towards seamless computing.")
    lit.markdown("[Click here to find out more about the conference!](https://www.bits-dubai.ac.ae/cins2023/home1.html)")
    col1, col2, col3 = lit.columns([0.11,0.05,1])

# Add content to the columns
    col1.write("Click on")
    col2.image(icon, width=20)
    col3.write("icon to view the schedule")
    lit.write("")
    lit.write("")
    lit.write("")
    lit.success("Venue: Auditorium (G07) unless stated otherwise") 
    lit.write("Keep an eye on this space for further updates!")
    
if page == "Day 1 - 18th October":

    lit.write(" 08:30 AM | Registration")
    lit.write(" 09:30 AM | Opening Remarks")
    with lit.expander("10:00 AM | Keynote Address"):
        lit.markdown(''' ### Dr. Christoph Benzmüller \n\n Chair for AI Systems Engineering, Otto-Friendrich-Universitat Bamberg \n\nFU Berlin, Germany''')
    lit.write(" 11:00 AM | Break")
    lit.write(" 11:15 AM | Generative AI Expo")
    lit.write(" 01:00 PM | Lunch Break")
    lit.write(" 02:30 PM | Paper Presentation (Offline Mode)")
    lit.write(" 04:30 PM | Refreshment")

if page == "Day 2 - 19th October":

    with lit.expander("09:00 AM | Keynote Address"):
        lit.markdown(''' ### Dr. Jyotika Singh \n\n Director of Data Science, Placemaker, USA''')
    with lit.expander("10:00 AM | Intel OneAPI Workshop"):
        lit.markdown(''' ### Dr. Shriram K. Vasudevan \n\n Intel Software Innovator, Intel Coorperation Ltd''')
    lit.write(" 01:00 PM | Lunch Break")
    lit.write(" 02:30 PM | Paper Presentation (Online)")
    lit.success("Venue: TelePresence Room unless stated otherwise") 
    
if page == "Day 3 - 20th October":
    
    with lit.expander("09:00 AM | Cyber & Digital Forensics Workshop"):
        lit.markdown(''' ### Mr. Nikhil Mahadeshwar \n\n CEO, Cyber Secured India''')
    lit.write(" 10:00 AM | Microsoft ESL Global Summit")
    lit.write(" 12:00 PM | Winner Prize Distribution")
    lit.write(" 12:30 PM | Valedictory")
    lit.write(" 01:00 PM | Lunch")
    

if page == "MTC ESL GenAI Global Summit":
    lit.write("")
    lit.image(img_1, use_column_width=False, width=300)
    lit.write("Microsoft Tech Club is organizing the Emirati Sign Language (ESL) Generative AI Summit, which is a part of the International Conference on Computational Intelligence and Network Systems (CINS 2023).")
    lit.write("The summit aims to leverage the capabilities of generative AI to enhance accessibility and communication for the Deaf and hard-of-hearing community in the United Arab Emirates (UAE) through Emirati Sign Language (ESL).")
    lit.markdown("[Click here to know more!](https://www.linkedin.com/company/mtc-esl-generative-ai-global-summit/)")
