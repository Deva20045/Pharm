let order=[],idx=0,xpGain=0,streak=0,correct=0,wrongList=[],locked=false;
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function kindOf(q){return q.type||'mcq';}
function typeLabel(k){return k==='fill'?'FILL':k==='match'?'MATCH':'CHOOSE';}
function revealAnswer(q){
  const k=kindOf(q);
  if(k==='fill') return q.blank;
  if(k==='match'){
    const ans=Array.isArray(q.ans)?q.ans:q.left.map((_,i)=>i);
    return q.left.map((L,i)=>L+' → '+q.right[ans[i]]).join(' · ');
  }
  return q.opts[q.ans];
}
function beginUnit(){
  order=curUnit.qs.map(id=>{
    const q=QBYID[id];
    const k=kindOf(q);
    if(k==='fill') return {q,kind:'fill'};
    if(k==='match'){
      const ans=Array.isArray(q.ans)?q.ans.slice():q.left.map((_,i)=>i);
      const right=q.right.map((t,i)=>({t,i}));
      shuffle(right);
      return {q,kind:'match',right,ans,chosen:Array(q.left.length).fill(null),sel:null};
    }
    return {q,kind:'mcq',opts:shuffle(q.opts.map((t,i)=>({t,ok:i===q.ans})))};
  });
  idx=0;xpGain=0;streak=0;correct=0;wrongList=[];
  show('quiz');renderQ();
}
function markResult(ok, el, msgBad){
  locked=true;
  const cur=order[idx], q=cur.q;
  const fb=$('fb');
  if(ok){
    correct++;streak++;
    const gain=10+Math.min(streak*2,10);xpGain+=gain;S.xp=S.xp+gain;
    if(el) floatText(el,'+'+gain+' XP','#e0607e');
    fb.className='fb show good';
    fb.innerHTML='✅ Correct! '+escapeHtml(q.exp);
  }else{
    streak=0;wrongList.push(q);
    fb.className='fb show bad';
    fb.innerHTML=msgBad;
  }
  refreshStats();
  $('nextBtn').classList.remove('hidden');
}
function renderQ(){
  locked=false;
  const cur=order[idx], q=cur.q, k=cur.kind;
  $('qbar').style.width=(idx/order.length*100)+'%';
  $('qcount').textContent='QUESTION '+(idx+1)+' OF '+order.length;
  $('qtag').innerHTML='<span class="qtype '+k+'">'+typeLabel(k)+'</span><span class="qsec">'+escapeHtml(q.sec)+' · Book p'+q.page+'</span>';
  const box=$('opts'); box.innerHTML='';
  $('fb').className='fb'; $('fb').innerHTML='';
  $('nextBtn').classList.add('hidden');
  $('nextBtn').textContent=idx===order.length-1?'Finish ✓':'Continue →';
  if(k==='fill') return renderFill(cur);
  if(k==='match') return renderMatch(cur);
  $('qtext').textContent=q.q;
  cur.opts.forEach(o=>{
    const b=document.createElement('button');b.className='opt';b.textContent=o.t;
    b.onclick=()=>answerMcq(o,b);box.appendChild(b);
  });
}
function renderFill(cur){
  const q=cur.q;
  $('qtext').innerHTML=escapeHtml(q.q).replace(/_{3,}/g,'<span class="blank">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>');
  const box=$('opts');
  const inp=document.createElement('input');
  inp.type='text'; inp.className='fillin'; inp.id='fillBox';
  inp.placeholder='Type the missing word / value';
  inp.autocomplete='off'; inp.autocapitalize='off'; inp.spellcheck=false;
  inp.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();submitFill();}});
  box.appendChild(inp);
  const btn=document.createElement('button'); btn.className='btn'; btn.textContent='Check answer';
  btn.onclick=submitFill; box.appendChild(btn);
  setTimeout(()=>inp.focus(),40);
}
function normFill(s){
  return String(s).toLowerCase()
    .replace(/,/g,'')
    .replace(/[–—−]/g,'-')
    .replace(/[μµ]/g,'u')
    .replace(/α/g,'a').replace(/β/g,'b').replace(/γ/g,'g')
    .replace(/[^a-z0-9+\-/%.\s]/g,' ')
    .replace(/\s+/g,' ')
    .trim();
}
function stripUnits(s){
  return s.replace(/\b(mg\/l|mg\/dl|mg\/kg|mg|mcg|ug|iu|hours?|hrs?|days?|weeks?|wks?|years?|yrs?|months?|min|minutes?|seconds?|sec|od|bd|tds|qid|percent|meq\/l|mmol\/l|ng\/ml)\b/g,'')
    .replace(/%/g,'')
    .replace(/\s+/g,' ').trim();
}
function fillMatches(q, input){
  const cands=[q.blank].concat(q.aliases||[]).map(normFill);
  const n=normFill(input);
  if(!n) return false;
  if(cands.includes(n)) return true;
  const ns=stripUnits(n);
  if(ns && cands.some(c=>stripUnits(c)===ns)) return true;
  if(cands.some(c=>c.replace(/ /g,'')===n.replace(/ /g,''))) return true;
  return false;
}
function submitFill(){
  if(locked) return;
  const cur=order[idx], q=cur.q;
  const inp=$('fillBox'); if(!inp) return;
  const ok=fillMatches(q, inp.value);
  inp.disabled=true;
  inp.classList.add(ok?'correct':'wrong');
  const msgBad='❌ Answer: <b>'+escapeHtml(q.blank)+'</b><br>'+escapeHtml(q.exp);
  markResult(ok, inp, msgBad);
}
function renderMatch(cur){
  $('qtext').textContent=cur.q.q;
  const box=$('opts'); box.innerHTML='';
  cur.q.left.forEach((L,i)=>{
    const row=document.createElement('div'); row.className='mrow';
    const left=document.createElement('div'); left.className='mleft'; left.textContent=L;
    const slot=document.createElement('button');
    const filled=cur.chosen[i]!=null;
    slot.className='mslot'+(filled?' filled':'')+(cur.sel===i?' sel':'');
    slot.type='button';
    slot.textContent=filled ? (cur.right.find(x=>x.i===cur.chosen[i])||{t:''}).t : 'Tap, then pick a match';
    slot.onclick=()=>{
      if(locked) return;
      if(cur.chosen[i]!=null){ cur.chosen[i]=null; cur.sel=i; }
      else cur.sel = cur.sel===i ? null : i;
      renderMatch(cur);
    };
    row.appendChild(left); row.appendChild(slot); box.appendChild(row);
  });
  const bank=document.createElement('div'); bank.className='mbank';
  cur.right.forEach(r=>{
    const used=cur.chosen.includes(r.i);
    const c=document.createElement('button'); c.type='button';
    c.className='chip'+(used?' used':''); c.textContent=r.t;
    c.onclick=()=>{
      if(locked||used) return;
      let t=cur.sel;
      if(t==null) t=cur.chosen.findIndex(x=>x==null);
      if(t<0) return;
      cur.chosen[t]=r.i; cur.sel=null;
      renderMatch(cur);
    };
    bank.appendChild(c);
  });
  box.appendChild(bank);
  if(!locked && cur.chosen.every(x=>x!=null)){
    const btn=document.createElement('button'); btn.className='btn'; btn.textContent='Check matches';
    btn.onclick=submitMatch; box.appendChild(btn);
  }
}
function submitMatch(){
  if(locked) return;
  const cur=order[idx], q=cur.q;
  const ok=cur.chosen.every((c,i)=>c===cur.ans[i]);
  locked=true;
  const slots=[...document.querySelectorAll('.mslot')];
  slots.forEach((s,i)=>{
    s.classList.add(cur.chosen[i]===cur.ans[i]?'correct':'wrong');
    s.disabled=true;
  });
  [...document.querySelectorAll('.chip')].forEach(c=>c.disabled=true);
  const chk=[...document.querySelectorAll('#opts > .btn')];
  chk.forEach(b=>b.remove());
  const msgBad='❌ '+escapeHtml(revealAnswer(q))+'<br>'+escapeHtml(q.exp);
  markResult(ok, slots[0]||null, msgBad);
}
function answerMcq(o,btn){
  if(locked)return;
  const cur=order[idx],q=cur.q,btns=$('opts').children;
  const rightIdx=cur.opts.findIndex(x=>x.ok);
  [...btns].forEach(b=>b.disabled=true);
  btns[rightIdx].classList.add('correct');
  if(!o.ok) btn.classList.add('wrong');
  const msgBad='❌ Answer: <b>'+escapeHtml(cur.opts[rightIdx].t)+'</b><br>'+escapeHtml(q.exp);
  markResult(o.ok, btn, msgBad);
}
function escapeHtml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function floatText(el,txt,color){
  const r=el.getBoundingClientRect(),s=document.createElement('div');
  s.className='float';s.textContent=txt;s.style.color=color;
  s.style.left=(r.left+r.width/2-24)+'px';s.style.top=(r.top-6+window.scrollY)+'px';
  document.body.appendChild(s);setTimeout(()=>s.remove(),1000);
}
function nextQ(){idx++;if(idx>=order.length)finishUnit();else renderQ();}
function finishUnit(){
  const d=S.done;if(!d.includes(curUnit.id)){d.push(curUnit.id);S.done=d;}
  S.bumpStreak();
  const pct=Math.round(correct/order.length*100);
  $('dSub').textContent=curUnit.title+' · '+correct+'/'+order.length+' correct';
  $('dScore').textContent=correct+'/'+order.length;
  $('dXP').textContent='+'+xpGain;$('dAcc').textContent=pct+'%';
  const box=$('dRev');box.innerHTML='';
  if(wrongList.length){const h=document.createElement('p');h.className='sub';h.textContent='Review:';box.appendChild(h);}
  wrongList.forEach(q=>{
    const r=document.createElement('div');r.className='rev';
    r.innerHTML='❓ '+escapeHtml(q.q)+'<br>✅ <b>'+escapeHtml(revealAnswer(q))+'</b> — '+escapeHtml(q.exp);
    box.appendChild(r);
  });
  show('unitdone');
}
function afterUnit(){nav.stack=['home','chapters','path'];render();}
function continueLearning(){
  const c=CHAPTERS.find(x=>x.live);
  if(!c)return;curCh=c.n;
  const us=unitsOf(c.n);
  const nxt=us.find(u=>unitState(u,us)==='current')||us[0];
  curUnit=nxt;nav.stack=['home'];openGuide(nxt);
}
function unlockAll(){S.unlock=true;render();}
document.addEventListener('keydown',e=>{
  if($('quiz').classList.contains('hidden'))return;
  if(!order.length)return;
  const cur=order[idx];
  if(e.key==='Enter'&&locked){nextQ();return;}
  if(cur && cur.kind==='mcq'){
    const k=parseInt(e.key);
    if(k>=1&&k<=4&&!locked){const b=$('opts').children[k-1];if(b)b.click();}
  }
});
render();
