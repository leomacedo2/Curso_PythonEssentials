""" 
Comandos para utilizar no terminal:
python -m venv venv - Criação de Ambiente de Trabalho
venv/Scripts/activate - Ativação do venv
"""
"""
Desabilitando segurança, comando no terminal: 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
"""
""" 
Instalação do flask:
pip install flask
"""
"""
Cuidados com os caminhos do Interpretador se colocar dentro de pastas entre repositorios.
É necessario indicar o caminho do Interpretador:
E:\Python Essential - Leonardo\Aula 04 - Flask\site\venv\Scripts\python.exe
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Rota raiz: Chama a função Index e retorna o formulario html.
@app.route('/')
def Index():
    return render_template('formulario.html')

# Metodo POST serve para guardar e inserir em outra página
@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form.get('nome')
    email = request.form.get('email')
    curso = request.form.get('curso')
    sexo = request.form.get('sexo')
    turno = request.form.getlist('turno')
    observacoes = request.form.get('observacoes')

    return render_template('resultado.html',
                           nome = nome,
                           email = email,
                           curso = curso,
                           sexo = sexo,
                           turno = turno,
                           observacoes = observacoes
                           )

if __name__ == '__main__':
    app.run(debug=True)

"""
Para rodar utilize o comando no terminal com o venv ativado:
python app.py
"""