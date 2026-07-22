**Afficher le code source de la page (compatible avec les appareils mobiles)**
`javascript:void(document.location='view-source:'+document.location)`

**Extraire tous les liens de la page actuelle**
`javascript:void(function(){var links=document.querySelectorAll('a[href]');var output='';links.forEach(function(a){output+=a.href+'\n';});var w=window.open('','_blank');w.document.write('<pre>'+output+'</pre>');})()`

**Extraire toutes les images de la page actuelle**
`javascript:void(function(){var imgs=document.querySelectorAll('img[src]');var output='';imgs.forEach(function(img){output+='<img src="'+img.src+'" style="max-width:200px;margin:5px"><br>'+img.src+'<br><br>';});var w=window.open('','_blank');w.document.write(output);})()`

**Consultez la Wayback Machine pour la page actuelle**
`javascript:void(window.open('https://web.archive.org/web/*/'+document.location.href))`

**Cache Google de la page actuelle**
`javascript:void(window.open('https://webcache.googleusercontent.com/search?q=cache:'+document.location.href))`

**Recherche d'image inversée (Google) pour l'image sélectionnée**
`javascript:void(function(){var imgs=document.querySelectorAll('img');imgs.forEach(function(img){img.style.cursor='crosshair';img.onclick=function(e){e.preventDefault();window.open('https://lens.google.com/uploadbyurl?url='+encodeURIComponent(this.src));};});})()`

**Mettre en surbrillance toutes les adresses e-mail sur la page**
`javascript:void(function(){var body=document.body.innerHTML;var emails=body.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g);if(emails){alert('Found '+emails.length+' emails:\n\n'+[...new Set(emails)].join('\n'));}else{alert('No email addresses found.');}})()`

**Afficher les champs de formulaire cachés**
`javascript:void(function(){var hidden=document.querySelectorAll('input[type=hidden]');hidden.forEach(function(h){h.type='text';h.style.border='2px solid red';h.style.background='yellow';});alert(hidden.length+' hidden fields revealed.');})()`

