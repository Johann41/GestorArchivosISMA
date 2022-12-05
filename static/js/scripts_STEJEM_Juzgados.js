const lista_areas_juzgados = async (IdDisrito)=>{
    try {
        const response = await fetch(`./juzgados/distritos/${IdDisrito}`)
        const data = await response.json()
        console.log(data)        
        if(data.msg==="Success"){
            let opciones=''
            data.areas.forEach(area => {
                opciones+=`<option value='${area.id}'>${area.nombre}</option>`          
            });
            areaJuzgados.innerHTML=opciones       
        }else{
            alert('areas no encontrados')
        }

    } catch (error) {
        console.log(error)
    }
}

const lista_distridos = async () =>{
    try {      
        const response = await fetch("./juzgados/distritos")
        const data = await response.json()

        if(data.msg === "Success"){
            let opciones = ''
            data.distritos.forEach( distrito => {
                opciones+=`<option value='${distrito.id}'>${distrito.nombre}</option>`
            })
            distrito.innerHTML=opciones
            lista_areas_juzgados(data.distritos[0].id)
        }else{
            alert('distritos no encontrados')
        }

    } catch (error) {
        console.log(error)
    }
}

const cargaInicial = async()=>{
    await lista_distridos()
    distrito.addEventListener("change", (event) =>{     
        lista_areas_juzgados(event.target.value)
    })
    
}

window.addEventListener("load", async()=>{
    cargaInicial()
})

if (window.history.replaceState) { // verificamos disponibilidad
    window.history.replaceState(null, null, window.location.href);
}