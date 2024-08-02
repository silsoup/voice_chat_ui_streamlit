import streamlit as st

# openAI package
import openai
import os
from dotenv import load_dotenv

# env.file loading
load_dotenv()

#open ai api key setting
api_key = os.environ.get('OPEN_API_KEY')

#open ai object
openai.OpenAI(api_key=api_key)

# 실행함수
def main():
    st.set_page_config(page_title="음성 챗봇", layout="wide")

    #제목
    st.header("음성 챗봇 프로그램")

    # 구분선
    st.markdown("---")

    with st.expander(
        "음성챗봇 프로그램에 관하여", expanded=True):
        st.write(
            """
            - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용
            - STT는 openai의 whisper활용
            - 답변은 OpenAI의 GPT 모델을 활용합니다. 
            - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
                    
            """
        )
        st.markdown("")
    
    system_content="ou are a thoughtful assistant. Respond to all input in 25 words and answer in korea"
    
    # session state 초기화
    if 'chat' not in st.session_state:
        st.session_state['chat'] =[]

    if 'messages' not in st.session_state:
        st.session_state['messages'] =[{'role':'system','content':system_content}]
    
    if 'check_rest' not in st.session_state:
        st.session_state['sheck_reset'] = False


        with st.sidebar:
            # radio button -choose GPT model
            model = st.radio(label="gpt model", options=["gpt-3.5-turbo","gpt-4o","gpt-4-turbo"])
            st.markdown("---")

            if st.button(label="reset"):
                st.session_state['chat']=[]
                st.session_state['messages']=[{'role':'system','content':system_content}]
                st.session_state['check_reset']=True

# 기능구현공간
col1, col2 = st.columns(2)
with col1:
    # left side
    st.subheader("질문하기")
with col2:
    #right side
    st.subheader("질문/답변")



if __name__=="__main__":
    print(__name__)

    # 실행함수
    main()
