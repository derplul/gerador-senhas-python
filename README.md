# 🛡️ Gerador de Senhas em Python

## ✨ Sobre o Projeto
Este é um script simples e direto desenvolvido em Python para **criar senhas seguras e aleatórias**. 

A ferramenta permite que você escolha:
1.  O **tamanho** exato que sua senha deve ter.
2.  O **nível de complexidade** que você precisa (de apenas letras até incluir números e símbolos).

---

## ⚙️ Como Funciona a Complexidade

| Nível | Caracteres Incluídos | Sugestão de Uso |
| :--- | :--- | :--- |
| **1** | Letras (A-Z, a-z) | Testes e Senhas muito básicas. |
| **2** | Letras e Números (0-9) | Nível de segurança médio. |
| **3** | **Letras, Números e Símbolos** | **Máxima segurança (Recomendado).** |

---

## 🚀 Como Executar

Para rodar o gerador no seu computador, siga estes passos:

1.  **Pré-requisito:** Tenha o Python 3 instalado.
2.  **Execute o Arquivo:** Abra o terminal na pasta do projeto e use o comando:
    ```bash
    python gerador_senhas.py
    ```
3.  **Interaja:** O programa solicitará o nível de complexidade e o tamanho da senha.

### Exemplo de Uso
```bash
$ python gerador_senhas.py
Bem-vindo ao Gerador de Senhas!
...
Digite o nível de complexidade (1, 2 ou 3): 3
Digite o tamanho desejado para a senha: 12
Aqui está a sua senha gerada: A3!k@7xP9$oW
