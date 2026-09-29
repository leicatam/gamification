import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.dates as md, datetime as dt
S='/tmp/claude-0/-home-user-gamification/3d8a50e8-9258-51ce-a7d6-194da50f9a04/scratchpad/'
D=lambda m,d: dt.date(2026,m,d)
fig,ax=plt.subplots(figsize=(7,3.6),dpi=200)
rows={'Builds':2,'Distribution':1,'Returns':0}
C={'Builds':'#1f77b4','Distribution':'#2ca02c','Returns':'#d62728'}
ax.axvspan(D(9,15),D(10,15),ymin=0.02,ymax=0.36,color='#e8eff9',zorder=0)
ax.text(D(9,16),-0.8,'clean-run window 15 Sep – 15 Oct',ha='left',va='bottom',color='#3a6ea5',fontsize=7)
for y in rows.values(): ax.axhline(y,color='#cccccc',lw=1,zorder=1)
ev=[('Builds',D(8,8),'protocol 473046c/846a286',0.22,'center'),('Builds',D(8,9),'2×2 device set 59b7881; hierarchy 13a6e91',-0.2,'center'),
('Builds',D(8,13),'v3.1 revisions 923a25e/a1afc42',0.38,'center'),('Builds',D(9,15),'freeze 2f61e62 (FROZEN20260915)',-0.3,'center'),
('Builds',D(9,19),'Pro v4.1 self-test recorded',0.22,'center'),
('Distribution',D(8,9),'pitch (15:42 local)',-0.2,'center'),('Distribution',D(8,10),'DEV2 sent',0.36,'center'),('Distribution',D(8,12),'DEV1 sent',-0.35,'center'),
('Distribution',D(9,15),'D01–D20 copies',0.22,'center'),('Distribution',D(9,17),'hosted links',-0.2,'center'),
('Returns',D(8,15),'B9V8YA verified',0.36,'center'),('Returns',D(9,15),'five returns excluded',-0.3,'center'),
('Returns',D(9,19),'Pro Batch 01\nself-test',0.2,'right'),('Returns',D(9,26),'26 Sep decision: not the\nadaptive-learning test',0.36,'left'),
('Returns',D(9,29),'three clean-run\nreturns (D01)',-0.3,'left')]
for r,d,l,off,ha in ev:
    y=rows[r]; ax.plot(d,y,'o',color=C[r],ms=6,zorder=3)
    ax.plot([d,d],[y,y+off*0.8],color='#999999',lw=0.8,zorder=2)
    ax.text(d,y+off,l,ha=ha,va='bottom' if off>0 else 'top',fontsize=6.5)
ax.axvline(D(10,15),color='black',ls='--',lw=1.2)
ax.text(D(10,14),2.45,'thesis cut-off\n15 Oct',ha='right',fontsize=7)
ax.set_yticks(list(rows.values())); ax.set_yticklabels(list(rows.keys()),fontsize=10)
ax.set_ylim(-0.9,2.7); ax.set_xlim(D(8,3),D(10,20))
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=0)); ax.xaxis.set_major_formatter(md.DateFormatter('%d %b'))
ax.tick_params(axis='x',labelsize=7)
for s in ('top','right','left'): ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(S+'fig_I_1_v46.png',dpi=200)
