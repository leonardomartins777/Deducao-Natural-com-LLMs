# -*- coding: utf-8 -*-
"""Experimentos Julho 2025
# Adaptado para multiplos Experimentos:
### Modelos AceitosÇ
- GPTs ;
- Modelos Disponíveis no Ollama;
---
### Tipos de Questões
- Questões de Lógica de Primeira Ordem;
- Questões de Lógica Proposicional;
---
### Formato de Questões
- Questões Escritas em Latex;
- Questões Escritas na Linguagem do NADIA;
---
### Tipo de Prompt
- Com 1 questão de Entrada;
- Com 1 questão de Entrada + Guia Básico de Formatação (para ajudar a deixar a resposta com o maior fidelidade na Formatação);
---
"""

#importando bibliotecas
from random import randrange
import os.path
import requests
import json
import os
import configparser
import csv
##atualizacao
from nadia.nadia_pt_fo import check_proof
import ollama
import argparse

"""Crie Um arquivo 'config.ini' e cole o seguinte texto:

[API]
key = insira_a_chave_aqui

Substitua a chave da API na variável key, mais informacoes sobre a chave API: https://platform.openai.com/account/api-keys

"""

#Carregando Arquivos de Configuração
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['API']['key']
#openai.api_key = API_KEY

###Parser
###
#rodar as questoes e gerar relatorio
#Variaveis
#user content = Pergunta Padrao (para o exemplo)
#assistant_response = Resposta Padrao (para o exemplo)
#API_KEY = Chave da API da OpenAI
#Questoes de Entrada = Dicionario de Questoes de Entrada (Logica de Predicados ou Proposicional)
  #Modelo= id do modelo utilizado, exemplo:
  #id_modelo = "gpt-3.5-turbo"
  #id_modelo = "gpt-3.5-turbo-0613"
  #id_modelo ="gpt-4-0125-preview"
  #id_modelo = "gpt-4o"
#api = chatgpt (para modelos gpt); ollama (para os demais modelos)
parser = argparse.ArgumentParser()
parser.add_argument("num_questions", type=int,
                    help="quantidade de questoes a serem utilizadas")
parser.add_argument("tipo_de_questoes",
                    help="Logica Proposicional (proposicional) ou Logica de Predicados (predicados)")
parser.add_argument("--modelo",
                    help="nome do modelo (LLM) a ser utilizado", default="gemma2:2b")
parser.add_argument("--complemento_arquivo",
                    help="nome adicionado como prefixo aos arquivos que serao salvos", default="experimento")
# parser.add_argument("--debug_mode", action="store_true",
#                     help="Habilitar modo de depuração")
parser.add_argument("--api",
                    help="API utilizada para comunicacao com o modelo: ollama ou gpt",default="ollama")
args = parser.parse_args()
print("ARGS",args)
print("ARGS",args.num_questions)
print("ARGS",args.tipo_de_questoes)
print("ARGS",args.modelo)
print("ARGS",args.complemento_arquivo)
print("ARGS",args.api)
if args.num_questions > 0:
    print("ARGS",args.num_questions)

    num_questions = args.num_questions
    
else:
    print("ARGS",args.num_questions)

    print("numero de questoes invalido")


print("ARGS",args.modelo)

if args.api == "ollama":
    print("ARGS",args.modelo)

    api=args.api
    
elif args.api == "gpt":
    print("ARGS",args.modelo)

    api=args.api
else:
    print("ARGS",args.modelo)

    print("Tipo de API nao informado de forma correta")

###
#questoes de logica de primeira ordem  em Latex
####
questoes_fo = dict()
questoes_fo['Q1'] = r'$\forall x  P(x)  \vdash \lnot \exists x \lnot  P(x)$'

questoes_fo['Q2'] = r'$\lnot \exists x \lnot  P(x) \vdash \forall x  P(x)$'

questoes_fo['Q3'] = r'$\exists x  P (x) \vdash \lnot \forall x \lnot  P(x)$'

questoes_fo['Q4'] = r'$\lnot \forall x \lnot  P (x) \vdash \exists x  P(x)$'

questoes_fo['Q5'] = r'$\forall x( P(x)\wedge Q(x)) \vdash (\forall x P(x)\wedge\forall x Q(x))$'

questoes_fo['Q6'] = r'$\forall x \forall y  P (x,y) \vdash \forall y \forall x  P (x,y)$'


