import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import detect_credit_card_info


def configure_interface():
    st.title("Upload de Arquivo - Desafio 2 - Azure - Face Docs")
    upload_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if upload_file is not None:
        filename = upload_file.name
        blob_url = upload_blob(upload_file, filename)
        
        if blob_url:

            st.write(f"Arquivo {filename} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = detect_credit_card_info(blob_url)
            show_image_and_validation(blob_url, credit_card_info)

        else:
            st.write(f"Erro ao enviar o arquivo {filename} para o Azure Blob Storage")


def show_image_and_validation(blob_url, credit_card_info):

    st.image(blob_url, caption="Imagem válida", use_column_width=True)
    st.write("Resultado da validação:")

    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expirity_date']}")

    else:
        st.markdown(f"<h1 style='color: green;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write(f"Este não é um cartão de crédito válido")

    st.write(credit_card_info)

if __name__ == "__main__":
    configure_interface()