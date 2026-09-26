# URLs externas, OAuth e Web3 (hardcoded no main.js)

## OAuth Google
- Client ID: `1005568560502-6hm16lef8oh46hr2d98vf2ohlnj4nfhq.apps.googleusercontent.com`
- Auth: `https://accounts.google.com/o/oauth2/v2/auth`
- Userinfo: `https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=<TOKEN>`
- Pentest: fluxo OAuth do Juice Shop cria/loga usuario a partir do email Google. 
  A **senha** do usuario OAuth = base64 do email **invertido** (truque classico do Juice Shop). 
  Ex: email `bjoern.kimminich@gmail.com` -> inverter string -> base64 -> senha. Permite login normal na conta OAuth.

## Enderecos blockchain / crypto (desafios web3)
- BTC: `1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm`
- ETH: `0x0f933ab9fcaaa782d0279c300d73750e1311eae6`
- Dash: `Xr556RzuwX6hg5EGpkybbv5RanJoZN17kW`
- NFT (Mumbai testnet): contrato `0xf4817631372dca68a25a18eb7a0b36d54f3dbcf7`
- OpenSea testnet: `0x8343d2eb2B13A2495De435a1b15e85b98115Ce05`
- `ponzico.win/ponzico.pdf` (desafio do contrato Ponzi)

## Parametro de REDIRECIONAMENTO (open redirect)
No bundle: `redirect?to=http...` / `redirect?to=https...`
- Endpoint `/redirect?to=<url>` so aceita URLs de uma allowlist (as de cima). 
- **Open redirect challenge**: colar uma URL permitida no meio: 
  `/redirect?to=https://foo.bar/?x=https://github.com/juice-shop/juice-shop` (bypass da validacao "contem string permitida").

## Outras URLs (baixo risco, so referencia)
github.com/juice-shop/juice-shop, owasp-juice.shop, twitter/bsky/mastodon share, leanpub, spreadshirt.
