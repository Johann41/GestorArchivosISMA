const listar_tribunales=async()=>{
    try{
        const response = await fetch("./tribunales")
        const data = await response.json()
        // console.log(data)        
        if(data.msg==="Success"){
            let opciones=''
            data.tribunales.forEach(tribunal => {
                opciones+=`<option value='${tribunal.id}'>${tribunal.nombre}</option>`          
            });
            tribunal.innerHTML=opciones
        }else{
            alert('tribunales no encontrados')
        }
    }catch(error){
        console.log(error)
    }
}

const cargaInicial=async()=>{
    await listar_tribunales()    
}

window.addEventListener("load", async()=>{
    cargaInicial()
})