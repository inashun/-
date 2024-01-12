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
    return f"{word}は素晴らしい単語です。"

def main():
    print("Azure OpenAI チャットボット - プログラムを終了するには 'end' を入力してください")

    while True:
        user_input = input("ユーザー: ")

        if user_input.lower() == "end":
            print("プログラムを終了します。")
            break

        word_description = get_word_description(user_input)
        quiz_prompt = f"{word_description} それに関するクイズを出題します。"
        ai_response = ask_openai(quiz_prompt)
        print("AI:", ai_response)

if __name__ == "__main__":
    main()
