import streamlit as st

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
                    
            """
        )
        st.markdown("")
if __name__=="__main__":
    print(__name__)
    
    # 실행함수
    main()
