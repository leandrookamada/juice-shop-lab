# Cookies e Storage (client-side)

## Cookies (via CookieService / cookieWriterService)
| Cookie | Conteudo | Nota pentest |
|---|---|---|
| token | **JWT de sessao** | gravado tambem no localStorage. JWT assinado RS256 mas chave publica/`none` alg = forjar admin. Roubo via XSS. |
| welcomebanner_status | dismiss do banner | cosmetico |
| cookieconsent_status | consentimento | cosmetico |
| language | idioma escolhido | - |
| continueCode | codigo de progresso dos desafios | - |

Codigo relevante no bundle:
- `cookieService.get(...)`, `cookieService.put(...)`, `cookieService.remove(...)`
- `cookieWriterService.write(...)` / `readAllAsString()`  <- escreve cookie a partir de valor controlado
- Constantes: `COOKIE_OPTIONS`, `COOKIE_WRITER`, `welcomeBannerStatusCookieKey`

## localStorage / sessionStorage
- **localStorage['token']** = JWT (mesmo do cookie). Sem HttpOnly -> **XSS rouba a sessao**.
- localStorage guarda tambem: `bid` (basket id), `itemTotal`, `email`, dados de continue-code.
- sessionStorage: `totp_tmp_token` (token temporario no meio do fluxo 2FA -> alvo p/ pular 2FA).

## Implicacoes
1. Token em localStorage + cookie sem flags -> qualquer XSS (ver arquivo 5) = account takeover.
2. `bid`/`itemTotal` no client = manipulaveis -> alterar preco/quantidade (basta trocar valor e refazer request).
3. Decodificar o JWT (jwt.io) revela email/role. Testar `alg:none` e chave fraca.
