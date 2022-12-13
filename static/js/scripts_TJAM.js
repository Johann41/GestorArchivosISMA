const listarTipos=async(idInstancia)=>{
    try{
        const response = await fetch(`./tipos/${idInstancia}`)
        const data = await response.json()
        console.log(data)        
        if(data.msg==="Success"){
            tipo.removeAttribute('disabled')
            let opciones=''
            data.tipos.forEach(tipo => {
                opciones+=`<option  value='${tipo.id}'>${tipo.tipo}</option>`          
            });
            tipo.innerHTML=opciones       
        }else{
            tipo.setAttribute('disabled',"")
        }
    }catch(error){
        console.log(error)
    }
}

const listarNumeros=async(idInstancia)=>{
    try{
        const response = await fetch(`./numeros/${idInstancia}`)
        const data = await response.json()
        // console.log(data)        
        if(data.msg==="Success"){
            numero.removeAttribute('disabled')
            let opciones=''
            data.numeros.forEach(numero => {
                opciones+=`<option   value='${numero.id}' >${numero.numero}</option>`          
            });
            numero.innerHTML=opciones       
        }else{
            numero.setAttribute('disabled',"")
        }
    }catch(error){
        console.log(error)
    }
}


const listar_instancias=async()=>{
    try{
        const response = await fetch("./instancias")
        const data = await response.json()
        // console.log(data)        
        if(data.msg==="Success"){
            let opciones=''
            data.instancias.forEach(instancia => {
                opciones+=`<option value='${instancia.id}'>${instancia.nombre}</option>`          
            });
            instancia.innerHTML=opciones
            listarNumeros(data.instancias[0].id)
            listarTipos(data.instancias[0].id)
        }else{
            alert('instancias no encontradas')
        }
    }catch(error){
        console.log(error)
    }
}

const cargaInicial=async()=>{
    await listar_instancias()
    instancia.addEventListener("change", (event)=>{
        // console.log(event)
        // console.log(event.target)
        // console.log(event.target.value)
        listarNumeros(event.target.value)
    })
    instancia.addEventListener("change", (event)=>{
        listarTipos(event.target.value)
    })
}

window.addEventListener("load", async()=>{
    cargaInicial()
})