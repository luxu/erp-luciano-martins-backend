# **Projeto Backend para o Pipoca Ágil**

# Para começar
* Crie um virtualenv com Python.

#### Windows

``python -m venv .venv``

* Ative o virtualenv.
#### Windows
`` .venv/Scripts/activate``

OBS: À partir de agora que acessou a virtualenv todos os comandos dentro dela só precisa usar **python e pip**

* Instale as dependências.

``pip install -r requirements.txt``

* Gerar o arquivo o *.env*

``python contrib/env_gen.py``

* Fazer as alterações necessárias

* Rode as migrações.

```python manage.py migrate```

* Criar um usuário padrão

``python manage.py createsuperuser``

* Rode a aplicação

``python manage.py runserver``