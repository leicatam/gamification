# Figures I.2 and I.3 (V47): Batch 01 values as reported (20 Sep 2026) plus PFWU9V from its raw export.
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import sys
out=sys.argv[1]
def save(fig,name,ref):
    W,H=Image.open(ref).size; fig.set_size_inches(W/200,H/200); fig.tight_layout(); fig.savefig(out+name,dpi=200)
    im=Image.open(out+name)
    if im.size!=(W,H): im.resize((W,H),Image.LANCZOS).save(out+name)
# ---- I.2 pace chains
fig,ax=plt.subplots()
P=[(3,1.20,'x'),(4,1.08,'L'),(5,1.08,'L'),(6,1.08,'L'),(7,1.18,'L'),(8,1.18,'L'),(9,1.06,'L')]
T=[(3,1.20,'x'),(4,1.30,'O'),(5,1.40,'O'),(6,1.50,'L'),(7,1.60,'O')]
F=[(3,0.68,'x'),(4,0.56,'L'),(5,0.66,'L')]
for data,c,lab in [(P,'#1f77b4','P8P2Z9, visit 1 (six chains, all local rule)'),(T,'#d62728','PT8FJC, visit 1 (four chains: three player overrides, one local rule)'),(F,'#2ca02c','PFWU9V, visit 1 (two chains, both local rule)')]:
    ax.plot([d[0] for d in data],[d[1] for d in data],color=c,lw=1.6,label=lab)
    for x,y,k in data:
        if k=='x': ax.plot(x,y,'x',color=c,ms=7,mew=1.8)
        elif k=='L': ax.plot(x,y,'o',color=c,ms=7)
        else: ax.plot(x,y,'o',mfc='white',mec=c,mew=1.8,ms=7)
ax.plot([],[],'o',color='k',label='filled: local-rule decision'); ax.plot([],[],'o',mfc='white',mec='k',label='open: player override')
ax.plot([],[],'x',color='k',label='×: first practice run (warm-up setting)')
ax.set_ylim(0.4,1.75); ax.set_xticks(range(3,10)); ax.set_xlabel('Practice run within visit 1 (exported Session_No)',fontsize=9)
ax.set_ylabel('Pace multiplier',fontsize=9); ax.legend(fontsize=6.5,frameon=False,loc='lower right',ncol=1)
for s in ('top','right'): ax.spines[s].set_visible(False)
save(fig,'fig_I_2_pro_pace_chains_v47.png','docs/thesis/figures/fig_I_2_pro_pace_chains.png'); plt.close(fig)
# ---- I.3 paired checks
fig,ax=plt.subplots()
pairs=[('P8P2Z9 / 1',100,90,'#1f77b4','o','-',0),('PT8FJC / 1',95,100,'#2ca02c','s','-',0),('PEVNZ8 / 1',95,90,'#d62728','^','-',0),
('PZTPCG / 1',100,100,'#9467bd','D','-',0),('P8P2Z9 / 4',80,90,'#1f77b4','o','--',-0.02),('PFWU9V / 1 (received 29 Sep)',80,90,'#ff7f0e','v',':',0.02)]
for lab,a,b,c,m,ls,j in pairs:
    ax.plot([0+j,1+j],[a,b],color=c,marker=m,ls=ls,lw=1.8,ms=7,label=f'{lab}: {a}% → {b}% ({b-a:+d} pp)')
ax.axhline(100,color='grey',ls=':',lw=0.8); ax.text(1.06,100,'ceiling 100%',va='center',fontsize=7,color='#555')
ax.set_xticks([0,1]); ax.set_xticklabels(['Opening check','Closing check']); ax.set_xlim(-0.2,1.4); ax.set_ylim(75,103)
ax.set_ylabel('Obstacle clearance (%)',fontsize=9)
ax.set_title('Six within-visit fixed-course pairs (five stored codes)',fontsize=9)
ax.legend(fontsize=6.5,frameon=False,loc='upper center',bbox_to_anchor=(0.5,-0.12),ncol=2)
for s in ('top','right'): ax.spines[s].set_visible(False)
save(fig,'fig_I_3_pro_paired_checks_v47.png','docs/thesis/figures/fig_I_3_pro_paired_checks.png')
