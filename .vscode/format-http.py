import json, sys, re

path = sys.argv[1]
raw = open(path, 'rb').read().decode('utf-8')

# split headers/body on first blank line (CRLF or LF)
m = re.search(r'\r?\n\r?\n', raw)
if m:
    head, body = raw[:m.start()], raw[m.end():].strip()
else:
    head, body = raw, ''
head = head.replace('\r', '')

# drop any previously generated cookie-view block so we can regenerate it
lines = [ln for ln in head.split('\n') if not ln.startswith('#   ') and ln != '# Cookie (view):']

# expand Cookie header into a readable comment block right after it
out_lines = []
ctype = ''
for ln in lines:
    out_lines.append(ln)
    low = ln.lower()
    if low.startswith('content-type:'):
        ctype = low
    if low.startswith('cookie:'):
        val = ln.split(':', 1)[1].strip()
        out_lines.append('# Cookie (view):')
        for pair in val.split('; '):
            out_lines.append('#   ' + pair)
head = '\n'.join(out_lines)

# beautify body by type
def beautify(body, ctype):
    try:
        return json.dumps(json.loads(body), indent=2, ensure_ascii=False)
    except json.JSONDecodeError:
        pass
    try:
        import jsbeautifier
        opts = jsbeautifier.default_options()
        opts.indent_size = 2
        if 'html' in ctype:
            from jsbeautifier import html
            return html.beautify(body)
        if 'css' in ctype:
            from jsbeautifier import css
            return css.beautify(body)
        return jsbeautifier.beautify(body, opts)  # js / default
    except Exception:
        return body  # leave untouched if anything fails

if body:
    out = head + '\n\n' + beautify(body, ctype) + '\n'
else:
    out = head + '\n'

open(path, 'w', encoding='utf-8', newline='\n').write(out)
