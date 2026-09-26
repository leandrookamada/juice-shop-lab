# Endpoints da API (extraidos do main.js)

Base: `http://<host>/` (Juice Shop). Dois estilos: `/api/*` (CRUD auto via Sequelize) e `/rest/*` (logica custom).

## /api/* (CRUD - REST auto)
Cada um aceita GET/POST/PUT/DELETE. IDOR e mass-assignment comuns aqui.

| Endpoint | Uso pentest |
|---|---|
| api/Users | enumerar usuarios; registro com role=admin (mass assignment) |
| api/Products | listar produtos; SQLi no search |
| api/Feedbacks | feedback; XSS armazenado no campo comment |
| api/Complaints | upload arquivo (XXE / path traversal via arquivo) |
| api/BasketItems | IDOR: alterar basket de outro usuario |
| api/Cards | dados de cartao (IDOR) |
| api/Addresss | enderecos (IDOR) |
| api/Deliverys | metodos de entrega |
| api/Quantitys | so admin deveria alterar (broken access control) |
| api/Recycles | reciclagem |
| api/SecurityQuestions | perguntas de seguranca (enumerar) |
| api/SecurityAnswers | respostas (base p/ reset de senha) |
| api/Challenges | status dos desafios |
| api/Hints | dicas dos desafios |

## /rest/* (logica custom)
| Endpoint | Uso pentest |
|---|---|
| rest/user/login | login (SQLi no email: `' OR 1=1--`) |
| rest/user/change-password | troca sem checar senha atual (CSRF/broken auth) |
| rest/user/reset-password | reset via resposta de seguranca |
| rest/user/security-question | pega pergunta por email (enumeracao) |
| rest/user/whoami | vaza dados do usuario logado |
| rest/user/authentication-details/ | lista sessoes/tokens |
| rest/admin | area admin |
| rest/products/search | **SQL injection** (parametro q) |
| rest/basket/ | ver basket por id (IDOR) |
| rest/order-history | historico de pedidos |
| rest/track-order | rastreio (NoSQL injection classica) |
| rest/2fa/setup, /verify, /status, /disable | fluxo TOTP 2FA |
| rest/continue-code + /apply/ | codigo de continuidade (bypass p/ challenges) |
| rest/captcha, rest/image-captcha/ | captcha (bypass) |
| rest/chat | chatbot (SSTI / injection no bot) |
| rest/memories | photo wall (upload) |
| rest/wallet/balance | saldo carteira |
| rest/web3, rest/deluxe-membership | desafios web3 / deluxe |
| rest/saveLoginIp | header injection (X-Forwarded-For) |
| rest/languages, rest/country-mapping | i18n |
| rest/repeat-notification | notificacoes |

## Outros caminhos de arquivo
- `ftp/order_...`  -> diretorio FTP exposto (path traversal: `ftp/package.json.bak%2500.md`, poison null byte)
- `assets/public/images/uploads/` -> uploads
- `assets/i18n/` -> arquivos de traducao
