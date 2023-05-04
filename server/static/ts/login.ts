const error = () =>{
    const error = document.getElementById("loginError") as HTMLElement
    
    setTimeout(()=>{
        error.style.opacity = " 0"
        error.style.transition = 'opacity 1s ease-out'
    }, 2000)
}

error()