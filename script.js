
document.addEventListener('click', e => {
  if (e.target.matches('.btn.primary')){
    e.target.innerText = 'Added ✓';
    setTimeout(()=> e.target.innerText = 'Add to cart', 900);
  }
});
