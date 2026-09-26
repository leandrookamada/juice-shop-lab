# Analise do main.js — OWASP Juice Shop

Analise estatica do bundle frontend (`main.js`, 1.8 MB, Angular via rolldown).
Objetivo: mapear superficie de ataque para o pentest do Juice Shop (lab proposital).

## Arquivos desta pasta
| Arquivo | Conteudo |
|---|---|
| `main.formatado.js` | copia do main.js formatada (prettier) para leitura |
| `1 - endpoints-api.md` | todos os endpoints `/api/*` e `/rest/*` + caminhos de arquivo (ftp, assets) |
| `2 - cookies-e-storage.md` | cookies, localStorage/sessionStorage, onde fica o token JWT |
| `3 - rotas-frontend.md` | rotas Angular (`#/administration`, `#/score-board`, ...) + roles |
| `4 - urls-externas-e-oauth.md` | OAuth Google (client_id), enderecos web3/crypto, open redirect |
| `5 - VULNERABILIDADES.txt` | **lista priorizada de vulnerabilidades** + como explorar cada uma |

## Como foi feito
Greps direcionados no bundle procurando: endpoints, sinks de XSS
(`bypassSecurityTrustHtml`), uso de storage/cookie do token, URLs
hardcoded, roles e slugs de rota. Tudo confirmado no proprio `main.js`.

## Aviso
main.js = SO o cliente. Ele revela o **mapa**, nao a falha em si.
Confirmar cada vulnerabilidade com request real (Burp) contra uma
instancia local do Juice Shop. Uso autorizado / educacional apenas.
