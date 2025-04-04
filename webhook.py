# Webhook para integração do GPT-4 com ManyChat

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configure sua API Key da OpenAI aqui
openai.api_key = 'SUA_API_KEY_AQUI'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Extrair a mensagem do usuário
    user_message = data.get('message')

    if not user_message:
        return jsonify({'error': 'Nenhuma mensagem encontrada.'}), 400

    try:
        # Fazer a chamada para o GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente humanizado chamado Rosa Assistente."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500
        )

        # Extrair a resposta gerada pela IA
        ai_response = response['choices'][0]['message']['content']
        return jsonify({'reply': ai_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
