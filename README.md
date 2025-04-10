# 🧠 compair - Commit Pairing (Human x AI)

> Comparando mensagens de commit geradas por humanos e por modelos de linguagem

- **Lucca Carvalho Augusto**

---

## 🎯 Objetivo do trabalho

Este trabalho tem como objetivo investigar a qualidade e a percepção de mensagens de commit geradas por modelos de linguagem (LLMs) em comparação com mensagens escritas por humanos. A proposta é entender se essas mensagens geradas automaticamente são suficientemente boas para uso prático em desenvolvimento de software, considerando aspectos como clareza, identificação de autoria e preferência de programadores.

---

## 🧪 Metodologia

### 🤖 Modelo de linguagem que será usado

Serão utilizadas de duas a quatro LLMs com diferentes arquiteturas e propósitos, sendo algumas das candidatas:

- ChatGPT (OpenAI)
- Gemini (Google)
- Ollama (modelo local)
- DeepSeek
- [Outros modelos podem ser incluídos conforme disponibilidade]

Todas receberão o **mesmo prompt padronizado** para garantir uniformidade na geração das mensagens.

---

### 🗃️ Dataset

- Serão criados **commits em sistemas dummy simples**, com criações ou alterações claras, curtas e de fácil compreensão.
- Para cada commit:
    - De 1 a 2 humanos escreverão mensagens de commit.
    - De 2 a 4 LLMs também gerarão mensagens.
- Cada item do dataset conterá:
    - O diff do commit (em código)
    - De 4 a 6 mensagens de commit (sem identificação da origem)
- Os sistemas serão construídos com critérios como:
    - Serem pequenos e com escopo bem definido
    - Utilizarem boas práticas e estilo comum de desenvolvimento
    - Diversidade de tipos de alteração (bugfix, refactor, feature, etc.)

---

### ✍️ Exemplos preliminares de prompts

Prompt de exemplo para alteração:
> A seguir está uma alteração de código. Escreva uma mensagem de commit clara, concisa e seguindo boas práticas.
>
> Código antigo:
> ```python
> def soma(a, b):
>   return a+b
> ```
> Código novo:
> ```python
> def soma(a: int|float, b: int|float) -> float:
>   return float(a+b)
> ```

Prompt de exemplo para criação:
> A seguir está uma adição de código. Escreva uma mensagem de commit clara, concisa e seguindo boas práticas.
>
> Código novo:
> ```python
> def soma(a, b):
>   return a+b
> ```

Exemplos em uso no ChatGPT: https://chatgpt.com/share/67f7b6cc-51b4-8005-af83-f478fcec1362

---

### 📊 Avaliação quantitativa

- Será aplicado um formulário a vários programadores com as seguintes perguntas:
    1. Marque todas as mensagens de commit que você acredita terem sido feitas por seres humanos.
    2. Marque qual mensagem de commit você julga ser a melhor.
- As respostas serão coletadas e analisadas estatisticamente para identificar:
    - Se existe correlação entre a mensagem escolhida como "melhor" e a percepção de que foi feita por um humano.
    - Se existe diferença significativa entre mensagens preferidas geradas por humanos e por IA.
    - A taxa de acerto na identificação correta da autoria (humano vs IA).

---

### 🧠 Avaliação qualitativa

Além da análise estatística, será avaliada a **qualidade percebida** das mensagens geradas por LLMs, com foco em:

- Clareza e objetividade da mensagem
- Coerência com a alteração realizada no código
- Uso de boas práticas na escrita de commits
- Potencial de uso real no dia a dia de desenvolvimento

A partir desses dados, será discutida a **relevância prática** da diferença entre mensagens humanas e geradas. Ainda que as mensagens humanas sejam superiores, avalia-se se as mensagens de IA já atingem um patamar aceitável para uso cotidiano, com possível economia de tempo e esforço por parte dos desenvolvedores.

---

## 📌 Licença

Este projeto é acadêmico e não possui fins comerciais.

---
