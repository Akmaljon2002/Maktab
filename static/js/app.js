let form = document.querySelector('.regst')
let join = document.querySelector('.but');
let clos = document.querySelector('.close');
let newsbtn = document.querySelector('.menuNews');
let mediabtn = document.querySelector('.menumedia');
let journalAll = document.querySelector('.journal__subject');
let first = document.querySelector('.classcalFirst');
let two = document.querySelector('.classcalTwo');
let three = document.querySelector('.classcalThree');
let four = document.querySelector('.classcalFour');
let all = document.querySelector('.classcalAll');
let perion = document.querySelector('.tab');
let perionTwo = document.querySelector('.tabTwo');
let perionThree = document.querySelector('.tabThree');
let perionFour = document.querySelector('.tabFour');
let perionAll = document.querySelector('.tabAll');


function one(){
    first.style.display = "block";
    two.style.display = "none";
    three.style.display= "none";
    four.style.display = "none";
    all.style.display = "none";
    perion.classList.add("active");
    perionTwo.classList.remove("active");
    perionThree.classList.remove("active");
    perionAll.classList.remove("active");
    perionFour.classList.remove("active");

}
function second(){
    first.style.display = "none";
    two.style.display = "block";
    three.style.display= "none";
    four.style.display = "none";
    all.style.display = "none";
    perion.classList.remove("active");
    perionTwo.classList.add("active");
    perionThree.classList.remove("active");
    perionAll.classList.remove("active");
    perionFour.classList.remove("active");

}
function third(){
    first.style.display = "none";
    two.style.display = "none";
    three.style.display= "block";
    four.style.display = "none";
    all.style.display = "none";
    perion.classList.remove("active");
    perionTwo.classList.remove("active");
    perionThree.classList.add("active");
    perionAll.classList.remove("active");
    perionFour.classList.remove("active");

}
function fourth(){
    first.style.display = "none";
    two.style.display = "none";
    three.style.display= "none";
    four.style.display = "block";
    all.style.display = "none";
    perion.classList.remove("active");
    perionTwo.classList.remove("active");
    perionThree.classList.remove("active");
    perionFour.classList.add("active");
    perionAll.classList.remove("active");

}
function Allteam(){
    first.style.display = "none";
    two.style.display = "none";
    three.style.display= "none";
    four.style.display = "none";
    all.style.display = "block";
    perion.classList.remove("active");
    perionTwo.classList.remove("active");
    perionThree.classList.remove("active");
    perionFour.classList.remove("active");
    perionAll.classList.add("active");

}



let btnHisobot = document.querySelector('.reports_panel_button')
let Hisobot = document.querySelector('#reportPlaceHolder');

const journal = () => {
    journalAll.style.display = "flex"
}
// btnHisobot.addEventListener('click', function(){
//     Hisobot.style.display = 'block';
// })

join.addEventListener('click', function(){
    form.style.display = 'block';
})
clos.addEventListener('click', function () {
   form.style.display = 'none';
    
})