questoes_fo['Q7'] = r'$\forall x( P \rightarrow  Q (x)) \vdash( P \rightarrow\forall x Q (x))$'

questoes_fo['Q8'] = r'$\exists x( P (x)\vee Q (x)) \vdash (\exists x P (x)\vee\exists x Q (x))$'

questoes_fo['Q9'] = r'$\lnot \forall x  P (x) \vdash \exists x \lnot  P (x)$'

questoes_fo['Q10'] = r'$\exists x \lnot  P (x) \vdash \lnot \forall x  P (x)$'

questoes_fo['Q11'] = r'$\lnot \exists x  P (x) \vdash \forall x \lnot  P (x)$'

questoes_fo['Q12'] = r'$\forall x \lnot  P (x) \vdash \lnot \exists x  P (x)$'

questoes_fo['Q13'] = r'$\exists x( P (x)\wedge Q ) \vdash (\exists x P (x)\wedge Q )$'

questoes_fo['Q14'] = r'$(\exists x P (x)\wedge Q ) \vdash \exists x( P (x)\wedge Q )$'

questoes_fo['Q15'] = r'$\forall x( P (x)\vee Q ) \vdash (\forall x P (x)\vee Q )$'

questoes_fo['Q16'] = r'$(\forall x P (x)\vee Q ) \vdash \forall x( P (x)\vee Q )$'

questoes_fo['Q17'] = r'$\exists x( P (x)\rightarrow Q ) \vdash (\forall x P (x)\rightarrow Q )$'

questoes_fo['Q18'] = r'$(\forall x P (x)\rightarrow Q ) \vdash \exists x( P (x)\rightarrow Q ) $'

questoes_fo['Q19'] = r'$\exists x( P \rightarrow Q (x)) \vdash ( P \rightarrow\exists x Q (x)) $'

