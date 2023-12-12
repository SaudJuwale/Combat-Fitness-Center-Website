let barsbtn = document.getElementById('bars');
let cancelbtn = document.getElementById('cancel');
let navbar = document.getElementById('mob');


barsbtn.addEventListener("click",()=>{
    barsbtn.style.display = "none";
    cancelbtn.style.display = "block";
    navbar.style.marginTop  = "0px";
});

cancelbtn.addEventListener("click",()=>{
    barsbtn.style.display = "block";
    cancelbtn.style.display = "none";
    navbar.style.marginTop  = "-580px";
});
