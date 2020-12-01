onload = function() {
    console.log('onload')
    document.getElementById('id_username').addEventListener('blur', function (e) {
        console.log('verificaUsername');
        var campoUsername = document.getElementById('id_username');
        console.log('Campo username = ' + campoUsername.value)
        xmlhttp = new XMLHttpRequest();
        xmlhttp.open('GET',
            '/accounts/verificaUsername' + "?username=" + encodeURIComponent(campoUsername.value),
            true);
        xmlhttp.onreadystatechange = function () {
            console.log("call back")
            if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var resposta = JSON.parse(xmlhttp.responseText);
								if(!resposta.vazio) {
									if(resposta.existe) {
											campoUsername.style = "border: 1px solid #FF0000";
											document.getElementById('idMsgErro').replaceChild(document.createTextNode("Usuário já existe"), document.getElementById('idMsgErro').firstChild);
									}
									else {
											campoUsername.style= "border: 1px solid#00FF00";
											document.getElementById('idMsgErro').replaceChild(document.createTextNode("Usuário disponível"), document.getElementById('idMsgErro').firstChild);
									}									
								} else {
											campoUsername.style = "border: 1px solid #FF0000";
											document.getElementById('idMsgErro').replaceChild(document.createTextNode("Usuário inválido"), document.getElementById('idMsgErro').firstChild);
								}
            }
        }
        xmlhttp.send(null);
    });
}