questoes_fo['Q20'] = r'$( P \rightarrow\exists x Q (x)) \vdash \exists x( P \rightarrow Q (x))$ '
###
#questoes de logica proposicional em Latex
####
questoes = dict()
questoes['Q1'] = r'$\vdash A \vee( A \wedge  B )\rightarrow  A $'
questoes['Q2'] = r'$\vdash A \wedge( A \vee  B )\rightarrow  A $'
questoes['Q3'] = r'$\vdash( A \rightarrow( B \rightarrow  C ))\rightarrow( B \rightarrow( A \rightarrow  C ))$'
questoes['Q4'] = r'$\vdash( A \rightarrow( A \rightarrow  B ))\rightarrow( A \rightarrow  B )$'
questoes['Q5'] = r'$\vdash(\lnot  A \rightarrow  B )\rightarrow((\lnot  A \rightarrow\lnot  B )\rightarrow  A )$'
questoes['Q6'] = r'$\vdash A \vee\lnot  A $'
questoes['Q7'] = r'$\vdash( A \rightarrow  B )\vee ( B \rightarrow  A )$'
questoes['Q8'] = r'$\vdash A \rightarrow  A $'
questoes['Q9'] = r'$\vdash( A \rightarrow  B )\rightarrow(( C \rightarrow  A )\rightarrow( C \rightarrow  A ))$'
questoes['Q10'] = r'$A\land B \rightarrow C \vdash B \rightarrow (A\rightarrow C)$'
questoes['Q11'] = r'$B \rightarrow (A\rightarrow C) \vdash A\land B \rightarrow C$'
questoes['Q12'] = r'$\vdash( A \rightarrow( B \rightarrow  C ))\rightarrow(( A \rightarrow  B )\rightarrow( A \rightarrow  C ))$'
questoes['Q13'] = r'$\vdash( A \rightarrow( B \rightarrow  A ))$'
questoes['Q14'] = r'$\vdash(( A \rightarrow  B )\rightarrow  A )\rightarrow  A $'
questoes['Q15'] = r'$ A \vee  B ,  A \rightarrow  C ,  B \rightarrow  C \vdash  C $'
questoes['Q16'] = r'$ A \vdash\lnot\lnot  A $'
questoes['Q17'] = r'$\lnot\lnot  A \vdash  A $'
questoes['Q18'] = r'$ A \rightarrow  B , \lnot  B \vdash\lnot  A $'
questoes['Q19'] = r'$\lnot  B \rightarrow\lnot  A \vdash  A \rightarrow  B $'
questoes['Q20'] = r'$ A \rightarrow  B \vdash \lnot  B \rightarrow\lnot  A $'
questoes['Q21'] = r'$\lnot( A \vee  B )\vdash \lnot  A \wedge\lnot  B $'
questoes['Q22'] = r'$\lnot  A \wedge\lnot  B \vdash \lnot( A \vee  B )$'
questoes['Q23'] = r'$\lnot( A \wedge  B )\vdash \lnot  A \vee\lnot  B $'
questoes['Q24'] = r'$\lnot  A \vee\lnot  B \vdash\lnot( A \wedge  B )$'
questoes['Q25'] = r'$ A \vee( B \wedge  C )\vdash( A \vee  B )\wedge( A \vee  C )$'
questoes['Q26'] = r'$( A \vee  B )\wedge( A \vee  C )\vdash  A \vee( B \wedge  C )$'
questoes['Q27'] = r'$ A \wedge( B \vee  C )\vdash ( A \wedge  B )\vee( A \wedge  C )$'
questoes['Q28'] = r'$( A \wedge  B )\vee( A \wedge  C )\vdash  A \wedge( B \vee  C )$'
questoes['Q29'] = r'$ A \vee  B , \lnot  B \vdash  A $'
questoes['Q30'] = r'$ A \vee  B \vdash\lnot  A \rightarrow  B  $'
questoes['Q31'] = r'$\lnot  A \rightarrow  B \vdash  A \vee  B $'
questoes['Q32'] = r'$ A \wedge  B \vdash \lnot( A \rightarrow\lnot  B )$'
questoes['Q33'] = r'$\lnot( A \rightarrow\lnot  B )\vdash  A \wedge  B $'
questoes['Q34'] = r'$ A \vee  B \vdash \lnot(\lnot  A \wedge\lnot  B )$'
questoes['Q35'] = r'$\lnot(\lnot  A \wedge\lnot  B )\vdash  A \vee  B $'
questoes['Q36'] = r'$ A \rightarrow  B \vdash \lnot( A \wedge\lnot  B )$'
questoes['Q37'] = r'$\lnot( A \wedge\lnot  B )\vdash  A \rightarrow  B $'
questoes['Q38'] = r'$ A \wedge  B \vdash \lnot(\lnot  A \vee\lnot  B )$'
questoes['Q39'] = r'$\lnot(\lnot  A \vee\lnot  B )\vdash  A \wedge  B $'
questoes['Q40'] = r'$ A \rightarrow  B \vdash\lnot  A \vee  B $'
questoes['Q41'] = r'$\lnot  A \vee  B \vdash  A \rightarrow  B $'

