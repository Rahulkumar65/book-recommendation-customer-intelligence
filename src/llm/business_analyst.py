import os, requests
SYSTEM="You are a book-retail business analyst. Use only the supplied context. Never invent figures. Separate observations from recommendations."
def ask_llm(question,context):
    base=os.getenv("LLM_BASE_URL","").rstrip("/"); model=os.getenv("LLM_MODEL","")
    if not base or not model:return "LLM not configured. Set LLM_BASE_URL and LLM_MODEL in .env."
    headers={"Content-Type":"application/json"}; key=os.getenv("LLM_API_KEY","")
    if key:headers["Authorization"]="Bearer "+key
    payload={"model":model,"messages":[{"role":"system","content":SYSTEM},{"role":"user","content":f"Context:\n{context}\n\nQuestion: {question}"}],"temperature":0.1}
    r=requests.post(base+"/chat/completions",json=payload,headers=headers,timeout=60); r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
