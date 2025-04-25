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

Foi utilizado um dataset base de commits e suas mensagens, o [GitHub Commit Messages Dataset](https://www.kaggle.com/datasets/dhruvildave/github-commit-messages-dataset?resource=download)
A partir daí foram feitas duas principais modificações:
1. Redução de tamanho
   - Para utilizar um dataset menor e ter um controle maior, serão utilizadas apenas as instâncias do [scikit-learn](https://github.com/scikit-learn/scikit-learn)
2. Coleta do commit feito
   - Tendo o repositório e o _commit hash_ foi coletado o commit rodando o comando `git show COMMIT_HASH`, então foram removidas as primeiras linhas que contém a mensagem escrita pelo autor do commit, para não influencia na resposta da LLM, e outras informações inúteis como data e código hash 

---

### ✍️ Exemplos preliminares de prompts

Prompt de exemplo para as LLMs:
> The lines below are a commit into the scikit-learn repo, write a commit message clear, concise and following good-practices. Write only the title, without description.
>
> ```
> diff --git a/sklearn/manifold/tests/test_locally_linear.py b/sklearn/manifold/tests/test_locally_linear.py
> index 9d06c27fe..c9ca2f0d7 100644
> --- a/sklearn/manifold/tests/test_locally_linear.py
> +++ b/sklearn/manifold/tests/test_locally_linear.py
> @@ -36,7 +36,7 @@ def test_lle_simple_grid():
> rng = np.random.RandomState(0)
> # grid of equidistant points in 2D, out_dim = n_dim
> X = np.array(list(product(range(5), repeat=2)))
> -    X = X + 1e-10 * np.random.uniform(size=X.shape)
> +    X = X + 1e-10 * rng.uniform(size=X.shape)
>      out_dim = 2
>      clf = manifold.LocallyLinearEmbedding(n_neighbors=5, out_dim=out_dim)
>      tol = .1
> ```

Exemplos em uso no ChatGPT: https://chatgpt.com/c/680c11bf-ad8c-8005-96df-4e18585ed060

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