#questoes de logica e de primeira ordem escritas no formato aceito
#pela ferramenta NADIA
questoes_gerais = dict()
questoes_gerais["Q1"] = "Ax P(x) |- ~Ex ~P(x)"
questoes_gerais["Q2"] = "~Ex ~P(x) |- Ax P(x)"
questoes_gerais["Q3"] = "Ex P(x) |- ~Ax ~P(x)"
questoes_gerais["Q4"] = "~Ax ~P(x) |- Ex P(x)"
questoes_gerais["Q5"] = "Ax (P(x)&Q(x)) |- Ax P(x)&Ax Q(x)"
questoes_gerais["Q6"] = "Ax Ay P(x,y) |- Ay Ax P(x,y)"
questoes_gerais["Q7"] = "Ax (P->Q(x)) |- P->Ax Q(x)"
questoes_gerais["Q8"] = "Ex (P(x)|Q(x)) |- Ex P(x)|Ex Q(x)"
questoes_gerais["Q9"] = "~Ax P(x) |- Ex ~P(x)"
questoes_gerais["Q10"] = "Ex ~P(x) |- ~Ax P(x)"
questoes_gerais["Q11"] = "~Ex P(x) |- Ax ~P(x)"
questoes_gerais["Q12"] = "Ax ~P(x) |- ~Ex P(x)"
questoes_gerais["Q13"] = "Ex (P(x)&Q) |- Ex P(x)&Q"
questoes_gerais["Q14"] = "Ex P(x)&Q |- Ex (P(x)&Q)"
questoes_gerais["Q15"] = "Ax (P(x)|Q) |- Ax P(x)|Q"
questoes_gerais["Q16"] = "Ax P(x)|Q |- Ax (P(x)|Q)"
questoes_gerais["Q17"] = "Ex (P(x)->Q) |- Ax P(x)->Q"
questoes_gerais["Q18"] = "Ax P(x)->Q |- Ex (P(x)->Q)"
questoes_gerais["Q19"] = "Ex (P->Q(x)) |- P->Ex Q(x)"
questoes_gerais["Q20"] = "P->Ex Q(x) |- Ex (P->Q(x))"
questoes_gerais["Q21"] = "|- (A|(A&B))->A"
questoes_gerais["Q22"] = "|- (A&(A|B))->A"
questoes_gerais["Q23"] = "|- (A->(B->C))->(B->(A->C))"
questoes_gerais["Q24"] = "|- (A->(A->B))->(A->B)"
questoes_gerais["Q25"] = "|- (~A->B)->((~A->~B)->A)"
questoes_gerais["Q26"] = "|- A|~A"
questoes_gerais["Q27"] = "|- (A->B)|(B->A)"
questoes_gerais["Q28"] = "|- A->A"
questoes_gerais["Q29"] = "|- (A->B)->((C->A)->(C->A))"
questoes_gerais["Q30"] = "(A&B)->C |- B->(A->C)"
questoes_gerais["Q31"] = "B->(A->C) |- (A&B)->C"
questoes_gerais["Q32"] = "|- (A->(B->C))->((A->B)->(A->C))"
questoes_gerais["Q33"] = "|- A->(B->A)"
questoes_gerais["Q34"] = "|- ((A->B)->A)->A"
questoes_gerais["Q35"] = "A->C, B->C, A|B |- C"
questoes_gerais["Q36"] = "A |- ~~A"
questoes_gerais["Q37"] = "~~A |- A"
questoes_gerais["Q38"] = "A->B, ~B |- ~A"
questoes_gerais["Q39"] = "~B->~A |- A->B"
questoes_gerais["Q40"] = "A->B |- ~B->~A"
questoes_gerais["Q41"] = "~(A|B) |- ~A&~B"
questoes_gerais["Q42"] = "~A&~B |- ~(A|B)"
questoes_gerais["Q43"] = "~(A&B) |- ~A|~B"
questoes_gerais["Q44"] = "~A|~B |- ~(A&B)"
questoes_gerais["Q45"] = "A|(B&C) |- (A|B)&(A|C)"
questoes_gerais["Q46"] = "(A|B)&(A|C) |- A|(B&C)"
questoes_gerais["Q47"] = "A&(B|C) |- (A&B)|(A&C)"
questoes_gerais["Q48"] = "(A&B)|(A&C) |- A&(B|C)"
questoes_gerais["Q49"] = "A|B, ~B |- A"
questoes_gerais["Q50"] = "A|B |- ~A->B"
questoes_gerais["Q51"] = "~A->B |- A|B"
questoes_gerais["Q52"] = "A&B |- ~(A->~B)"
questoes_gerais["Q53"] = "~(A->~B) |- A&B"
questoes_gerais["Q54"] = "A|B |- ~(~A&~B)"
questoes_gerais["Q55"] = "~(~A&~B) |- A|B"
questoes_gerais["Q56"] = "A->B |- ~(A&~B)"
questoes_gerais["Q57"] = "~(A&~B) |- A->B"
questoes_gerais["Q58"] = "A&B |- ~(~A|~B)"
questoes_gerais["Q59"] = "~(~A|~B) |- A&B"
questoes_gerais["Q60"] = "A->B |- ~A|B"
questoes_gerais["Q61"] = "~A|B |- A->B"
# A funcao recebe a chave da api e a conversa de entrada
# retorna a resposda da API
def chamada_api_chatGPT(API_KEY,conversa_entrada,id_modelo):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type":"application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    body_mensagem = {
        "model": id_modelo,
        #"temperature" : 0.2,
        "messages": conversa_entrada
    }
    body_mensagem = json.dumps(body_mensagem)
    resposta = requests.post(link,headers=headers,data=body_mensagem)
    resposta = resposta.json()
    return resposta
###
###
###
def chamada_api_ollama( conversa_entrada,id_modelo = 'gemma2:2b', stream = False ):
    
    resposta = ollama.chat(
    model= id_modelo,
    messages= conversa_entrada,
    stream=stream,
    options= {
             "num_predict": 1000
         }
    )
    
    return resposta
