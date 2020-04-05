document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("#stoggle").onclick =   ()=>{
        const a  = document.querySelector("#stoggle-icon");
    if(a.innerHTML== "menu"){
        a.innerHTML = "clear";
    }
    else{
        a.innerHTML = "menu";
    }
    return false;

    }
});
