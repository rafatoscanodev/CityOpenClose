import streamlit as st
import requests

# Função para criar um card
def create_card(image, badge, description, title, long_description):
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(image, width=100)
        with col2:
            st.write(f"**{title}**")
            st.caption(description)
            st.caption(badge)

# Dados de exemplo para os cards
data = [
    {
        "image": "path_to_image1.jpg",
        "badge": "New",
        "description": "Short description 1",
        "title": "Card Title 1",
        "long_description": "This is a longer description of the first item."
    },
    {
        "image": "path_to_image2.jpg",
        "badge": "Sale",
        "description": "Short description 2",
        "title": "Card Title 2",
        "long_description": "This is a longer description of the second item."
    }
]

# Renderização dos cards
for item in data:
    if st.button(item['title'], key=item['title']):
        with st.container():
            st.header(item['title'])
            st.write(item['long_description'])
            user_input = st.text_input("Enter your text here")
            if st.button("Submit"):
                # Chamada ao assistente da OpenAI
                response = requests.post(
                    'https://api.openai.com/v1/engines/davinci/completions',
                    headers={'Authorization': 'Bearer YOUR_OPENAI_API_KEY'},
                    json={
                        'prompt': user_input,
                        'max_tokens': 150
                    }
                )
                result_text = response.json()['choices'][0]['text'].strip()
                st.download_button("Download Text", result_text, file_name="result.txt")
                st.success(result_text)

def main():
    st.title("Your Streamlit App")
    for item in data:
        create_card(**item)

if __name__ == "__main__":
    main()