"""## Versao Logica Proposicional"""

# Texto Padrao da primeira mensagem do usuario
user_content_proposicional = r"""
Questão:
escreva a prova do teorema a seguir, usando o sistema de dedução natural no estilo fitch e de acordo com o formato aceito pelo NADIA.
Teorema:""
A->B, B->C |- A->C
""
"""
# Texto Padrao da primeira mensagem do assistente
assistant_response_proposicional = r"""
Prova:""
1. A -> B pre
2. B -> C pre
3. { A hip
4. B ->e 3, 1
5. C ->e 4, 2
}
6. A -> C ->i 3-5
""
"""
print(user_content_proposicional)
print(assistant_response_proposicional)

"""## Versao Logica de Primeira Ordem"""

# Texto Padrao da primeira mensagem do usuario
user_content_LPO = r"""
Questão:
escreva a prova do teorema a seguir, usando o sistema de dedução natural no estilo fitch e de acordo com o formato aceito pelo NADIA.
Teorema:""
Ax (H(x)->M(x)), Ax ~M(x) |- ~Ex H(x)
""
"""

# Texto Padrao da primeira mensagem do assistente
assistant_response_LPO = r"""
Prova:""
1. Ax(H(x) -> M(x)) pre
2. Ax~M(x) pre
3. { Ex H(x) hip
4.  { a H(a) hip
5.    H(a) -> M(a) Ae 1
6.    M(a) ->e 4, 5
7.    ~M(a) Ae 2
8.    @ ~e 6, 7
}
9. @ Ee 3, 4-8
}
10.~Ex H(x) ~i 3-9
""
"""

print(user_content_LPO)
print(assistant_response_LPO)

#funcao que salva os itens em latex como um arquivo txt
def salvar_arqivo_Latex(nome_arquivo_txt,string_conteudo):
  arquivo = open(nome_arquivo_txt,'w')
  arquivo.write(string_conteudo)
  arquivo.close()

#funcao que salva os resultados como um arquivo csv
def salvar_arqivo_CSV(nome_arquivo_csv,dicionarios_questoes,labels):
  try:
      with open(nome_arquivo_csv, "w") as f:
          writer = csv.DictWriter(f, fieldnames=labels)
          writer.writeheader()
          for elem in dicionarios_questoes:
              writer.writerow(elem)
  except IOError:
      print("I/O error")

def open_files(arquivo):
    with open(arquivo, 'r') as arquivo:
        nome_string = arquivo.read()
        #print(nome_string)
    return nome_string


#funcao que cria conversa a ser enviada para a api
def build_a_chat(user_content,assistant_response,questao_entrada):
    #Adicionado uma mensagem no Inicio da conversa para mostrar um exemplo de pergunta e resposta que a IA deve obedecer
    template_tutorial = open_files("template.txt")
    print("AQUI 01")
    template_tutorial = template_tutorial + "\n\n"
    user_question = f"""
      Questão:
escreva a prova do teorema a seguir, usando o sistema de dedução natural no estilo fitch e de acordo com o formato aceito pelo NADIA.
      Teorema:""
      ${questao_entrada}$
      ""
      """
    print("AQUI 03")
      #Criacao da Conversa de Entrada -> Pergunta Exemplo + Resposta de Exemplo + Pergunta a ser Respondida
    conversa_entrada = [{"role": "user", "content": template_tutorial + user_content},
                      {"role": "assistant", "content":assistant_response},
                      {"role": "user", "content": template_tutorial + user_question}]
    print("AQUI 04")                  
    return conversa_entrada

#rodar as questoes e gerar relatorio
#Variaveis
#user content = Pergunta Padrao (para o exemplo)
#assistant_response = Resposta Padrao (para o exemplo)
#API_KEY = Chave da API da OpenAI
#Questoes de Entrada = Dicionario de Questoes de Entrada (Logica de Predicados ou Proposicional)
  #Modelo= id do modelo utilizado, exemplo:
  #id_modelo = "gpt-3.5-turbo"
  #id_modelo = "gpt-3.5-turbo-0613"
  #id_modelo ="gpt-4-0125-preview"
  #id_modelo = "gpt-4o"
