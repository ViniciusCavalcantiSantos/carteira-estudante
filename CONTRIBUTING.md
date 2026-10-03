# Guia de contribuição

Obrigado por contribuir com o Carteira do Estudante. Estas orientações ajudam a manter as alterações revisáveis e rastreáveis.

## Fluxo de trabalho

1. Atualize sua branch `main` antes de começar.
2. Crie uma branch para a alteração; não faça commits diretamente em `main`.
3. Abra um Pull Request e preencha o template, incluindo a issue relacionada e as validações executadas.
4. Aguarde os checks e a revisão antes do merge.

Use nomes descritivos, por exemplo `feat/student-search`, `fix/login-validation`, `ci/harden-workflow` ou `docs/contributing-guide`.

## Commits

Use Conventional Commits no formato `<tipo>(<escopo opcional>): <descrição>`.

Exemplos:

- `feat(api): adiciona consulta de movimentações`
- `fix(frontend): corrige validação do formulário de login`
- `ci(actions): fixa versão da action do Trivy`
- `docs: documenta o fluxo de contribuição`

## Validação local

Execute as verificações relevantes para os arquivos alterados. Para subir a aplicação com Docker Compose, configure o `.env` local a partir do `.env.example` e execute `docker compose up --build`. Não versione `.env` nem inclua credenciais ou dados pessoais nos logs e nas issues.

Para validar componentes individualmente:

- Backend: `docker compose exec backend ruff check .` e `docker compose exec backend pytest`.
- Frontend: em `frontend/`, execute `npm ci` e `npm run lint --if-present`.

Inclua no Pull Request os comandos executados e seus resultados. Se uma validação não se aplicar, explique o motivo.

## Revisão e segurança

- Mantenha cada Pull Request focado e vinculado a uma issue quando aplicável.
- Não inclua tokens, senhas, chaves privadas ou dados pessoais.
- Avalie dependências novas e atualizações relevantes.
- Aguarde a aprovação dos responsáveis indicados em `CODEOWNERS` e a aprovação dos checks antes do merge.
