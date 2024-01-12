import requests

api_endpoint = "https://sunhackathon39.openai.azure.com/openai/deployments/GPT35TURBO/chat/completions?api-version=2023-05-15"
api_key = "bae83264c3bf4475bc0ad5be1345dbe4"

def ask_openai(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": f"{api_key}",
    }

    payload = {
        "messages": [
            {"role": "user", "content": prompt},
        ]
    }

    try:
        response = requests.post(api_endpoint, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        choices = data.get('choices', [])
        if choices:
            ai_response = choices[0].get('message', {}).get('content', 'AIからのメッセージがありません')
        else:
            ai_response = 'AIからのメッセージがありません'

    except requests.exceptions.RequestException as e:
        print(f"エラー: APIへのリクエスト中にエラーが発生しました - {e}")
        ai_response = "エラーが発生しました"

    except Exception as e:
        print(f"エラー: 応答データの処理中にエラーが発生しました - {e}")
        ai_response = "エラーが発生しました"

    return ai_response

def get_word_description(word):
    # 仮にダミーの単語説明を返す関数
    return (ask_openai(f"{word}の説明をしてください。") )

def main():
    print("検索したいワードを入力してください - プログラムを終了するには 'end' を入力してください")

    while True:
        user_input = input("ユーザー: ")

        if user_input.lower() == "end":
            print("プログラムを終了します。")
            break

        word_description = get_word_description(user_input)

        print("AI:", word_description)


        quiz_prompt = f"{user_input} に関するクイズを１つ出してください。"
        ai_response = ask_openai(quiz_prompt)
        print("AI:", ai_response)

        print("回答してください")

        user_input = input("ユーザー: ")

        a = f"{ai_response}の回答が{user_input} があっているか教えてください。間違っていた場合は答えを教えてください。"

        b = ask_openai(a)

        print("AI:", b)

        return main()
        
if __name__ == "__main__":
 main()
