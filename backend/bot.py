import pandas as pd
import numpy as np
qa_list=[]
data = pd.read_csv('./backend/ChatbotQAsamples.csv',encoding='utf_8')
question_list=data['Unnamed: 2'].to_list()
answer_list=data['Unnamed: 3'].to_list()
a=0
for q in question_list:
  
  qa_list.append(q)
  qa_list.append(answer_list[a])
  a=a+1
del qa_list[0:4]
del question_list[0:2]
del answer_list[0:2]

import tensorflow_hub as hub
module_url = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'
model = hub.load(module_url)

def embed_text(input):
  return model(input)

q_embeddings=[]
for q in question_list:
  q_embeddings.append(embed_text(q))

import json
document = dict()

with open("./backend/japdatasentence.json","r",encoding="utf-8") as f:
  document = json.load(f)

tempk=""
def similarity(x,y):
    return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

def check_in_document(vector, prev):

  ans_list = list()
  for sen, vec in document.items():
    tmp = similarity(vector, vec)
    ans_list.append((tmp, sen))

  ans_list = sorted(ans_list, key = lambda x:x[0], reverse = True)

  ret_ans = ''
  
  for ans in ans_list:

    _, ret_ans = ans
    
    if ret_ans not in prev:
      break
    
  return ret_ans

while True:
  nearest_q_confidence=[]
  request1=input('User:')
  embed=embed_text(request1)
  pos=0
  for q_embed in q_embeddings:
    confidence=np.inner(embed,q_embed)[0][0]
    nearest_q_confidence.append([confidence,pos])
    pos=pos+1
  nearest_q_confidence.sort(reverse=True)
  flag = True
  
  if nearest_q_confidence[0][0] > 0.7:
    print('Bot: ',answer_list[nearest_q_confidence[0][1]])
    print('Bot: confidence:',nearest_q_confidence[0][0])
    print('Bot: 応答に満足できない場合は、1を押します。')
    request2=int(input('User:'))
    i = 1
    while request2 == 1 and nearest_q_confidence[i][0] > 0.7:

      print('Bot: もしかして？：')
      print('Bot:',question_list[nearest_q_confidence[i][1]])
      print('Bot: 満足できない場合は1を押してください')

      request2 = int(input('User:'))

      if request2 != 1:
        flag = False
        question_list.append(request1)
        q_embeddings.append(embed_text(request1))
        answer_list.append(nearest_q_confidence[i][1])
        break

      else:
        i = i + 1

  # if flag:    
  # #Call the BERT server here
  # #Convert the request1 into vector and send the embeddings as argument for the function
  #   request2 = 1
  #   prev = []
  #   while request2 == 1:

  #     answer = check_in_document(vector, prev)
  #     print('Bot: ', answer)
  #     print('Bot: 満足できない場合は1を押してください')
  #     request2 = int(input('User: '))
      
  #     if request2 != 1:
  #       question_list.append(request1)
  #       answer_list.append(answer)

  #     prev.append(answer)     