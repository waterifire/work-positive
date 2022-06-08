let personPlace = document.getElementsByClassName('.person_place')

var active, prev, next

active = prev = next = document.querySelector('.center')

do prev = prev.previousSibling; while(prev && prev.nodeType !== 1);
do next = next.nextSibling; while(next && next.nodeType !== 1);


// Example ###########################################################

active.addEventListener('click', show_them)

function show_them() {
  prev.classList.remove('hide_me')
  next.classList.remove('hide_me')
  active.classList.add('fat_me_up')
  active.removeEventListener('click', show_them)
  active.addEventListener('click', hide_them)
}

function hide_them() {
  prev.classList.add('hide_me')
  next.classList.add('hide_me')
  active.classList.remove('fat_me_up')
  active.removeEventListener('click', hide_them)
  active.addEventListener('click', show_them)
}
