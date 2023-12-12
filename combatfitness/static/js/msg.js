let cancel = document.getElementById('cancelms');

if (document.getElementById('success') == 'success'){
    if (document.getElementById('msg').innerHTML == ""){
        document.getElementById('success').style.display  = "none";
    }else{
        document.getElementById('success').style.display  = "flex";
    }
}
else if (document.getElementById('error') == 'error'){
    if (document.getElementById('msg').innerHTML == ""){
        document.getElementById('error').style.display  = "none";
        console.log('inside this ')
    }else{
        document.getElementById('error').style.display  = "flex";
        console.log('inside this not')
    }
} 

cancel.addEventListener('click',()=>{
    document.getElementById('success').style.display  = "none";
});    

cancel.addEventListener('click',()=>{
    document.getElementById('error').style.display  = "none";
});
 



