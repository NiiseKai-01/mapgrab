
        let url = "";
        const q_inp = document.getElementById("q_inp");
        const gencard = document.getElementById("gencard");
        const resultcard = document.getElementById("resultcard");
        gencard.style.display = "none";
        resultcard.style.display = "none";

        let isDefault = false;
        q_inp.addEventListener("input", () => {
            isDefault = false;

            if (q_inp.value.trim() !== "") {
                console.log("Valid input");
            } else {
                console.log("Empty input");
            }
        });
        const defbtn = document.getElementById("defbtn");
        defbtn.addEventListener("click",()=>{
            isDefault = true;
            q_inp.value = "Cafes in Tokyo";
        })

        const edown = document.getElementById("edown");
        let exclpath = "";
        const cdown = document.getElementById("cdown");
        let csvpath = "";
        edown.addEventListener("click", ()=>{
            if (!exclpath) {
                alert("Generate data first!");
                return;
            }
            window.location.href = `/download/${exclpath}`;
        })
        cdown.addEventListener("click", ()=>{
            if (!csvpath) {
                alert("Generate data first!");
                return;
            }
            window.location.href = `/download/${csvpath}`;
        })

        const genbtn = document.getElementById("btn");
        genbtn.addEventListener("click",()=>{
            const query = q_inp.value;
            if(!query){
                alert("Enter input first!");
                return;
            }
            if(isDefault){
                url = `/generate?q=demoliveshowcase`;
            }
            else{
                url = `/generate?q=${encodeURIComponent(query)}`;
            }
            resultcard.style.display="none";
            gencard.style.display="flex";
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    exclpath = data.excel;
                    csvpath = data.csv;
                    gencard.style.display="none";
                    resultcard.style.display="flex";
                })
                .catch(error => {
                    console.error("Error:", error);
                });
        })