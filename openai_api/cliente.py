# import openai
# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Caminho absoluto para o .env na raiz do projeto
# env_path = Path(__file__).resolve().parent.parent.parent / '.env'
# load_dotenv(dotenv_path=env_path)


# def get_car_ai_bio(model, brand, year):
#     prompt = '''
#     Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas especificas sobre o carro, como o modelo, a marca e o ano de fabricação. Use uma linguagem persuasiva e envolvente para atrair potenciais compradores.
#     Escreva a descrição em português.
# '''
#     openai.api_key = "OPENAI_SECRET_KEY"
#     prompt = prompt.format(brand, model, year)
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         prompt=prompt,
#         max_tokens=1000,

#     )
#     return response['choices'][0]['text']
