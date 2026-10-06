# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.1.0](https://github.com/ViniciusCavalcantiSantos/carteira-estudante/compare/v1.0.0...v1.1.0) (2026-10-06)


### Features

* **auth:** implement Google SSO backend, fix HSTS local cache issues and update docker-compose ([c6dbe85](https://github.com/ViniciusCavalcantiSantos/carteira-estudante/commit/c6dbe851cd118dae6cd964a152d53a5a7afb948c))
* **auth:** implement Google SSO backend, fix HSTS local cache issues, and update docker-compose ([6209c7e](https://github.com/ViniciusCavalcantiSantos/carteira-estudante/commit/6209c7e767512e86504f9542cd05e01aee1b2e1b))
* automate releases and multi-arch image publishing ([c503109](https://github.com/ViniciusCavalcantiSantos/carteira-estudante/commit/c503109253d77fc02739b0770571977d325bb439))
* **ci:** automate validated multi-arch releases ([d49062f](https://github.com/ViniciusCavalcantiSantos/carteira-estudante/commit/d49062f3355524dc9de2b22f8187e83efe7eb8af))
* **ci:** gate automated releases on validated container artifacts ([e6d6fb5](https://github.com/ViniciusCavalcantiSantos/carteira-estudante/commit/e6d6fb5acfd2c3043047af988a4f0085081e805f))

## [0.2.0] - 2026-09-19

### Adicionado
- Estrutura inicial do monorepo separando `frontend` (Next.js) e `backend` (FastAPI).
- Documentação da base do projeto na Wiki (Visão, Arquitetura, Modelagem, Segurança, Execução).
- Containerização dos serviços utilizando Docker e Docker Compose.
- Pipeline de CI/CD via GitHub Actions (Lint, Testes e Build Multi-arquitetura).
- Publicação automatizada da imagem Docker no GitHub Container Registry (GHCR).
- Configuração do Dependabot para análise contínua de vulnerabilidades.

### Segurança
- Substituição da biblioteca abandonada `python-jose` por `PyJWT` para mitigação de vulnerabilidade (High) na dependência transitiva `ecdsa`.
- Implementação da action do OWASP ZAP (DAST) na esteira de CI/CD para detecção dinâmica de vulnerabilidades no contêiner.
- Implementação do Bandit (SAST) na esteira de CI/CD para análise estática de segurança no código-fonte Python.
