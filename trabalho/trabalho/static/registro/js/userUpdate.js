onload = function() {
    console.log('onload')
    document.getElementById('id_email').addEventListener('blur', function (e) {
        console.log('verificaEmail');
        var campoEmail = document.getElementById('id_email');
        console.log('Campo email = ' + campoEmail.value)
        xmlhttp = new XMLHttpRequest();
        xmlhttp.open('GET',
            '/accounts/verificaEmail' + "?email=" + encodeURIComponent(campoEmail.value),
            true);
        xmlhttp.onreadystatechange = function () {
            console.log("call back")
            if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var resposta = JSON.parse(xmlhttp.responseText);
                if(resposta.existe) {
                    campoEmail.style = "border: 1px solid #FF0000";
                    document.getElementById('idMsgErro').replaceChild(document.createTextNode("Email já cadastrado em outra conta"), document.getElementById('idMsgErro').firstChild);
                }
                else {
                    campoEmail.style= "border: 1px solid#00FF00";
                    document.getElementById('idMsgErro').replaceChild(document.createTextNode("Email disponível"), document.getElementById('idMsgErro').firstChild);
                }
            }
        }
        xmlhttp.send(null);
    });
}