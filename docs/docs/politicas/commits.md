## Padronização de Commits 

### Conventional Commits
Conventional Commits é uma especificação para criar mensagens de commit que sejam legíveis por humanos e máquinas, facilitando a colaboração e a manutenção de projetos.


### Formato
`<type>[scope]: <subject>`


### Exemplos
1. `docs: update README to add developer tips`
2. `feat[auth]: add password recovery flow`


### Explicação dos Campos

 **1. `type` (tipo)** 
Define o tipo de mudança realizada no commit. Os valores mais comuns incluem:

- **feat**: Uma nova funcionalidade.
- **fix**: Correção de um bug.
- **docs**: Mudanças apenas na documentação.
- **style**: Alterações que não afetam a lógica do código (espaço em branco, formatação, etc.).
- **refactor**: Alteração no código que não adiciona funcionalidades nem corrige bugs.
- **test**: Adição ou correção de testes.
- **chore**: Alterações em ferramentas ou processos auxiliares (ex.: scripts de build).
- **perf**: Mudança que melhora o desempenho do código.
- **ci**: Alterações nas configurações de integração contínua (CI).
- **build**: Alterações no sistema de build ou dependências externas.
- **temp**: Commit temporário que será removido e não entrará no changelog.


 **2. `scope` (escopo)**

- **Opcional**.
- Especifica a área ou módulo impactado pela mudança. Exemplos:

  - `[auth]` para mudanças relacionadas à autenticação.
  - `[api]` para alterações na API.
  - `[dashboard]` para o painel administrativo.


 **3. `subject` (assunto)**
- Um resumo breve e claro da mudança, escrito em **tempo presente**.

- **Regras**:
  - **Escreva no presente** (ex.: *add*, *fix*, *update*).
  - **Minúsculo** no início.
  - **Sem ponto final** ao final da frase.


## Benefícios
- Melhor legibilidade e consistência em projetos colaborativos.
- Facilita a geração de changelogs automáticos.
- Simplifica o entendimento do histórico de commits e as áreas impactadas.

---

Tabela de Versionamento

| Versão | Data       | Descrição                                                     | Autor(es)        |
|--------|------------|---------------------------------------------------------------|------------------|
| 1.0    | 09/12/2024 | Criação inicial                       | Laryssa Felix |
| 1.1    | 11/12/2024 | Crorreções                            | Laryssa Felix |