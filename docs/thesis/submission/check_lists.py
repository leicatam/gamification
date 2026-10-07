import sys,re,subprocess,docx
DOCX,PDF=sys.argv[1],sys.argv[2]
pages=subprocess.run(['pdftotext','-layout',PDF,'-'],capture_output=True,text=True).stdout.split('\f')
def norm(s): return re.sub(r'\s+',' ',s).strip()
pn=[norm(p) for p in pages]
def printed(pg):
    lines=[l.strip() for l in pg.strip().split('\n') if l.strip()]
    for l in reversed(lines[-3:]):
        m=re.fullmatch(r'(\d{1,3}|[ivxlc]{1,6})',l)
        if m: return m.group(1)
    return None
def is_hit(i,key):
    pg=pn[i]
    if pg.startswith(key): return True
    k=pg.find(key)
    while k>=0:
        if not re.search(r'\.{4,}',pg[k+len(key):k+len(key)+150]): return True
        k=pg.find(key,k+1)
    return False
d=docx.Document(DOCX); P=d.paragraphs
bad=0; total=0
for p in P:
    if not p.style.name.startswith('toc') or '\t' not in p.text: continue
    text,num=p.text.rsplit('\t',1); total+=1
    front=not num.isdigit()
    found=None
    for L in (90,45):
        key=norm(text)[:L]
        for i in range(len(pn)):
            if key in pn[i] and is_hit(i,key):
                pr=printed(pages[i])
                if pr is None: continue
                if front and pr.isdigit(): continue
                if not front and not pr.isdigit(): continue
                found=pr; break
        if found: break
    if found!=num:
        bad+=1; print(f"MISMATCH listed {num:>5}  actual {str(found):>5}  {text[:70]}")
print(f"{total} entries, {bad} mismatches")
