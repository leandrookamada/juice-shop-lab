# Rotas do Frontend (Angular) — paginas alcancaveis

Todas viram `http://<host>/#/<rota>`. Varias NAO tem protecao real (guard so client-side = burlavel).

## Rotas sensiveis / escondidas
| Rota | O que e | Pentest |
|---|---|---|
| #/administration | painel admin (lista clientes, feedback) | **guard so no client** — logar como qualquer user e navegar direto; precisa role admin no token p/ dados |
| #/score-board | placar de desafios | ponto de partida do CTF; achar a rota ja e 1 desafio |
| #/accounting | area contabilidade | requer role `accounting` |
| #/deluxe-membership | virar membro deluxe | manipular pagamento/wallet |
| #/wallet-web3 , #/web3-sandbox , #/juicy-nft | desafios web3/NFT | contratos: ver arquivo 4 |
| #/privacy-security/* | trocar senha, 2fa, data-export | data-export = vaza dados; change-password sem senha atual |
| #/complain | reclamacao + upload | XXE / upload malicioso |
| #/chatbot | bot "Juicy" | injection / vazar cupom |
| #/photo-wall (memories) | mural de fotos | upload, XSS em legenda |
| #/recycle | reciclagem | - |
| #/track-result , #/order-completion | rastreio pedido | IDOR / NoSQLi |
| #/data-export | exportar dados do usuario | CAPTCHA burlavel |

## Papeis (roles) referenciados no bundle
`'admin'`, `'accounting'`, `'deluxe'`, `'customer'` — checagem de role acontece no client (Angular). 
Broken Access Control: a decisao de mostrar/ocultar e client-side; o backend precisa validar de novo — testar chamando os `/rest` e `/api` direto com token de `customer`.

## Como enumerar tudo
No console do browser, o roteador Angular lista as rotas. Ou simplesmente varrer `#/<slug>` com os slugs deste arquivo.
