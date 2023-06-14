import openai
import time
import itchat

API_KEY = "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"


print("start\n")

def use_openai_api(prompt, api_key, tempreature=0, model="gpt-3.5-turbo"):
    
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model = model,
        messages = [{"role":"user", "content":prompt}],
        temperature = tempreature
    )
    
    return response

def get_content(response):

    return response.choices[0].message["content"]

def main():

    text = f"""
    Roy contended that McCarthy cut a hand-shake deal \
    in January that all nine Republicans on the \
    powerful panel must agree to move any legislation \
    forward, otherwise bills could not be considered \
    by the full House for majority approval. That \
    would essentially doom the debt ceiling bill since \
    Roy – who sits on the panel – and another \
    conservative committee member are trying to stop \
    the bill from advancing.
    """
    prompt = f"""
    Summarise the text delimited by triple backticks \
    into a single sentense. And then translate it to \
    Chinese.
    ```{text}```
    """

    test_prompt = f"""
    假定你是李华, 你们学校英语俱乐部计划排练一部英文短剧以参加下个月的英语戏剧节。请根据下面的要点提示, 给外教Mr. Brown用英语写一封电子邮件, 邀请他做你们的短剧顾问。 \
    1.写信的原因和目的 2. 需要何种帮助  3. 期待回复 \
    注意：（1）词数100词左右（2）可适当增加细节, 以使行文连贯
    """
    response = use_openai_api(test_prompt, API_KEY, tempreature=0)
    print(get_content(response))
    print(response["usage"])
    
    

#main()
itchat.auto_login(enableCmdQR=2)
itchat.send('Hello, filehelper', toUserName='文件传输助手')



print("\nend")
