import os
from dotenv import load_dotenv
from googletrans import Translator
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
tr = Translator()

TARGET = "en" 

def llm_english(prompt_en):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"Helpful, concise."},
                  {"role":"user","content":prompt_en}]
    )
    return r.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Type in any language. 'exit' to quit.")
    while True:
        user = input("You: ")
        if user.lower() == "exit": break
        det = tr.detect(user).lang
        en = tr.translate(user, src=det, dest=TARGET).text if det != TARGET else user
        ans_en = llm_english(en)
        ans_user = tr.translate(ans_en, src=TARGET, dest=det).text if det != TARGET else ans_en
        print(f"Assistant ({det}): {ans_user}")