#api = chatgpt (para modelos gpt); ollama (para os demais modelos)
def run_questions(num_questions,user_content,assistant_response,API_KEY,questoes_entrada,modelo,complemento_arquivo,debug_mode=False,api="ollama"):
    arquivo_LATEX = ''''''
    dicionarios_questoes = []
    
    for x in range(1,num_questions+1):
        conversa_entrada = build_a_chat(user_content,assistant_response,questoes_entrada[f'Q{x}'])
        
        #Chamada da API
        if api=="ollama":
            reposta_ = chamada_api_ollama(conversa_entrada,modelo)
        else:
            reposta_ = chamada_api_chatGPT(API_KEY,conversa_entrada,modelo)
        try:
        #filtrar apenas a resposta do Modelo
            if api=="ollama":
                reposta_ = reposta_['message']['content']
            else:
                reposta_ = reposta_["choices"][0]["message"]["content"]
          
        except:
            print("Um ERRO OCORREU",reposta_ )
        if debug_mode:
            print("Questao:",x)
            print("mensagens de entrada")
            print(conversa_entrada)
            print('resposta')
            print(reposta_)
        #SALVANDO na string do arquivo Latex
        arquivo_LATEX+= '\n\item '+questoes_entrada[f'Q{x}']+' \n\nRESPOSTA CHAT-GPT  \n\n'+reposta_+' \n\n'
        #SALVANDO na string  do arquivo CSV
        dicionarios_questoes.append({'numero':f'q{x}','questao':questoes_entrada[f'Q{x}'],'resposta':reposta_,'resposta_correta':'','avaliacao':''})
    labels = ['numero','questao','resposta','resposta_correta','avaliacao']
    salvar_arqivo_CSV('Relatorio-'+complemento_arquivo+'-'+'.csv',dicionarios_questoes,labels)
    salvar_arqivo_Latex('Relatorio-'+complemento_arquivo+'-'+'.txt',arquivo_LATEX)

#num_questions,user_content,assistant_response,API_KEY,questoes_entrada,modelo,complemento_arquivo,debug_mode=False
######################
######################
### OLLAMA EXAMPLE ###
######################
######################
#run_questions(num_questions=5,user_content=user_content_proposicional,assistant_response=assistant_response_proposicional,API_KEY=API_KEY,questoes_entrada=questoes,modelo="gemma2:2b",complemento_arquivo="experimento_proposicional-GEMA2B",debug_mode=True,api="ollama")
######################
######################
## CHATGPT EXAMPLE ###
######################
######################
#run_questions(num_questions=5,user_content=user_content_proposicional,assistant_response=assistant_response_proposicional,API_KEY=API_KEY,questoes_entrada=questoes,modelo="gpt-4o",complemento_arquivo="experimento_proposicional-GPT",debug_mode=True,api="gpt")

#run_questions(num_questions=20,user_content=user_content_LPO,assistant_response=assistant_response_LPO,API_KEY=API_KEY,questoes_entrada=questoes_fo,modelo="gpt-4o",complemento_arquivo="experimento_primeira-ordem")
###
#terminal
###

if args.tipo_de_questoes == "proposicional":
    print("ARGS",args.tipo_de_questoes)

    user_content_terminal=user_content_proposicional
    assistant_response_terminal=assistant_response_proposicional
    questoes_entrada_terminal=questoes
elif args.tipo_de_questoes == "predicados":
    print("ARGS",args.tipo_de_questoes)

    user_content_terminal=user_content_LPO
    assistant_response_terminal=assistant_response_LPO
    questoes_entrada_terminal=questoes_fo
    print("ARGS",args.tipo_de_questoes)
elif args.tipo_de_questoes == "gerais":
    print("ARGS",args.tipo_de_questoes)

    user_content_terminal=user_content_LPO
    assistant_response_terminal=assistant_response_LPO
    questoes_entrada_terminal=questoes_gerais
    print("ARGS",args.tipo_de_questoes)
else:
    print("ARGS",args.tipo_de_questoes)

    print("Tipo de questoes nao informado de forma correta")

run_questions(num_questions=args.num_questions,user_content=user_content_terminal,assistant_response=assistant_response_terminal,API_KEY=API_KEY,questoes_entrada=questoes_entrada_terminal,modelo=args.modelo,complemento_arquivo=args.complemento_arquivo,debug_mode=True,api=api)
