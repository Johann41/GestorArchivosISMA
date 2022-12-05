

const listar_salas = async () =>{
    try {
        const response = await fetch("./salas/areas")
        const data = await response.json()

        if(data.msg==="Success"){
            let opciones=''
            data.areas.forEach(area => {
                opciones+=`<option style="font-size:16px;" value='${area.id}'>${area.nombre}</option>`
            });
            area.innerHTML=opciones
        }else{
            alert('areas no encontradas')
        }
    } catch (error) {
        console.log(error)
    }
}

const cargaInicial = async()=>{
    await listar_salas()
}

window.addEventListener("load", async()=>{
    cargaInicial()
})

if (window.history.replaceState) { // verificamos disponibilidad
    window.history.replaceState(null, null, window.location.href);
}