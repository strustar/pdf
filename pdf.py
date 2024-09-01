import streamlit as st
import time, os
import pdf_Fcn

os.system('cls')  # 터미널 창 청소, clear screen
total_start_time = time.time();  start_time = time.time()
st.set_page_config(page_title = "PDF 자료 분석", page_icon = "✨", layout = "wide",    # centered, wide
                    initial_sidebar_state="expanded",
                    # runOnSave = True,
                    menu_items = {        #   initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                        # 'Get Help': 'https://www.extremelycoolapp.com/help',
                        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
                        # 'About': "# This is a header. This is an *extremely* cool app!"
                    })

col = st.sidebar.columns(2)
with col[0]:
    keywords = st.text_input("#### :green[✨ 키워드 입력] (공백으로 구분)", "신축 이음").split()    
with col[1]:
    keywords_condition = st.radio('#### :green[✨조건을 선택하세요]', ['and', 'or'], horizontal=True, index=0)

st.sidebar.write('---')
search_condition = st.sidebar.radio('#### :green[✨검색할 조건을 선택하세요]', ['폴더에서 검색', '파일들을 업로드해서 검색'], horizontal=True, index=0)

if '폴더' in search_condition:
    pdf_folders = pdf_Fcn.get_folders_with_pdfs('.')    

    col = st.sidebar.columns([2, 1])
    with col[0]:
        pdf_folder = st.selectbox("#### :blue[검색할 폴더를 선택하세요]", pdf_folders[1:], index=0)
        pdf_list = os.listdir(pdf_folder)
    with col[1]:
        st.write('');  st.write('');  st.write('')
        st.write(f'#### 파일 개수 : {len(pdf_list)}개')
    with st.sidebar.expander('#### :blue[파일 목록을 보시려면 클릭하세요]'):
        st.write(pdf_list)


    for idx, pdf_name in enumerate(pdf_list):
        # idx
        # if idx > 2:
        #     break

        pdf_path = os.path.join(pdf_folder, pdf_name)
        pdf_Fcn.main(pdf_path, keywords, keywords_condition)
else:
    uploaded_files = st.sidebar.file_uploader("#### :blue[PDF 파일들을 끌어 놓으세요]", type=["pdf"], accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        pdf_Fcn.main(uploaded_file, keywords, keywords_condition)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
st.sidebar.write('---')
st.sidebar.write(f"#### :orange[총 검색 시간 : {time.time() - start_time:.2f} 초]")