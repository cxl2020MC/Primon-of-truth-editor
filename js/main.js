document.addEventListener("DOMContentLoaded", async (e) => {
    const main_content = document.querySelector(".main")
    let res = await api.check_login()
    if (res.username) {
        res = await api.get_juqin()
        if (res.ok) {
            let data = await res.json()
            console.log(data)
            data = data.data
            for (let i = 0; i < data.length; i++) {
                let div = document.createElement("div")
                div.className = "juqin"
                div.innerHTML = ``
                main_content.appendChild(div)
            }
        }
    }
})