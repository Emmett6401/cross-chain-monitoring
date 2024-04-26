# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='우송대학교 IT 센터', page_icon=':bar_chart:', layout='wide')

# Outlier warning
# st.warning("""
#     이 프로그램은 [Outlier](https://outlier.streamlit.app/)를 가져와서 만든것이고 더 많은 modern UI/UX in
#     presenting the same set of data.
# """)

# Title
st.title('늘 새로움을 만들다')
st.divider()
# Blockchains
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.image(Image.open('images/arbitrum-logo.png'))
c2.image(Image.open('images/1wsu1.png'))
c3.image(Image.open('images/nostalgia.jpg'))
c4.image(Image.open('images/ethereum-logo.png'))
c5.image(Image.open('images/optimism-logo.png'))
c6.image(Image.open('images/polygon-logo.png'))

# Introduction
st.subheader('커리큘럼')
st.write(
    """
    우송 대학교 에서는 IT교육센터를 운영중에 있다. 여기서는 국비 교육 과정으로 2024년 03월 06일 부터 
    총 960시간의 교육 프로그램으로 취업연계형 응용SW 전문인력 양성을 위한 교육을 하고 있다. 
    주요 프로그램으로는 'AI응용 SW 전문가','로봇 응용 SW 전문가' 과정을 각각 운영중에 있다. 
    각 과정의 정원은 24명이며 480시간의 이론과 실습 교육을 하고 있으며 이후 480시간의 프로젝트 과정과 
    인턴쉽 과정으로 구성되어 있다. 
    """
)

# Methodology
st.subheader('수업과정')
st.write(
    """
    본 수업은 Python, C, C++, Java등으로 구성 되어 있으며 chatGPT와 함께 하는 과정으로 
    AI를 활용한 프로젝트 개발등을 교육 하고 있다. 
    수업 방법은 오전 09:00부터 13:00까지 4시간 교육을 하고 13:00부터 14:00까지 점심시간을 갖은후 
    14:00부터 18:00까지 오후 수업을 하도록 한다. 
    기타 자세한 문의는 [**우송대학교IT교육센터**](https://itedu.wsu.ac.kr)를 통해 안내 하고있다.
    """
)

# Divider
st.divider()

# Credits
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@AliTslm](https://twitter.com/AliTslm)**', icon="💡")
with c2:
    st.info('**GitHub: [@alitaslimi](https://github.com/alitaslimi)**', icon="💻")
with c3:
    st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz)**', icon="🧠")