# Releases do fork

A aplicação recebe uma versão conjunta, registrada em `version.txt` e `.release-please-manifest.json`. Backend e frontend usam a mesma tag de imagem. As versões internas de `package.json` e `pyproject.toml` não são atualizadas por esta estratégia genérica.

O ponto de partida é 1.0.0, já declarado nos componentes. `bootstrap-sha` delimita o histórico inicial; ele não cria uma tag nem uma release retroativa. O próximo incremento depende dos Conventional Commits posteriores. Não altere manualmente o manifesto para simular uma release já publicada.

## Fluxo

1. Abra um PR com uma alteração real e título Conventional Commits.
2. Após o merge em `main`, a qualidade valida o commit com PostgreSQL, build, Semgrep, Bandit, Trivy e o diagnóstico ZAP.
3. Release Please abre ou atualiza o PR de release, com changelog e versão.
4. Após revisar e mesclar esse PR, uma nova validação precede a criação da tag.
5. O workflow confere que a tag aponta para o commit validado. Só então chama a publicação compartilhada: quatro imagens escaneadas, dois manifests AMD64/ARM64 e tags versionadas no GHCR.

O fork usa exclusivamente esse fluxo para publicar: `ci.yml` não mantém o publicador legado. Não haverá um segundo push concorrente disparado pelo mesmo merge.

## Configuração do GitHub

Habilite Actions no fork e permita que Actions criem PRs em Settings → Actions → General. Os YAMLs concedem apenas as permissões necessárias por job; não é necessário conceder `write-all` como padrão.

O `GITHUB_TOKEN` não dispara automaticamente workflows a partir dos PRs que ele próprio cria. Antes de mesclar o PR de release, um mantenedor pode fechá-lo e reabri-lo pela interface para disparar a CI. Para automação completa, configure uma GitHub App com permissões mínimas e adapte o token do Release Please; não desative os checks obrigatórios para contornar essa limitação.

Proteja `main` com PR e o check **CI gate**, selecionando o nome efetivamente exibido no GitHub. Proteja também as tags de release contra exclusão/alteração. Ajuste a visibilidade dos dois pacotes no GHCR se a entrega precisar permitir download público.

## Recuperação e rollback

Primeiro use **Re-run failed jobs**, que preserva os resultados dos jobs bem-sucedidos. Se os artefatos de imagem tiverem expirado, execute **Release and publish** manualmente em `main`, informando uma tag de release já existente. O workflow rejeita tags inexistentes, releases em rascunho e commits fora do histórico de `main`; ele revalida o commit da tag antes de reconstruir.

Essa recuperação reescaneia as imagens e não atualiza `latest`, evitando promover acidentalmente uma versão antiga. Tags de imagens podem receber novos digests em reconstruções, pois as bases Docker ainda usam tags e a base de CVEs muda. Fixe digests nos deployments para garantir rollback exato.

Uma release no GitHub não comprova publicação bem-sucedida. Verifique o job de publicação e os dois manifests. Em falha parcial, mantenha o deployment anterior e repita a publicação; o GHCR não oferece transação entre os pacotes.
