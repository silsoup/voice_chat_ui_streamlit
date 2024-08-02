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

        with st.sidebar:
            #radio button
            model = st.radio(label="gpt model", options=["gpt-3.5-turbo","gpt-4o","gpt-4-turbo"])
            st.markdown("---")

            if st.button(label="reset"):
                pass

if __name__=="__main__":
    print(__name__)

    # 실행함수
    main()
