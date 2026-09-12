const budget=document.getElementById('budget');const budgetValue=document.getElementById('budgetValue');const results=document.getElementById('results');const resultList=document.getElementById('resultList');
function money(n){return new Intl.NumberFormat('fa-IR').format(n)+' تومان'}
budget.addEventListener('input',()=>budgetValue.textContent=money(Number(budget.value)));
const demoProducts=[
 {name:'Samsung Galaxy A56',price:28900000,score:94,reason:'Strong camera, battery and balanced performance'},
 {name:'Xiaomi Redmi Note 14 Pro',price:24900000,score:91,reason:'Excellent value and display for your priorities'},
 {name:'Poco X7 Pro',price:27900000,score:88,reason:'Excellent performance and battery for gaming'}
];
document.getElementById('findBtn').addEventListener('click',()=>{resultList.innerHTML=demoProducts.map((p,i)=>`<article class="result"><div class="rank">0${i+1}</div><div class="phone"><h3>${p.name}</h3><p>${money(p.price)} · ${p.reason}</p></div><div class="score"><strong>${p.score}% match</strong><div class="bar"><i style="width:${p.score}%"></i></div><div class="match-note">Based on your priorities</div></div></article>`).join('');results.classList.remove('hidden');results.scrollIntoView({behavior:'smooth',block:'start'})});
document.getElementById('resetBtn').addEventListener('click',()=>{budget.value=30000000;budget.dispatchEvent(new Event('input'));document.querySelectorAll('.priority-card select').forEach((s,i)=>s.value=[2,3,3,2,1,1][i]);results.classList.add('hidden')});
