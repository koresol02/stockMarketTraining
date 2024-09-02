import boto3
import streamlit as st



#2 create client connection with bedrock
client_bedrock_knowledgebase = boto3.client('bedrock-agent-runtime')
def get_answer(prompt):
    #3 Store the user prompt
    print(prompt)
    user_prompt=prompt
    # 4. Use retrieve and generate API
    client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
    input={
        'text': user_prompt
    },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': 'FSRPOHRDU3',
            'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/meta.llama3-1-8b-instruct-v1:0'
                }
            })
            
    # print(client_knowledgebase)     
    #print(client_knowledgebase['output']['text'])
    #print(client_knowledgebase['citations'][0]['generatedResponsePart']['textResponsePart'])
    response_kbase_final = client_knowledgebase['output']['text']
    # return {
    #     'statusCode': 200,
    #     'body': response_kbase_final
    # }
    return response_kbase_final


# response_content = get_answer("what is gamma")
# print(response_content)

st.set_page_config(page_title="Nitin's Stocks Futures  & Options Training Using RAG") ### Modify Heading

new_title = '<p style="font-family:comic-sans; color:Green; font-size: 42px;">Nitin\'s GPT To Learn Stock Markets🎯</p>'
st.markdown(new_title, unsafe_allow_html=True) ### Modify Title

input_text = st.text_area("Your Question", "What exactly is the stock market?", label_visibility="collapsed") 
go_button = st.button("📌Get Answer", type="primary") ### Button Name


if go_button: 
    
    with st.spinner("📢Anytime someone tells me that I can't do something, I want to do it more - Taylor Swift"): ### Spinner message
        response_content = get_answer(input_text) ### replace with RAG Function from backend file
        st.write(response_content) 

st.markdown("![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGpwbjVsbG5pZXFqaXJ4eTd2ZDYxdG1oNm04ZnZ0N3FkM3RpYmcwdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KbfDRCD1GB9VTrzvtB/giphy.gif)", unsafe_allow_html=True)

