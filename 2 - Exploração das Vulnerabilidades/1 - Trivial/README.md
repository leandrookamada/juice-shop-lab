# Nível 1 — Trivial ★

Desafios do OWASP Juice Shop neste nível: 13

## Web3 Sandbox

**Categoria:** Broken Access Control

## Missing Encoding

**Categoria:** Improper Input Validation

## Repetitive Registration

**Categoria:** Improper Input Validation

## Zero Stars

**Categoria:** Improper Input Validation

## Mass Dispel

**Categoria:** Miscellaneous

## Privacy Policy

**Categoria:** Miscellaneous

## Score Board

**Categoria:** Miscellaneous

## Exposed Metrics

**Categoria:** Observability Failures

## Error Handling

**Categoria:** Security Misconfiguration

## Confidential Document

**Categoria:** Sensitive Data Exposure

## Outdated Allowlist

**Categoria:** Unvalidated Redirects

## Bonus Payload

**Categoria:** XSS

>

## DOM XSS

**Categoria:** XSS

> Para explorar essa vulnerabilidade passei a tag <iframe src="javascript:alert(`xss`)"> na área de pesquisa. O que aconteceu foi que: a aplicação execultou o que foi passado na tela, sem sanitização. O que é passado alí é pesquisado por uma função, essa função retorna/"cria" um elemento HTML em formato de uma tag <p>, porém, o que eu passei é outra tag HTML, ent quando esse elemento for criado, dentro da tag <p>, vai ser impresso o que eu passei.
